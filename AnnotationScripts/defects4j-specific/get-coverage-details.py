# script to get coverage of test suite for Defects4J defects

# script requires Defects4J installed on system and enviorinment variable PATH should include "<path-to-defects4j>/framework/bin"
# script requires <path-to-defects4j> as command line argument

# output of the script is Defects4JCoverage.csv that lists 
# Project, DefectId, LinesTotal, LinesCovered, ConditionsTotal, ConditionsCovered, StatementCoverage, ConditionCoverage
# for all the defects of Defects4J

# run the script using command: python get-coverage-details.py <path-to-defects4j>

import os
import commands
import sys

if len(sys.argv) < 2:
        print "ERROR: Please provide path to Defects4J directory"
        sys.exit()

defects4jpath = str(sys.argv[1])                           # path to Defects4J 
os.chdir(defects4jpath)  
outputfile = open("Defects4JCoverage.csv", 'w')			
outputfile.write("Project, DefectId, LinesTotal, LinesCovered, ConditionsTotal, ConditionsCovered, StatementCoverage, ConditionCoverage\n")

#1 Chart
proj = "Chart"
for i in range(1,27):
    command = "defects4j checkout -p "+proj+" -v "+str(i)+"b -w /tmp/chart_"+str(i)
    print command
    checkoutput = commands.getoutput(command)
    if checkoutput:
        os.chdir("/tmp/chart_"+str(i))
        covoutput = commands.getoutput("defects4j coverage")
        print covoutput
	lines = covoutput.split('\n')
        found=0
        for l in lines:
            if l.find("Lines total:")!=-1 :
                found=found+1
                out1 = l[l.find(":")+2:len(l)]
            if l.find("Lines covered:")!=-1 :
                found=found+1
                out2 = l[l.find(":")+2:len(l)]
            if l.find("Conditions total:")!=-1 :
                found=found+1
                out3 = l[l.find(":")+2:len(l)]
            if l.find("Conditions covered:")!=-1 :
                found=found+1
                out4 = l[l.find(":")+2:len(l)]
            if l.find("Line coverage:")!=-1 :
                found=found+1
                out5 = l[l.find(":")+2:len(l)]
            if l.find("Condition coverage:")!=-1 :
                found=found+1
                out6 = l[l.find(":")+2:len(l)]
        if found==6:
            outline = proj+", "+str(i)+", "+str(out1)+", "+str(out2)+", "+str(out3)+", "+str(out4)+", "+str(out5)+", "+str(out6)
            outputfile.write(outline)
            outputfile.write('\n')

#2 Closure
proj = "Closure"
for i in range(1,134):
    command = "defects4j checkout -p "+proj+" -v "+str(i)+"b -w /tmp/closure_"+str(i)
    checkoutput = commands.getoutput(command)
    if checkoutput:
        os.chdir("/tmp/closure_"+str(i))
        covoutput = commands.getoutput("defects4j coverage")
        lines = covoutput.split('\n')
        found=0
        for l in lines:
            if l.find("Lines total:")!=-1 :
                found=found+1
                out1 = l[l.find(":")+2:len(l)]
            if l.find("Lines covered:")!=-1 :
                found=found+1
                out2 = l[l.find(":")+2:len(l)]
            if l.find("Conditions total:")!=-1 :
                found=found+1
                out3 = l[l.find(":")+2:len(l)]
            if l.find("Conditions covered:")!=-1 :
                found=found+1
                out4 = l[l.find(":")+2:len(l)]
            if l.find("Line coverage:")!=-1 :
                found=found+1
                out5 = l[l.find(":")+2:len(l)]
            if l.find("Condition coverage:")!=-1 :
                found=found+1
                out6 = l[l.find(":")+2:len(l)]
        if found==6:
            outline = proj+", "+str(i)+", "+str(out1)+", "+str(out2)+", "+str(out3)+", "+str(out4)+", "+str(out5)+", "+str(out6)
            outputfile.write(outline)
            outputfile.write('\n')


