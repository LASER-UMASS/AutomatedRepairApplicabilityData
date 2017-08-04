#!/usr/bin/env bash

# PURPOSE: script to compute test case details for all defects of Defects4J
# INPUT: path to defects4j installation directory, project, start defect ID and end defect ID are specified as command-line arguments
# OUTPUT: output of this script is Defects4JTestCounts.csv file that lists Project, DefectId, RelevantTestCount and TriggeringTestCount. 
# HOW TO RUN: run the script by using command: bash getTestcaseDetails.sh <path-to-Defects4J> <project> <start defectID> <end defect ID> (e.g. bash getTestcaseDetails.sh ~/defects4j Chart 1 26)
# REQUIREMENTS AND DEPENDENCIES: script requires Defects4J installed on system and environment variable D4J_HOME should be set to <path-to-defects4j>, TestFinder.java and TestMethod.java files located in the same directory as this script"


if [ "$#" -ne 4 ]; then
    echo "Illegal number of arguments. Usage: bash getTestcaseDetails.sh <path-to-Defects4J> <Project> <start DefectId> <end DefectId>"
    exit 1 	
fi

D4J_HOME=$1
PROJECT=$2
START=$3
END=$4

if [ ! -f Defects4JTestCounts.csv ]; then
    echo -e "Project"','"DefectId"','"RelevantTestCount"','"TriggeringTestCount" > Defects4JTestCounts.csv
fi

for (( BUG=$START; BUG<=$END; BUG++ ))
do 
	DIR="${PROJECT}""${BUG}"Buggy
	echo $DIR
	defects4j checkout -p "$PROJECT" -v "${BUG}b" -w "$DIR" 
	cd "$DIR"
	JAVACLASSPATH="../bin/:.:$D4J_HOME/framework/projects/lib/junit-4.11.jar:$($D4J_HOME/framework/bin/defects4j export -p cp.compile):$($D4J_HOME/framework/bin/defects4j export -p cp.test)"
	$D4J_HOME/framework/bin/defects4j compile
	$D4J_HOME/framework/bin/defects4j export -p tests.relevant -o relevant-test-classes.txt
	$D4J_HOME/framework/bin/defects4j export -p tests.trigger -o triggering-tests.txt
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
	echo -e "${PROJECT}"','"${BUG}"','"${RELTESTCOUNT}"','"${TRIGTESTCOUNT}" >> Defects4JTestCounts.csv
	echo 
	rm -rf "$DIR"
done
