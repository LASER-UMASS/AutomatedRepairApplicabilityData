# PURPOSE:script to compute patch complexity from minimized patches of all defects of Defects4J.
# INPUT: this script uses data stored in all_diffs.csv (generated using script categorize_patches.sh provided by Defects4J authors) 
# OUTPUT: this script generates a file Defects4JPatchComplexity.csv that lists Project, DefectId, FileCount, and LineCount for all the defects
# HOW TO RUN: run the script by using command: python get-patch-details.py

import operator
diffFile = open("all_diffs.csv", 'r')
patchdetails = {}
linecount = {}
filecount = {}
outputfile = open("Defects4JPatchComplexity.csv", 'w')
outputfile.write("Project,DefectId,FileCount,LineCount\n")


def writeToFile(project, totaldefects):
	for i in range(1, totaldefects+1):
		dictkey = (project,str(i))
		outputline = project + "," + str(i) + "," + str(filecount[dictkey]) + "," + str(linecount[dictkey]) + "\n"
		outputfile.write(outputline)


for line in diffFile:
	if not "PID" in line:
		line = line.split(',')
		PID = line[0].strip()
		BID = line[1].strip()
		File = line[2].strip()
		INS = line[3].strip()
		DEL = line[4].strip()
		MOD = line[5].strip()
		dictkey = (PID,BID)
		if not dictkey in patchdetails:
			patchdetails[dictkey] = File + ":" + INS + ":" + DEL + ":" + MOD
			linecount[dictkey] = int(INS) + int(DEL) + int(MOD)
			filecount[dictkey] = 1
		else:
			existingpatch = patchdetails[dictkey]
			newpatch = existingpatch + "::" + File + ":" + INS + ":" + DEL + ":" + MOD
			patchdetails[dictkey] = newpatch
			linecount[dictkey] = int(linecount[dictkey]) + int(INS) + int(DEL) + int(MOD)
			filecount[dictkey] = int(filecount[dictkey]) + 1

writeToFile("Chart", 26)
writeToFile("Math", 106)
writeToFile("Lang", 65)
writeToFile("Time", 27)

outputfile.close()
