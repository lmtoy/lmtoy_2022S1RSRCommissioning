#! /usr/bin/env python
#
#   script generator for project=
#
#   lmtinfo.py grep LineCheck Bs

import os
import sys

#  2022S1RSRCommissioning  2018S1RSRCommissioning 2018ARSRCommissioning
#  2014ARSRCommissioning   2015ARSRCommissioning  2016ARSRCommissioning
project="linecheck"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['I10565'] = [94687, 94688,
                95132, 95186, 95187, 95234, 95235, 98306, 98307,
                98557, 98558,
                99815, 99816, 99820, 99821, 99846, 99847, 99947, 99948, 100384, 100385]

# historic 50m data pre-pandemic (2018, 2020) - jan 2018 50m was installed
on['I10565h50'] = [71588, 71589, 71590, 71605, 71606, 71610, 71611, 74021, 74022, 74051, 74052,        # 2018A   2018-02-10 to 2018-03-24
                   76707, 76708, 76829, 76830, 76988, 76989, 76991, 76992, 77008, 77009,               # 2018S1  2018-05-18 to 2018-06-09
                   77113, 77114, 77420, 77421, 
                   92057, 92060, 92061, 92062, 92064, 92065, 92067, 92068]                             # 2018S1  2020-03-05 

# historic 32m data
on['I10565h32'] = [28190 , 28191 , 29674 , 29675 , 31349 , 31350 , 31524 , 31525 , 31528 , 31529 ,
                   31532 , 31533 , 32018 , 32019 , 32876 , 32877 , 32992 , 32993 , 33392 , 33393 ,
                   33543 , 33544 , 33546 , 33547 , 33551 , 33552 , 33848 , 33849 , 33905 , 33906 ,
                   34431 , 34432 , 34788 , 34789 , 35691 , 35692 , 36445 , 36446 , 36949 , 36950 ,
                   38494 , 38495 , 38624 , 38625 , 38776 , 38777 , 39593 , 39594 , 39677 , 39678 ,
                   39682 , 39683 , 39686 , 39687 , 40134 , 40135 , 40286 , 40287 , 40605 , 40606 ,
                   40608 , 40609 , 40797 , 40798 , 41194 , 41195 , 41197 , 41198 , 42166 , 42167 ,
                   42303 , 42304 , 42313 , 42314 , 42318 , 42319 , 42864 , 42865 , 49515 , 49516 ,
                   52195 , 52196 , 54693 , 54694 , 54802 , 54803 , 55514 , 55515 , 55770 , 55771 ,
                   55784 , 55785 , 57632 , 57633 , 58383 , 58384 , 58392 , 58393 , 58448 , 58449 ,
                   58452 , 58618 , 58619 , 58620 , 58731 , 58732 , 58829 , 58830 , 58842 , 58843 ,
                   58866 , 58867 , 58962 , 58963 , 59035 , 59036 , 59112 , 59113 , 59122 , 59123 ,
                   59257 , 59258 , 59359 , 59360 , 59399 , 59400 , 59470 , 59471 , 59951 , 59952 ,
                   60125 , 60126 , 60977 , 60978 , 61087 , 61088 , 61218 , 61219 , 61352 , 61353 ,
                   61507 , 61508 , 61510 , 61511 , 61513 , 61514 , 61581 , 61582 , 61696 , 61697 ,
                   61827 , 61828 , 61978 , 61979 , 66008 , 66009 , 66175 , 66176 , 66236 , 66237 ,
                   66382 , 66383 , 66894 , 66895 , 66965 , 66966 , 67130 , 67131 , 67178 , 67179 ,
                   67310 , 67311 , 67312 , 67412 , 67413 , 67438 , 67439 , 67441 , 67442 , 67641 ,
                   67642 , 67772 , 67773 , 67899 , 67900 , 67964 , 67965 , 67968 , 67969 , 68397 ,
                   68398 , 68408 , 68409 , 68476 , 68477 , 68553 , 68554 , 68632 , 68633]

on['I12112'] = [94993, 94994, 95302, 95303,
                98184, 98185, 98299, 98300, 98302, 98303,              
                98422, 98423]

on['I12112h50'] = [71635, 71636, 72977, 72978, 73749, 73750, 73939, 73940, 75152, 75153,               # 2018A
                   76288, 76289, 76579, 76580, 76712, 76713, 76879, 76880, 77013, 77014, 77118, 77119, # 2018S1
                   92071, 92072, 92074, 92075, 92077, 92078, 92080, 92081, 92083, 92084, 92086, 92087] # taken in 2020


on['I17208'] = [95306, 95307, 95524, 95525, 98594, 98595, 98649, 98650]

