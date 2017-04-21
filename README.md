# AutomatedRepairApplicabilityData
## Data and scripts extending the ManyBugs and Defects4J benchmarks for evaluating applicability of automated program repair techniques. 

### Data

ManyBugs and Defects4J benchmarks annotated with:

1. Defect characteristics obtained from various bug tracking systems and information available in benchmarks. 
These defect characteristics can be utilized to evaluate the applicability of automated program repair techniques. 

2. Reparability and patch quality analysis results of 9 automated program repair techniques evaluated on these benchmarks. 

The annonated defects are available in csv files - ManyBugs.csv and Defects4j.csv which correspond to annotations of 
ManyBugs and Defects4J respectively. 

ManyBugs.csv contains:

1. 185 defects of ManyBugs annotated with abstract parameters (described below) utilizing data from different project-specific 
bug tracking systems and ManyBugs benchmark available at http://repairbenchmarks.cs.umass.edu/. 

2. Reparability results and quality analysis results of 6 APR techniques - GenProg, TrpAutoRepair, AE, 
SPR, Prophet, and Kali. (Note: SPR, Prophet and Kali were evaluated on 105-subset of ManyBugs)

Defects4j.csv contains:

1. 224 defects of Defects4J annotated with abstract parameters (described below) utilizing data from different project-specific 
bug tracking systems and Defects4J benchmark available at https://github.com/rjust/defects4j.

2. Reparability results and quality analysis results of 3 APR techniques - GenProg, Kali, and Nopol for 224 defect
subset on which these techniques were evaluated.

### Scripts

Following python scripts are used to annotate parameters related to defect characterictics - *Complexity* and *Test effectivess* 
for which the data is available in benchmarks. These scripts are organized in terms of benchmarks from which they fetch 
data. Thus, we have:

1. defects4j-specific: This directory contains scripts that are used to annotate Defects4J defects.

   - **get-patch-details.py** is used to annotate file count and line count. This script takes as input all_diffs.csv 
     file provided by Defects4J authors and outputs patch_complexity.csv that lists ProjectId(PID), DefectIf(BID), FILECOUNT, 
     LINECOUNT for all the defects. The script can be run by using command: python get-patch-details.py.
   - **get-testcase-details.py** is used to annotate triggering test count and relevant test count. This requires to have 
      Defects4J installed and setting the defects4jpath variable (inside script) Defects4j installation path. The output of 
      this script is Defects4JTests.csv file that lists Project, BugID, #Relevant tests, #Triggering tests and #Classes 
      dependent on a given defect for all defects. This script can be run by using command: python get-testcase-details.py.    
   - **get-coverage-details.py** is used to annotate statement coverage. This script requires Defects4J installed and setting the 
      defects4jpath variable (inside script) Defects4j installation path. The output of this script is  Defects4JCoverage.csv 
      file that lists Project, BugID, Lines total, Lines covered, Conditions total, Conditions covered, Line Coverage, and 
      Condition coverage for all defects. This script can be run by using command: python get-coverage-details.py.

2. manybugs-specific - This directory contains scripts that are used to annotate ManyBugs defects. 

   - **get-minimized-patch-complexity.py** is used to annotate file count and line count by removing the blank and commented 
     lines from the developer-written patches of ManyBugs defects. This script takes as input ManyBugs scenarios available 
     at http://repairbenchmarks.cs.umass.edu/ManyBugs/scenarios/ (set the variable repoPath inside script to point to downloaded 
     scenarios) and it generates as output ManyBugsPatchComplexity.csv file that lists SCENARIO, FILECOUNT, INSERTED, DELETED, 
     MODIFIED, LINECOUNT for all the defects. The script can be run by using command: python get-minimized-patch-complexity.py 
   - **get-testcase-details.py** is used to annotate triggering test count and relevant test count. This script takes as 
     input ManyBugs scenarios available at http://repairbenchmarks.cs.umass.edu/ManyBugs/scenarios/ (set the variable repoPath 
     inside script to point to downloaded scenarios) and it generates as output ManyBugsTests.csv file that lists SCENARIO, 
     POSITIVE_TESTS_COUNT, NEGATIVE_TESTS_COUNT, RELEVANT_TESTS_COUNT, and TRIGGERING_TESTS_COUNT for all the ManyBugs defects. 
     The script can be run by using command: python get-testcase-details.py 
   
