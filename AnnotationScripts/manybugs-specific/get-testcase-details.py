# PURPOSE: script to compute test case details for all defects of ManyBugs. 
# INPUT: script requires ManyBugs scenarios available at http://repairbenchmarks.cs.umass.edu/ManyBugs/scenarios/
# OUTPUT: output of this script is ManyBugsRelevantTests.csv file that lists DefectID.ManyBugs185, PositiveTestCount, NegativeTestCount, RelevantTestCount, TriggeringTestCount for all the ManyBugs scenarios. 
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

for scenario in scenarios:
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

outputfile = open("ManyBugsTestCounts.csv", 'w')
outputfile.write("DefectID.ManyBugs185, PositiveTestCount, NegativeTestCount, RelevantTestCount, TriggeringTestCount\n")
for defect in sorted(relevanttests):
        outputline = defect + ", " + str(relevanttests[defect][0]) + ", " + str(relevanttests[defect][1]) + ", " + str(relevanttests[defect][2]) + ", " + str(relevanttests[defect][1]) + "\n"
        outputfile.write(outputline)

