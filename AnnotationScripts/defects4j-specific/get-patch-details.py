# script to compute patch complexity from minimized patches of all defects of Defects4J.
# this script uses data stored in all_diffs.csv and stores it in patch_complexity.csv
# that lists ProjectId(PID), DefectIf(BID), FILECOUNT, LINECOUNT for all the defects
# run the script by using command: python get-patch-details.py

diffFile = open("all_diffs.csv", 'r')
patchdetails = {}
linecount = {}
filecount = {}

for line in diffFile:
	print line
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
		

outputfile = open("patch_complexity.csv", 'w')
outputfile.write("PID, BID, FILECOUNT, LINECOUNT\n")
count = 1
for dictkey in sorted(patchdetails):	
	outputline = dictkey[0] + ", " + dictkey[1] + ", " + str(filecount[dictkey]) + ", " + str(linecount[dictkey]) + "\n"
	outputfile.write(outputline)
	count += 1


