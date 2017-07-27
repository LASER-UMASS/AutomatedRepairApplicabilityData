# PURPOSE: script to compute patch complexity from minimized patches of all defects from ManyBugs.
# INPUT: script requires path to ManyBugs scenarios downloaded from http://repairbenchmarks.cs.umass.edu/ManyBugs/scenarios/
# OUTPUT: output of this script is ManyBugsPatchComplexity.csv file that lists DefectID.ManyBugs185, FileCount, Insertions, Deletions, Modifications, LineCount for all the scenarios. 
# HOW TO RUN: run the script by using command: python get-minimized-patch-complexity.py <path to ManyBugs scenarios>

import os
import commands
import subprocess
import tarfile
import re
import sys

if len(sys.argv) < 2:
        print "ERROR: Please provide path to ManyBugs scenarios"
        sys.exit()

repoPath = str(sys.argv[1])                           # path to ManyBugs scenarios 
scenarios = os.listdir(repoPath)
inserted = {}
deleted = {}
modified = {}
filecount = {}

def remove_comments(text):
    """ remove c-style comments.
        text: blob of text with comments (can include newlines)
        returns: text with comments removed
    """
    pattern = r"""
                            ##  --------- COMMENT ---------
           /\*              ##  Start of /* ... */ comment
           [^*]*\*+         ##  Non-* followed by 1-or-more *'s
           (                ##
             [^/*][^*]*\*+  ##
           )*               ##  0-or-more things which don't start with /
                            ##    but do end with '*'
           /                ##  End of /* ... */ comment
         |                  ##  -OR-  various things which aren't comments:
           (                ## 
                            ##  ------ " ... " STRING ------
             "              ##  Start of " ... " string
             (              ##
               \\.          ##  Escaped char
             |              ##  -OR-
               [^"\\]       ##  Non "\ characters
             )*             ##
             "              ##  End of " ... " string
           |                ##  -OR-
                            ##
                            ##  ------ ' ... ' STRING ------
             '              ##  Start of ' ... ' string
             (              ##
               \\.          ##  Escaped char
             |              ##  -OR-
               [^'\\]       ##  Non '\ characters
             )*             ##
             '              ##  End of ' ... ' string
           |                ##  -OR-
                            ##
                            ##  ------ ANYTHING ELSE -------
             .              ##  Anything other char
             [^/"'\\]*      ##  Chars which doesn't start a comment, string
           )                ##    or escape
    """
    regex = re.compile(pattern, re.VERBOSE|re.MULTILINE|re.DOTALL)
    noncomments = [m.group(2) for m in regex.finditer(text) if m.group(2)]

    return "".join(noncomments)

def remove_spaces(text):
	newtext = ""
	linelist = text.split('\n')
	for line in linelist:
		if len(line.strip())>0:
			newtext = newtext + line.strip() + "\n"
	return newtext


for scenario in scenarios:
	scenario_list = scenario.split(".tar.gz")[0].split('-')
	buggyversion = scenario_list[len(scenario_list)-2]
	fixedversion = scenario_list[len(scenario_list)-1]
        print buggyversion, fixedversion

        scenariotar = tarfile.open(repoPath + scenario)
        filect = 0
	buggy = ""
	fixed = ""
	buggyflag = False
	fixedflag = False
        for filename in sorted(scenariotar.getnames()):
                if "/diffs/" in filename and ".c-" in filename and buggyversion in filename.split(".c-")[1]:
                	buggyflag = True
		       	tardiff=scenariotar.extractfile(filename)
    		       	code_w_comments = tardiff.read()
                       	code_wo_comments = remove_comments(code_w_comments)
			code_wo_spaces = remove_spaces(code_wo_comments)
    			fh = open("buggy", "w+")
    			fh.write(code_wo_spaces)
    			fh.close()
                if "/diffs/" in filename and ".c-" in filename and fixedversion in filename.split(".c-")[1]:
			fixedflag = True
		       	tardiff=scenariotar.extractfile(filename)
    		       	code_w_comments = tardiff.read()
                       	code_wo_comments = remove_comments(code_w_comments)
			code_wo_spaces = remove_spaces(code_wo_comments)
    			fh = open("fixed", "w+")
    			fh.write(code_wo_spaces)
    			fh.close()
		if buggyflag is True and fixedflag is True:
			diffoutput = commands.getoutput("diff -u buggy fixed")
			if diffoutput:
 	   			fd = open("diffoutput", "w+")
				fd.write(diffoutput)
				fd.close()
				diffstatoutput = commands.getoutput("cat diffoutput | diffstat -m -t")
				if "\n" in diffstatoutput:
					filect += 1
					diffstatoutput = diffstatoutput.split('\n')
					stats = diffstatoutput[1].split(',')
					if scenario in inserted:
						inserted[scenario] = int(inserted[scenario]) + int(stats[0])
						deleted[scenario] = int(deleted[scenario]) + int(stats[1])
						modified[scenario] = int(modified[scenario]) + int(stats[2])
					else:
						inserted[scenario] = int(stats[0])
						deleted[scenario] = int(stats[1])
						modified[scenario] = int(stats[2])

			buggyflag = False
			fixedflag = False
	filecount[scenario] = filect
	scenariotar.close()

outputfile = open("ManyBugsPatchComplexity.csv", 'w')
outputfile.write("DefectID.ManyBugs185, FileCount, Insertions, Deletions, Modifications, LineCount\n")
for defect in sorted(inserted):
	totallines = int(inserted[defect]) + int(deleted[defect]) + int(modified[defect])
        outputline = defect + ", " + str(filecount[defect]) + ", " + str(inserted[defect]) + ", " + str(deleted[defect]) + ", " + str(modified[defect]) + ", " + str(totallines) + "\n"
        outputfile.write(outputline)