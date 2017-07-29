#!/bin/bash

# PURPOSE: script to compute test case details for all defects of Defects4J
# INPUT: path to defects4j installation directory, project, start defect ID and end defect ID are specified as command-line arguments
# OUTPUT: output of this script is Defects4JTests.csv file that lists Project, DefectId, RelevantTestCount and TriggeringTestCount. 
# HOW TO RUN: run the script by using command: bash getTestcaseDetails.sh <project> <start defectID> <end defect ID> (e.g. bash getTestcaseDetails.sh Chart 1 26)
# REQUIREMENTS AND DEPENDENCIES: script requires Defects4J installed on system and environment variable PATH must include <path-to-defects4j>/framework/bin"

if [ "$#" -ne 3 ]; then
    echo "Illegal number of arguments. Usage: bash getTestcaseDetails.sh <project> <start defectID> <end defect ID>"
    exit 1 	
fi

PROJECT=$1
START=$2
END=$3

if [ ! -f Defects4JTests.csv ]; then
    echo -e "Project"' \t '"DefectId"' \t '"RelevantTestCount"' \t '"TriggeringTestCount" > Defects4JTests.csv
fi

for (( BUG=$START; BUG<=$END; BUG++ ))
do 
	DIR="${PROJECT}""${BUG}"Buggy
	echo $DIR
	defects4j checkout -p "$PROJECT" -v "${BUG}b" -w "$DIR" 
	cd "$DIR"
	JAVACLASSPATH="../bin/:.:$(defects4j export -p cp.compile):$(defects4j export -p cp.test)"
	defects4j compile
	defects4j export -p tests.relevant -o relevant-test-classes.txt
	defects4j export -p tests.trigger -o triggering-tests.txt
	echo "######### PROJECT PREPARED ###############"
	cd ..
	if [  -f /tmp/foo.txt ]; then
		rm *.class
	fi
	javac -cp "${JAVACLASSPATH}" TestMethod.java 
	javac -cp "${JAVACLASSPATH}" TestFinder.java 
	RELTESTDETAILS="$(java -cp "${JAVACLASSPATH}" TestFinder "${DIR}"/relevant-test-classes.txt)"
	lcount=$(cat "${DIR}"/triggering-tests.txt | wc -l)
# 	echo $RELTESTDETAILS
	TRIGTESTCOUNT="$(expr 1 + $lcount)"
	echo "${RELTESTDETAILS}" > "$DIR"/relevant-test-methods.txt
	RELTESTCOUNT="$(wc -l "${DIR}"/relevant-test-methods.txt | grep -o "[0-9]* ")"
	echo -e "${PROJECT}"' \t '"${BUG}"' \t '"${RELTESTCOUNT}"' \t '"${TRIGTESTCOUNT}"
	echo -e "${PROJECT}"' \t '"${BUG}"' \t '"${RELTESTCOUNT}"' \t '"${TRIGTESTCOUNT}" >> Defects4JTests.csv
	echo 
	rm -rf "$DIR"
	echo -e "######################################### COMPUTED COUNTS ############################################"
done