#3 Lang
proj = "Lang"
for i in range(1,66):
    command = "defects4j checkout -p "+proj+" -v "+str(i)+"b -w /tmp/lang_"+str(i)
    checkoutput = commands.getoutput(command)
    if checkoutput:
        os.chdir("/tmp/lang_"+str(i))
        covoutput = commands.getoutput("defects4j coverage")
        lines = covoutput.split('\n')
        found=0
        for l in lines:
            if l.find("Lines total:")!=-1 :
                found=found+1
                out1 = l[l.find(":")+2:len(l)]
            if l.find("Lines covered:")!=-1 :
                found=found+1
                out2 = l[l.find(":")+2:len(l)]
            if l.find("Conditions total:")!=-1 :
                found=found+1
                out3 = l[l.find(":")+2:len(l)]
            if l.find("Conditions covered:")!=-1 :
                found=found+1
                out4 = l[l.find(":")+2:len(l)]
            if l.find("Line coverage:")!=-1 :
                found=found+1
                out5 = l[l.find(":")+2:len(l)]
            if l.find("Condition coverage:")!=-1 :
                found=found+1
                out6 = l[l.find(":")+2:len(l)]
        if found==6:
            outline = proj+", "+str(i)+", "+str(out1)+", "+str(out2)+", "+str(out3)+", "+str(out4)+", "+str(out5)+", "+str(out6)
            outputfile.write(outline)
            outputfile.write('\n')

#4 Math
proj = "Math"
for i in range(1,107):
    command = "defects4j checkout -p "+proj+" -v "+str(i)+"b -w /tmp/math_"+str(i)
    checkoutput = commands.getoutput(command)
    if checkoutput:
        os.chdir("/tmp/math_"+str(i))
        covoutput = commands.getoutput("defects4j coverage")
        lines = covoutput.split('\n')
        found=0
        for l in lines:
            if l.find("Lines total:")!=-1 :
                found=found+1
                out1 = l[l.find(":")+2:len(l)]
            if l.find("Lines covered:")!=-1 :
                found=found+1
                out2 = l[l.find(":")+2:len(l)]
            if l.find("Conditions total:")!=-1 :
                found=found+1
                out3 = l[l.find(":")+2:len(l)]
            if l.find("Conditions covered:")!=-1 :
                found=found+1
                out4 = l[l.find(":")+2:len(l)]
            if l.find("Line coverage:")!=-1 :
                found=found+1
                out5 = l[l.find(":")+2:len(l)]
            if l.find("Condition coverage:")!=-1 :
                found=found+1
                out6 = l[l.find(":")+2:len(l)]
        if found==6:
            outline = proj+", "+str(i)+", "+str(out1)+", "+str(out2)+", "+str(out3)+", "+str(out4)+", "+str(out5)+", "+str(out6)
            outputfile.write(outline)
            outputfile.write('\n')

#5 Time
proj = "Time"
for i in range(1,28):
    command = "defects4j checkout -p "+proj+" -v "+str(i)+"b -w /tmp/time_"+str(i)
    checkoutput = commands.getoutput(command)
    if checkoutput:
        os.chdir("/tmp/time_"+str(i))
        covoutput = commands.getoutput("defects4j coverage")
        lines = covoutput.split('\n')
        found=0
        for l in lines:
            if l.find("Lines total:")!=-1 :
                found=found+1
                out1 = l[l.find(":")+2:len(l)]
            if l.find("Lines covered:")!=-1 :
                found=found+1
                out2 = l[l.find(":")+2:len(l)]
            if l.find("Conditions total:")!=-1 :
                found=found+1
                out3 = l[l.find(":")+2:len(l)]
            if l.find("Conditions covered:")!=-1 :
                found=found+1
                out4 = l[l.find(":")+2:len(l)]
            if l.find("Line coverage:")!=-1 :
                found=found+1
                out5 = l[l.find(":")+2:len(l)]
            if l.find("Condition coverage:")!=-1 :
                found=found+1
                out6 = l[l.find(":")+2:len(l)]
        if found==6:
            outline = proj+", "+str(i)+", "+str(out1)+", "+str(out2)+", "+str(out3)+", "+str(out4)+", "+str(out5)+", "+str(out6)
            outputfile.write(outline)
            outputfile.write('\n')


