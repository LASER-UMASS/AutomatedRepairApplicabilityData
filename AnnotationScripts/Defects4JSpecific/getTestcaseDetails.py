# PURPOSE: script to compute test case details for all defects of Defects4J
# INPUT: path to defects4j installation directory is specified as command-line argument
# OUTPUT: output of this script is Defects4JTests.csv file that lists Project, DefectId, RelevantTestCount, TriggeringTestCount, DependentClasses for all the Defects4J scenarios. 
# HOW TO RUN: run the script by using command: python get-testcase-details.py <path-to-defects4j>
# REQUIREMENTS AND DEPENDENCIES: script requires Defects4J installed on system"

import os
import sys

if len(sys.argv) < 2:
        print "ERROR: Please provide path to Defects4J directory"
        sys.exit()

defects4jpath = str(sys.argv[1])                           # path to Defects4J 
count=0
outputfile = open("Defects4JTestCounts.csv", 'w')
outputfile.write("Project, BugID, Relevant, Triggering, Dependent\n")

#1 Chart
proj= "Chart"
classes = set()
defects = {}
charttests = []

#relevant
os.chdir(defects4jpath + "framework/projects/" + proj + "/relevant_tests/")
currentpath = os.getcwd()
list = os.listdir(currentpath)
for l in list:
    relevant=0
    with open(currentpath+"/"+str(l),"r") as fo :
        for line in fo:
			relevant=relevant+1
			if line not in charttests:
				charttests.append(line)
        defects[proj+l]=str(relevant)
    fo.close()

#triggering and dependent
os.chdir(defects4jpath + "framework/projects/" + proj + "/trigger_tests/")
currentpath = os.getcwd()
list = os.listdir(currentpath)
for l in list:
    classes.clear()
    triggering=0
    with open(currentpath+"/"+str(l),"r") as fo :
        for line in fo:
            if line.find("---")!=-1 :
				triggering=triggering+1
				if line not in charttests:
					charttests.append(line)
            if line.find("(")!=-1 & line.find(")")!=-1 & line.find(".")!=-1 & line.find("j")!=-1:
                start = line.find("(")+1
                end = line.find(":")
                sub = line[start:end]
                classes.add(sub)
        dependent = len(classes)
        defects[proj+l]=defects[proj+l]+", "+str(triggering)+", "+str(dependent)
    fo.close()
for i in range(1,len(list)+1):
    outputfile.write(proj+", "+str(i)+", "+defects[proj+str(i)]+"\n")

#2 Closure
proj= "Closure"
classes = set()
defects = {}

#relevant
os.chdir(defects4jpath + "framework/projects/" + proj + "/relevant_tests/")
currentpath = os.getcwd()
list = os.listdir(currentpath)
for l in list:
    relevant=0
    with open(currentpath+"/"+str(l),"r") as fo :
        for line in fo:
            relevant=relevant+1
        defects[proj+l]=str(relevant)
    fo.close()

#triggering and dependent
os.chdir(defects4jpath + "framework/projects/" + proj + "/trigger_tests/")
currentpath = os.getcwd()
list = os.listdir(currentpath)
for l in list:
    classes.clear()
    triggering=0
    with open(currentpath+"/"+str(l),"r") as fo :
        for line in fo:
            if line.find("---")!=-1 :
                triggering=triggering+1
            if line.find("(")!=-1 & line.find(")")!=-1 & line.find(".")!=-1 & line.find("j")!=-1:
                start = line.find("(")+1
                end = line.find(":")
                sub = line[start:end]
                classes.add(sub)
        dependent = len(classes)
        defects[proj+l]=defects[proj+l]+", "+str(triggering)+", "+str(dependent)
    fo.close()
for i in range(1,len(list)+1):
    outputfile.write(proj+", "+str(i)+", "+defects[proj+str(i)]+"\n")


#3 Lang
proj= "Lang"
classes = set()
defects = {}

