# 2022S1RSRCommissioning

Mostly for linechecks now.

The following RSR projects were done in this session:L

       ProjectId     <ObsNum  mode    object

 	2021-S1-MX-26    100441  RSR     PG.../IRAS...   ?
	2021-S1-US-17    100101  RSR     J1557+1540      ?
	2021-S1-US-19    100474  RSR     Cyg_X-1         ?
	2021-S1-MX-34    100394  RSR     NGP*            ?
	2021-S1-UM-11    100334  RSR     J*.*            MinY

# sources

The command

      lmtinfo.py grep 2022 LineCheck Bs | awk '{print $5}' | sort | uniq -c

should give

      2 1051+213
      1 1146+399
      3 3c279
     21 I10565
     12 I12112
     16 I17208
      2 I23365
      1 ObsNum
      2 bllac
      8 mwc349a

