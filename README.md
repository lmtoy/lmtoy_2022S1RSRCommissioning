# 2022S1RSRCommissioning

This is mostly for linechecks now, but also includes historic data from 2018 (50m), 
and 2014,2015,2016 (32m). In January 2018 the 50m dish was installed, and initial
commissioning took place. The first LineCheck data in the 50m were taken 
on 2018-02-10 (obsnum=71588)

The following RSR projects were done in this 2022 session:

       ProjectId     <ObsNum  mode    object

 	2021-S1-MX-26    100441  RSR     PG.../IRAS...   Longinotti
	2021-S1-US-17    100101  RSR     J1557+1540      Jiangtao
	2021-S1-US-19    100474  RSR     Cyg_X-1         ?  (continuum)
	2021-S1-MX-34    100394  RSR     NGP*            Alfredo
	2021-S1-UM-11    100334  RSR     J*.*            MinYun

# sources

The command

      lmtinfo.py grep 2022 LineCheck Bs | awk '{print $5}' | sort | uniq -c

should give something like this

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

According to http://wiki.lmtgtm.org/lmtwiki/RSR%20Spectral%20Line%20Check?action=AttachFile&do=view&target=LineCheckSources.pdf
the fluxes of the sources we cover here are (for 32m dish)

      I10565      68 mK
      I17208      60 mK
      I23365      16 mK


# How to run

Normally the command
     
     ./mk_runs.py
	 
generates the text file for slurm, but currently RSR cannot run in parallel. But when it does,
this will be the command

      slurm_lmtoy.sh linecheck.run1

to run *everything* (historic data too).  And

      slurm_lmtoy.sh linecheck.run2
	  
to run the combinations.


## Historic data

This script generator also has the historic (2018 in 50m, an 2014,15,16 with a 32m dish) added, but adding 'h50' or 'h32' to the source name.
See also http://wiki.lmtgtm.org/lmtwiki/RSR%20Spectral%20Line%20Check and 
http://wiki.lmtgtm.org/lmtwiki/RSR%20Spectral%20Line%20Check?action=AttachFile&do=view&target=LineCheckSources.pdf


# Example Session: Historic 50m data

Typically if you start with a new project, you first make the project directory, in this case

      cd $WORK_LMT
	  mkdir 2022S1RSRCommissioning
	  cd 2022S1RSRCommissioning
	 
then you grab the script generator infrastructure

      git clone https://github.com/teuben/lmtoy_2022S1RSRCommissioning
	  cd lmtoy_2022S1RSRCommissioning
	  
from which you control the pipeline.   You first create the run scripts

	  make runs
	  
This project is a bit peculiar in that it handles 3 sources (I10565, I17208, and I12112) 
over more than that single ProjectID 2022S1RSRCommissioning, there are 5 other historic ones! The
data from those other projects will be rooted in another ProjectId, e.g.
$WORK_LMT/2018S1RSRCommissioning and the oldest one $WORK_LMT/2014ARSRCommissioning.

If you want to run the whole data from 2014-2022, you would do 

	  sbatch_lmtoy.sh linecheck.run1

but these are currently 317 obsnums, so will take a while for this example.
Better is to focus on 
for example the historic 50m data for one source.
For convenience we've labeled historic 50m and 32m data by appending "h50" and "h32" to
the source name. So, to test the historic 50m data for I10565 we do:


      grep I10565h50 linecheck.run1 > test1
      grep I10565h50 linecheck.run2 > test2
	  
where you will see 33 obsnums in test1, and just a single combination of those 33 in test2.
These files are now ready for slurm:

	  sbatch_lmtoy.sh test1
 
This should take about 5 mins, but you keep checking with the 
squeue command until all 33 jobs are done with this neat refresher (control-C to exit)

      watch -n3 squeue -u lmthelpdesk_umass_edu

When all is done, issue the run script to combine those 33 obsnums

      sbatch_lmtoy.sh test2
	  watch -n3 squeue -u lmthelpdesk_umass_edu
	  
Before you can view them, we need to distribute the comments.txt file to the pipeline directory, so 
the summary can include them. And then we make the summary:

      make comments
	  make summary
	  
after which you can view the pipeline summary here

* http://taps.lmtgtm.org/lmtslr/2018ARSRCommissioning/     covering obsnums 71588 - 74052, as well as the combination  71588_92068
* http://taps.lmtgtm.org/lmtslr/2018S1RSRCommissioning/    covering obsnums 76707 - 92068

 
Again, because of the unusual spread accross projects, you need to view this example in different web trees.

Once you run the other ones, you can view them in their respective summary URLs:

* http://taps.lmtgtm.org/lmtslr/2014ARSRCommissioning/   (32m)
* http://taps.lmtgtm.org/lmtslr/2015ARSRCommissioning/   (32m)
* http://taps.lmtgtm.org/lmtslr/2016ARSRCommissioning/   (32m)
* http://taps.lmtgtm.org/lmtslr/2022S1SRCommissioning/   new 2022 data


For the helpdesk accounts, the root directory would be something like

* http://taps.lmtgtm.org/lmthelpdesk/peter/2018ARSRCommissioning
