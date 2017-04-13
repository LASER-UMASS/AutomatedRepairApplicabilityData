# script to compute test case details for all defects of ManyBugs. 
# script requires ManyBugs scenarios available at http://repairbenchmarks.cs.umass.edu/ManyBugs/scenarios/
# run the script by using command: python get-testcase-details.py
# output of this script is ManyBugsRelevantTests.csv file that lists 
# SCENARIO, POSITIVE_TESTS_COUNT, NEGATIVE_TESTS_COUNT, RELEVANT_TESTS_COUNT, TRIGGERING_TESTS_COUNT 
# for all the ManyBugs scenarios. 

import os
import re
import tarfile

repoPath = "~/Downloads/ManyBugs_Scenarios/"   # path to ManyBugs scenarios 
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

outputfile = open("ManyBugsTests.csv", 'w')
outputfile.write("SCENARIO, POSITIVE_TESTS_COUNT, NEGATIVE_TESTS_COUNT, RELEVANT_TESTS_COUNT, TRIGGERING_TESTS_COUNT\n")
for defect in sorted(relevanttests):
        outputline = defect + ", " + str(relevanttests[defect][0]) + ", " + str(relevanttests[defect][1]) + ", " + str(relevanttests[defect][2]) + ", " + str(relevanttests[defect][1]) + "\n"
        outputfile.write(outputline)