on['I17208h50'] = [76304, 76305, 76307, 76308, 76310, 76311, 77439, 77440, 78136, 78137]               # 2018S1 (none in 2018A)

#  doesn't seem to work too well
#on['mwc349a'] = [98534, 98535, 100114, 100114, 101103, 101104, 101106, 101107]


#       common parameters per source on the first dryrun (run1, run2)
pars1 = {}

pars1['I10565']     = "xlines=110.51,0.15,108.65,0.3,85.2,0.4"
pars1['I10565h50']  = "xlines=110.51,0.15,108.65,0.3,85.2,0.4"
pars1['I10565h32']  = "xlines=110.51,0.15,108.65,0.3,85.2,0.4"
pars1['I12112']     = "xlines=107.40,0.25"
pars1['I12112h50']  = "xlines=107.40,0.25"
pars1['I17208']     = "xlines=110.50,0.20,108.8,0.3"
pars1['I17208h50']  = "xlines=110.50,0.20"

#        common parameters per source on subsequent runs (run1a, run2a)
pars2 = {}
pars2['I10565']     = ""
pars2['I10565h50']  = ""
pars2['I10565h32']  = ""
pars2['I12112']     = ""
pars2['I12112h50']  = ""
pars2['I17208']     = ""
pars2['I17208h50']  = ""


# below here no need to change code
# ========================================================================

#        helper function for populating obsnum dependant argument -- deprecated
def getargs3(obsnum):
    """ search for <obsnum>.args
    """
    f = "%d.args" % obsnum
    if os.path.exists(f):
        lines = open(f).readlines()
        args = ""
        for line in lines:
            if line[0] == '#': continue
            args = args + line.strip() + " "
        return args
    else:
        return ""

#        specific parameters per obsnum will be in files <obsnum>.args -- deprecated
pars3 = {}
for s in on.keys():
    for o1 in on[s]:
        o = abs(o1)
        pars3[o] = getargs3(o)

#        obsnum.args is alternative single file pars file to set individual parameters
pars4 = {}
if os.path.exists("obsnum.args"):
    lines = open("obsnum.args").readlines()
    for line in lines:
        if line[0] == '#': continue
        w = line.split()
        pars4[int(w[0])] = w[1:]
        print('PJT',w[0],w[1:])

def getargs(obsnum):
    """ search for <obsnum> in obsnum.args
    """
    args = ""
    if obsnum in pars4.keys():
        print("PJT2:",obsnum,pars4[obsnum])
        for a in pars4[obsnum]:
            args = args + " " + a
    return args

run1  = '%s.run1'  % project
run1a = '%s.run1a' % project
run1b = '%s.run1b' % project
run2  = '%s.run2' % project
run2a = '%s.run2a' % project

fp1 = open(run1,  "w")
fp2 = open(run1a, "w")
fp3 = open(run1b, "w")

fp4 = open(run2,  "w")
fp5 = open(run2a, "w")

#                           single obsnum
n1 = 0
for s in on.keys():
    for o1 in on[s]:
        o = abs(o1)
        cmd1 = "SLpipeline.sh obsnum=%d _s=%s %s admit=0 restart=1 %s %s" % (o,s,pars1[s], pars2[s], getargs(o))
        cmd2 = "SLpipeline.sh obsnum=%d _s=%s %s admit=0 restart=1" % (o,s,pars1[s])
        cmd3 = "SLpipeline.sh obsnum=%d _s=%s %s admit=0 %s" % (o,s,pars2[s], getargs(o))
        fp1.write("%s\n" % cmd1)
        fp2.write("%s\n" % cmd2)
        fp3.write("%s\n" % cmd3)
        n1 = n1 + 1

#                           combination obsnums
n2 = 0        
for s in on.keys():
    obsnums = ""
    n3 = 0
    for o1 in on[s]:
        o = abs(o1)
        if o1 < 0: continue
        n3 = n3 + 1
        if obsnums == "":
            obsnums = "%d" % o
        else:
            obsnums = obsnums + ",%d" % o
    print('%s[%d/%d] :' % (s,n3,len(on[s])), obsnums)
    cmd4 = "SLpipeline.sh _s=%s admit=0 restart=1 obsnums=%s" % (s, obsnums)
    cmd5 = "SLpipeline.sh _s=%s admit=1 srdp=1  obsnums=%s" % (s, obsnums)
    fp4.write("%s\n" % cmd4)
    fp5.write("%s\n" % cmd5)
    n2 = n2 + 1

print("A proper re-run of %s should be in the following order:" % project)
print(run1a)
print(run2)
print(run1b)
print(run2a)
print("Where there are %d single obsnum runs, and %d combination obsnums" % (n1,n2))

