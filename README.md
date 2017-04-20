# AutomatedRepairApplicabilityData
## Data and scripts extending the ManyBugs and Defects4J benchmarks for evaluating applicability of automated program repair techniques.

### Data

ManyBugs and Defects4J benchmarks annotated with:

1. Defect characteristics obtained from various bug tracking systems and information available in benchmarks.
These defect characteristics can be utilized to evaluate the applicability of automated program repair techniques.

2. Repairability and patch quality analysis results of 9 automated program repair techniques evaluated on these benchmarks.

The annotated defects are available in csv files - ManyBugs.csv and Defects4j.csv which correspond to annotations of
ManyBugs and Defects4J respectively.

ManyBugs.csv contains:

1. 185 defects of ManyBugs annotated with abstract parameters utilizing data from different project-specific
bug tracking systems and ManyBugs benchmark available at http://repairbenchmarks.cs.umass.edu/.

2. Repairability results and quality analysis results of 6 APR techniques - GenProg, TrpAutoRepair, AE,
SPR, Prophet, and Kali. (Note: SPR, Prophet and Kali were evaluated on 105-subset of ManyBugs)

Defects4j.csv contains:

1. 357 defects of Defects4J annotated with abstract parameters utilizing data from different project-specific
bug tracking systems and Defects4J benchmark available at https://github.com/rjust/defects4j.

2. Repairability results and quality analysis results of 3 APR techniques - GenProg, Kali, and Nopol for 224 defect
subset on which these techniques were evaluated.

### Scripts

Following python scripts are used to annotate parameters related to defect characteristics - *Complexity* and *Test effectivess*
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


