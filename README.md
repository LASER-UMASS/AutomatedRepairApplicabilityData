# Automated repair applicability data 

This project contains data and scripts that extend the
[ManyBugs](http://repairbenchmarks.cs.umass.edu/) version beta-2.1 and
[Defects4J](https://github.com/rjust/defects4j) version 1.1.0 benchmarks to enable the
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


### Primary key parameters 
Following two parameters are used to uniquely identify each defect.  

1. Project
    - Data-type:string
    - Description: the name of the project.
2. DefectId (or DeprecatedDefectId for ManyBugs)
    - Data-type:string
    - Description: For Defects4J, the DefectId lists the bug number for each defect as provided in Defects4J benchmark. For ManyBugs, the DefectId lists the buggycommitHash-fixedcommithash for each defect as provided in ManyBugs benchmark. The dataset provides DefectIds for both 2015 ManyBugs benchmark containing 185 defects and 2012 ManyBugs benchmark contaning 105 defects (strict subset of 185 defects) under columns DefectId and DeprecatedDefectId respectively.

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
   - Description: the percent of the lines in the files edited by the developer-written patch that are executed by the test suite. We computed the coverage of Defects4J defects utilizing the `coverage` utility provided in Defects4J framwork available with Defects4J benchmark. For ManyBugs defects, we used the virtual machine image (genprog_icse2012_virtualbox) available with ManyBugs benchmark to manually download and compile each defect and then used `gcov` utlity to compute the test suite coverage.    
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
   - Possible values: 0, 0.5, 1, and NA (information not available)
   - Description: how easy it is to reproduce the defect by developer (0 indicates defect is nondeterministic, 0.5 indicates defect is reproducible sometimes but not always, and 1 indicates defect is reproducible).
11. PatchCharacteristics
    - Data-type:binary
    - Possible values: 0,1 
    - Description: characteristics of the developer-written patch in terms of
      the type of code modifications. This information comes from both benchmarks, but the characteristics (mentioned in quotes)
      are adopted from the ManyBugs benchmark. The possible code modification types are:
     
       - *ChangesType*: patch changes one or more data structure or data type. ("Human patch changes data structures or types?")	
       - *ChangesMethodSignature*: patch changes method signature of one or more methods. ("Human patch changes method signature?")	
       - *ChangesMethodCallArgs*: patch changes one or more arguments of one or more methods. ("Human patch changes arguments to a function?")	
       - *AddsMethodCall*: patch adds one or more method calls. ("Human patch added 1 or more function calls?")	
       - *ChangesCondition*: patch changes one or more conditional statements. ("Human patch changes conditional?")	
       - *AddsVariable*: patch adds one or more variables. ("Human patch adds new variables?")	
       - *AddsIfStmt*: patch adds one or more if-statements. ("Human patch adds 1 or more if-statements?")	
       - *AddsLoop*: patch adds one or more loops. ("Human patch adds 1 or more loops?")	
       - *AddsMethod*: patch adds one or more methods. ("Human patch adds a whole new function?")
       
## Additional annotations

1. IssueReportLink
    - Data-type:string
    - Possible values: url to issue tracker, NA (information not available)
    - Description: the URL to the bug tracking system that describes the bug or feature-request depending upon the defect type. 
      Some defects had multiple URL mappings so we took the one which was reported first. Also, some of the defects map to same 
      URLs indicating that these correspond to individual commits made while resolving the issue.    
2. BugOrFeature
    - Data-type:string
    - Possible values: bug, feature 
    - Description: if the defect is a bug or feature. This is determined based on our defined methodology of 
      classifying defects into bugs and features. 
3. IsRegression	
    - Data-type:binary
    - Possible values: 0,1 
    - Description: if the chronological order of commits corresponding to buggy and fixed versions of the defect is reverse, it 
      is annotated with 1 (defect is regression) otherwise it is annotated with value 0 (defect is not regression).
4. PatchFound:\<APR technique\>
   - Data-type:binary
   - Possible values: 0,1, NA (\<APR technique\> was not tested on that defect)
   - Description: this contains 1 or 0 corresponding to whether \<APR technique\> was able to fix the defect (generate a  
     plausible patch) or not respectively. The repairability results are borrowed from previous evaluations. 
5. PatchQuality:\<APR technique\>
   - Data-type:string
   - Possible values: plausible, correct, NA (\<APR technique\> was not tested on that defect or <APR technique\> was not 
     able to generate a patch for that defect).
   - Description: this contains the information about the quality of patches generated by \<APR technique\>. We borrow this data   from the prior work done on evaluating these patches (refer [1] and [2]). A patch is plausible (or incorrect) if it passes all the relevant tests. The correctness of a patch is based on the specific methodology followed by the researchers in [1] and [2]. 

## Scripts

This section describes the scripts (in the scripts/ directory) used to
annotate five defect parameters, FileCount, LineCount, TriggeringTestCount,
RelevantTestCount, and StatementCoverage. Remaining parameters were obtained
by manually analysing the bug tracking systems. 

1. defects4j-specific: This directory contains scripts used to annotate Defects4J defects.

   - **getPatchComplexity.py** annotates FileCount and LineCount. This script
     takes as input all_diffs.csv file from the Defects4J benchmark and
     outputs file Defects4JPatchComplexity.csv that lists Project, DefectId, FileCount, and LineCount for all the defects.
   - **getTestcaseDetails.sh** annotates TriggeringTestCount and
     RelevantTestCount. This script requires having Defects4J installed and
     setting the environment variable PATH to \<path-to-Defects4J installation\>/framewor/bin. The input to the script required 
     is project, start  DefectId and end DefectId (e.g. Chart 1 26). The output generated by the script is file
     Defects4JTestCounts.csv  that lists Project, DefectId, RelevantTestCount, and TriggeringTestCount for all the defects. 
   - **getCoverageDetails.py** annotates StatementCoverage. This script
     requires having Defects4J installed and providing the defects4j installation path
     as command line argument for execution. The output generated by the 
     script is file Defects4JCoverage.csv that lists Project, DefectId and, StatementCoverage for all the defects.

2. manybugs-specific - This directory contains scripts used to annotate ManyBugs defects.

   - **getPatchComplexity.py** annotates FileCount and LineCount, without counting the the blank and comment lines in the
     developer-written patches. This script requires ManyBugs scenarios downloaded from
     http://repairbenchmarks.cs.umass.edu/ManyBugs/scenarios/. The script requires specifying the path to ManyBugs scenarios as 
     command-line argument. The output generated by the script is file ManyBugsPatchComplexity.csv that lists
     Project, DefectId, FileCount, and LineCount for all the 185 ManyBugs defects.
   - **getTestcaseDetails.py** annotates TriggeringTestCount and RelevantTestCount. This script takes as input the ManyBugs 
     scenarios available at http://repairbenchmarks.cs.umass.edu/ManyBugs/scenarios/. The output generated by the script is file 
     ManyBugsTestCounts.csv that lists Project, DefectId, PositiveTestCount, NegativeTestCount, RelevantTestCount, and 
     TriggeringTestCount.

##### References:

1. Long, F., Rinard, M.: Automatic patch generation by learning correct code. In: ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages (POPL), pp. 298–312. St. Petersburg, FL, USA (2016). DOI 10.1145/2837614.2837617
2. Martinez, M., Durieux, T., Sommerard, R., Xuan, J., Monperrus, M.: Automatic repair of real bugs in Java: A large-scale experiment on the Defects4J dataset. Empirical Software Engineering (EMSE) (2016)
