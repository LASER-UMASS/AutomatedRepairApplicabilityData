# PURPOSE: script to compute test case details for all defects of ManyBugs. The number of relevant tests is computed by counting the total number of positive and negative tests encoded in test.sh script available inside each defect and the number of triggering tests is equal to the number of negative tests in that script. 
# INPUT: script requires ManyBugs scenarios available at http://repairbenchmarks.cs.umass.edu/ManyBugs/scenarios/
# OUTPUT: output of this script is ManyBugsTestCounts.csv file that lists Project, DefectId, RelevantTestCount and TriggeringTestCount for all the ManyBugs defects. 
# HOW TO RUN: run the script by using command: python get-testcase-details.py <path to ManyBugs scenarios>

import os
import re
import tarfile
import sys

if len(sys.argv) < 2:
	print "ERROR: Please provide path to ManyBugs scenarios"
	sys.exit()

repoPath = str(sys.argv[1])                           # path to ManyBugs scenarios 
scenarios = os.listdir(repoPath)

postestpattern = re.compile('p[0-9]+\) ')
negtestpattern = re.compile('n[0-9]+\) ')
relevanttests = {}

# read the tar file for each scenario, fetch the test.sh script and identify and store the number of positive and negative tests utilizing the above regular expressions 
for scenario in sorted(scenarios):
        scenario_list = scenario.split(".tar.gz")[0].split('-')
	project = scenario_list[0]
        buggyversion = scenario_list[len(scenario_list)-2]
        fixedversion = scenario_list[len(scenario_list)-1]
	print project, buggyversion, fixedversion
	scenariotar = tarfile.open(repoPath + scenario)
        postestcount = 0
        negtestcount = 0
	totalreltests = 0
        for filename in scenariotar.getnames():
                if filename.endswith("test.sh"):
			tardiff=scenariotar.extractfile(filename)
                        diffline = tardiff.readline()
			while(diffline):
                        	diffline = tardiff.readline()
				if postestpattern.match(diffline.strip()):
					postestcount += 1
				elif negtestpattern.match(diffline.strip()):
					negtestcount += 1					
  	relevanttests[scenario] = (postestcount, negtestcount, postestcount + negtestcount)

# write the data extracted to the output file
outputfile = open("ManyBugsTestCounts.csv", 'w')
outputfile.write("Project,DefectId,RelevantTestCount,TriggeringTestCount\n")
for scenario in sorted(relevanttests):
        scenario_list = scenario.split(".tar.gz")[0].split('-')
	project = scenario_list[0]
        defectid = scenario.split("-bug-")[1].split('.tar.gz')[0]
        outputline = project + "," + defectid + "," + str(relevanttests[scenario][2]) + "," + str(relevanttests[scenario][1]) + "\n"
	outputfile.write(outputline)

outputfile.close()