#relevant
os.chdir(defects4jpath + "framework/projects/" + proj + "/relevant_tests/")
currentpath = os.getcwd()
list = os.listdir(currentpath)
for l in list:
    relevant=0
    with open(currentpath+"/"+str(l),"r") as fo :
        for line in fo:
            relevant=relevant+1
        defects[proj+l]=str(relevant)
    fo.close()

#triggering and dependent
os.chdir(defects4jpath + "framework/projects/" + proj + "/trigger_tests/")
currentpath = os.getcwd()
list = os.listdir(currentpath)
for l in list:
    if l!="1~":
        classes.clear()
        triggering=0
        with open(currentpath+"/"+str(l),"r") as fo :
            for line in fo:
                if line.find("---")!=-1 :
                    triggering=triggering+1
                if line.find("(")!=-1 & line.find(")")!=-1 & line.find(".")!=-1 & line.find("j")!=-1:
                    start = line.find("(")+1
                    end = line.find(":")
                    sub = line[start:end]
                    classes.add(sub)
            dependent = len(classes)
            defects[proj+l]=defects[proj+l]+", "+str(triggering)+", "+str(dependent)
        fo.close()
for i in range(1,len(list)+1):
    outputfile.write(proj+", "+str(i)+", "+defects[proj+str(i)]+"\n")

#4 Math
proj= "Math"
classes = set()
defects = {}

#relevant
os.chdir(defects4jpath + "framework/projects/" + proj + "/relevant_tests/")
currentpath = os.getcwd()
list = os.listdir(currentpath)
for l in list:
    relevant=0
    with open(currentpath+"/"+str(l),"r") as fo :
        for line in fo:
            relevant=relevant+1
        defects[proj+l]=str(relevant)
    fo.close()

#triggering and dependent
os.chdir(defects4jpath + "framework/projects/" + proj + "/trigger_tests/")
currentpath = os.getcwd()
list = os.listdir(currentpath)
for l in list:
    classes.clear()
    triggering=0
    with open(currentpath+"/"+str(l),"r") as fo :
        for line in fo:
            if line.find("---")!=-1 :
                triggering=triggering+1
            if line.find("(")!=-1 & line.find(")")!=-1 & line.find(".")!=-1 & line.find("j")!=-1:
                start = line.find("(")+1
                end = line.find(":")
                sub = line[start:end]
                classes.add(sub)
        dependent = len(classes)
        defects[proj+l]=defects[proj+l]+", "+str(triggering)+", "+str(dependent)
    fo.close()
for i in range(1,len(list)+1):
    outputfile.write(proj+", "+str(i)+", "+defects[proj+str(i)]+"\n")


#5 Time
proj= "Time"
classes = set()
defects = {}

#relevant
os.chdir(defects4jpath + "framework/projects/" + proj + "/relevant_tests/")
currentpath = os.getcwd()
list = os.listdir(currentpath)
for l in list:
    relevant=0
    with open(currentpath+"/"+str(l),"r") as fo :
        for line in fo:
            relevant=relevant+1
        defects[proj+l]=str(relevant)
    fo.close()

#triggering and dependent
os.chdir(defects4jpath + "framework/projects/" + proj + "/trigger_tests/")
currentpath = os.getcwd()
list = os.listdir(currentpath)
for l in list:
    classes.clear()
    triggering=0
    with open(currentpath+"/"+str(l),"r") as fo :
        for line in fo:
            if line.find("---")!=-1 :
                triggering=triggering+1
            if line.find("(")!=-1 & line.find(")")!=-1 & line.find(".")!=-1 & line.find("j")!=-1:
                start = line.find("(")+1
                end = line.find(":")
                sub = line[start:end]
                classes.add(sub)
        dependent = len(classes)
        defects[proj+l]=defects[proj+l]+", "+str(triggering)+", "+str(dependent)
    fo.close()
for i in range(1,len(list)+1):
    outputfile.write(proj+", "+str(i)+", "+defects[proj+str(i)]+"\n")