### Abstract parameters

Following is the list describing abstract parameters which the defects are annotated with. 

1. FileCount
   - Data-type:integer
   - Possible values: >=1 
   - Description: the number of files containing non-comment non-blank-line edits in the developer-written fix.
2. LineCount
   - Data-type:integer
   - Possible values: >=1 
   - Description: the total number of non-comment non-blank lines of code in the developer-written fix.
3. RelevantTestCount	
   - Data-type:integer
   - Possible values: >=1 
   - Description: number of test cases that execute at least one statement in at least one file edited by the developer-written patch.
4. TriggeringTestCount	
   - Data-type:integer
   - Possible values: >=1 
   - Description: number of defect triggering test cases
5. StatementCoverage	
   - Data-type:double
   - Possible values: >=0 and <=100 
   - Description: the percentage of the lines in the files edited by the developer-written patches that are executed by the test suite
6. TimeToFix	
   - Data-type:double
   - Possible values: >0 
   - Description: the amount of time (days) taken by developer to fix a defect. This is computed as the time difference between when the 
     issue was reported and when the issue was resolved. Depending on the bug tracking system, different concrete parameters are used to 
     obtain these two timestamps.
7. Versions	
   - Data-type:integer
   - Possible values: >=1 
   - Description: effect of defect on different versions of a project or other project modules and components.
8. Priority	
   - Data-type:integer
   - Possible values: 1,2,3,4,5 
   - Description: importance of fixing a defect in terms of defect priority. This is obtained using priority assigned to the defect. 
     Different bug tracking systems use different values to denote low, normal, high, critical, blocker defects. We use a scale of 
     1 to 5 corresponding to these priority values (1 is the lowest priority and 5 is the highest) and map the values used by bug tracking
     systems to our scale.
9. Dependents	
   - Data-type:integer
   - Possible values: >=1 
   - Description: number of defects (also with URLs to bug tracking systems) on which the fixing of a given defect depends.
10. PatchCharacteristics: 
   - Data-type:integer
   - Possible values: 0,1 
   - Description: characteristics of the developer-written patch in terms of the type of code modifications done to fix the defect. The defects
     are annotated corresponding to following nine patch characterictics borrowed from the information about bug type available within the 
     ManyBugs metadata. For each characteristic a defect is annotated with value 0 or 1 depending upon the edits involved in developer-written fix.  
       - Human patch changes data structures or types?	
       - Human patch changes method signature?	
       - Human patch changes arguments to a function?	
       - Human patch added 1 or more function calls?	
       - Human patch changes conditional?	
       - Human patch adds new variables?	
       - Human patch adds 1 or more if-statements?	
       - Human patch adds 1 or more loops?	
       - Human patch adds a whole new function?

Additional annotations

11. DefectType (bug vs feature-request)	
   - Data-type:string
   - Possible values: bug, feature-request 
   - Description: if the defect is a bug report or a feature request. This is determined based on our defined methodology of classifying defects into 
     bugs and feature-requests. 
12. DefectType (defect vs regression)	
   - Data-type:string
   - Possible values: defect, regression
   - Description: if the choronological order of commits corresponding to buggy and fixed versions of the defect is reverse, it is annotated as regression
     otherwise as defect. 
13. IssueReportLink
   - Data-type:string
   - Possible values: url to issue tracker 
   - Description: the URL to the bug tracking system that decribes the bug or feature-request depening upon the defect type. Some defects had multiple URL
     mappings so we took the one which was reported first. Also, some of the defects map to same URLs indicating that these correspond to individual commits
     made while resolving the issue.   
14. LinkedToBugTracker
   - Data-type:integer
   - Possible values: 0,1 
   - Description: this containes values 1 and 0 corresponding to whether a defect is linked to any bug tracking system (through URL) or not respectively.  
