# Automated repair applicability data 

This project contains data and scripts that extend the
[ManyBugs](http://repairbenchmarks.cs.umass.edu/) and
[Defects4J](https://github.com/rjust/defects4j) benchmarks to enable the
evaluation of automated program repair's applicability to defects, For
example, these data enable evaluating if automated repair techniques are able
to produce patches for defects considered hard or important by developers. 

## Data 

ManyBugs.csv and Defects4J.csv files, respectively, contain annotations for
the 185 defects from the [ManyBugs](http://repairbenchmarks.cs.umass.edu/)
benchmark, and 224 defects from the
[Defects4J](https://github.com/rjust/defects4j) benchmark. These annotations
include:

1. Eleven abstract parameters describing defect properties derived from bug tracking systems and the benchmarks.

2. For which defects nine automated repair techniques produce patches, and
the quality of those patches. The ManyBugs benchmark contains these data for
six C techniques: GenProg, TrpAutoRepair, AE, SPR, Prophet, and Kali. (SPR,
Prophet, and Kali are evaluated on an 105-defect subset of ManyBugs.) The
Defects4J benchmark contains these data for three Java techniques: GenProg,
Kali, and Nopol. (These techniques were evaluated on a 224-defect subset of
Defects4J.)

### The eleven abstract parameters

The defects are annotated with the following abstract parameters, when the relevant data is available: 

1. FileCount
   - Data-type:integer
   - Possible values: >=1 
   - Description: the number of files containing non-comment, non-blank lines edited by the developer-written patch.
2. LineCount
   - Data-type:integer
   - Possible values: >=1 
   - Description: the total number of non-comment, non-blank lines edited by the developer-written patch.
3. RelevantTestCount	
   - Data-type:integer
   - Possible values: >=1 
   - Description: number of test cases that execute at least one statement in at least one file edited by the developer-written patch.
4. TriggeringTestCount	
   - Data-type:integer
   - Possible values: >=1 
   - Description: number of defect-triggering test cases
5. StatementCoverage	
   - Data-type:double
   - Possible values: >=0 and <=100, NA (information not available)
   - Description: the percent of the lines in the files edited by the developer-written patch that are executed by the test suite
6. TimeToFix	
   - Data-type:double
   - Possible values: >0, NA (information not available)
   - Description: the difference, in days, between when the defect's issue
     was reported and when that issue was resolved.
7. Versions	
   - Data-type:integer
   - Possible values: >=1, NA (information not available)
   - Description: number of project versions or project modules and components affected by the defect.
8. Priority	
   - Data-type:integer
   - Possible values: 1, 2, 3, 4, 5, NA (information not available)
   - Description: the priority assigned to the defect's issue in the bug
     tracking system. Different bug tracking systems use different values to
     denote low, normal, high, critical, and blocker defects. We map these
     values to a scale of 1 (lowest) to 5 (higher).
9. Dependents	
   - Data-type:integer
   - Possible values: >=1, NA (information not available)
   - Description: number of defects (with URLs to a bug tracking system) on which the defect's issue depends.
9. Reproducibility	
   - Data-type:double
   - Possible values: >=0 and <=1 NA (information not available)
   - Description: how easy it is to reproduce the defect by developer (0 indicates defect is non-determinitsic and 1 indicates defect is reproducible).
11. PatchCharacteristics
    - Data-type:integer
    - Possible values: 0,1 
    - Description: characteristics of the developer-written patch in terms of
      the type of code modifications. This information comes from the
      ManyBugs benchmark. The possible code modification types are:
     
       - Human patch changes data structures or types?	
       - Human patch changes method signature?	
       - Human patch changes arguments to a function?	
       - Human patch added 1 or more function calls?	
       - Human patch changes conditional?	
       - Human patch adds new variables?	
       - Human patch adds 1 or more if-statements?	
       - Human patch adds 1 or more loops?	
       - Human patch adds a whole new function?

## Additional annotations

1. DefectId
    - Data-type:string
    - Description: The unique defect IDs. For ManyBugs the DefectId is of the format project-buggyHash-fixedhash. 
      For Defects4J, we have separate columns for Project and DefectId provided by Defects4J authors. For ManyBugs the dataset 
      provides DefectIds for both 2015 ManyBugs benchmark containing 185 defects and 2012 ManyBugs benchmark contaning 105 
      defects (strict subset of 185 defects) in seperate columns.
2. IssueReportLink
    - Data-type:string
    - Possible values: url to issue tracker, NA (information not available)
    - Description: the URL to the bug tracking system that describes the bug or feature-request depending upon the defect type. 
      Some defects had multiple URL mappings so we took the one which was reported first. Also, some of the defects map to same 
      URLs indicating that these correspond to individual commits made while resolving the issue.   
3. LinkedToBugTracker
    - Data-type:integer
    - Possible values: 0,1 
    - Description: this contains values 1 and 0 corresponding to whether a defect is linked to any bug tracking system (through
      URL) or not respectively.  
4. DefectType (bug vs feature-request)	
    - Data-type:string
    - Possible values: bug, feature-request 
    - Description: if the defect is a bug report or a feature request. This is determined based on our defined methodology of 
      classifying defects into bugs and feature-requests. 
5. DefectType (defect vs regression)	
    - Data-type:string
    - Possible values: defect, regression
    - Description: if the chronological order of commits corresponding to buggy and fixed versions of the defect is reverse, it 
      is annotated as regression otherwise as defect.
6. \<APR technique\>
   - Data-type:integer
   - Possible values: 0,1, NT (\<APR technique\> was not tested on that defect)
   - Description: this contains 1 or 0 corresponding to whether \<APR technique\> was able to fix the defect (generate a  
     plausible patch) or not respectively. The repairability results are borrowed from previous evaluations. 
7. \<APR technique\> (patch-quality)
   - Data-type:string
   - Possible values: plausible, correct, NT (\<APR technique\> was not tested on that defect)
   - Description: this contains the information about the quality of patches generated by \<APR technique\>. These results are 
     borrowed from evaluation of patches done by other researchers. A patch is plausible if it passes all the negative and 
     positive tests. The criteria considered for correctness depend upon the specific methodology followed by researchers. 
8. (In ManyBugs.csv) SPRCorrect, ProphetCorrect
   - Data-type:integer
   - Possible values: 0,1, NT (SPR/Prophet was not tested on that defect)
   - Description: this contains 1 or 0 corresponding to whether SPR/Prophet was able to fix the defect correctly i.e. if the 
     generated patch is correct patch or not respectively. These repairability results are borrowed from previous evaluation. 


## Scripts

This section describes the scripts (in the scripts/ directory) used to
annotate five defect parameters, FileCount, LineCount, TriggeringTestCount,
RelevantTestCount, and StatementCoverage.

1. defects4j-specific: This directory contains scripts used to annotate Defects4J defects.

   - **get-patch-details.py** annotates FileCount and LineCount. This script
     takes as input all_diffs.csv file from the Defects4J benchmark and
     outputs patch_complexity.csv that includes each defect's ProjectId(PID),
     DefectIf(BID), FILECOUNT, LINECOUNT for all the defects.
   - **get-testcase-details.py** annotates TriggeringTestCount and
     RelevantTestCount. This script requires having Defects4J installed and
     setting the defects4jpath variable (inside script) to the Defects4J
     installation path. The output of this script is Defects4JTests.csv that
     includes each defect's Project, BugID, #Relevant tests, #Triggering
     tests, and #Classes dependent on a given defect. 
   - **get-coverage-details.py** annotates StatementCoverage. This script
     requires having Defects4J installed and setting the defects4jpath
     variable (inside script) to the Defects4j installation path. The output
     of this script is Defects4JCoverage.csv that includes each defect's
     Project, BugID, Lines total, Lines covered, Conditions total, Conditions
     covered, Line Coverage, and Condition coverage for all defects.

2. manybugs-specific - This directory contains scripts used to annotate ManyBugs defects.

   - **get-minimized-patch-complexity.py** annotates FileCount and LineCount,
     without counting the the blank and comment lines in the
     developer-written patches. This script takes as input the ManyBugs
     scenarios available at
     http://repairbenchmarks.cs.umass.edu/ManyBugs/scenarios/. The script
     requires setting the variable repoPath inside the script to point to the
     scenarios. The script outputs ManyBugsPatchComplexity.csv that includes
     each defect's SCENARIO, FILECOUNT, INSERTED, DELETED, MODIFIED,
     LINECOUNT.
   - **get-testcase-details.py** annotates TriggeringTestCount and
     RelevantTestCount. This script takes as input the ManyBugs scenarios
     available at http://repairbenchmarks.cs.umass.edu/ManyBugs/scenarios/.
     The script requires setting the variable repoPath inside the script to
     point to the scenarios. The script outputs ManyBugsTests.csv that
     includes each defect's SCENARIO, POSITIVE_TESTS_COUNT,
     NEGATIVE_TESTS_COUNT, RELEVANT_TESTS_COUNT, and TRIGGERING_TESTS_COUNT.


