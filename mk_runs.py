#! /usr/bin/env python
#
#   script generator for project=
#
#   lmtinfo.py grep LineCheck Bs

import os
import sys

#  2022S1RSRCommissioning  2018S1RSRCommissioning 2018ARSRCommissioning
project="linecheck"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['I10565'] = [94687, 94688,
                95132, 95186, 95187, 95234, 95235, 98306, 98307,
                98557, 98558,
                99815, 99816, 99820, 99821, 99846, 99847, 99947, 99948, 100384, 100385]
# 92068
on['I10565a'] = [71588, 71589, 71590, 71605, 71606, 71610, 71611, 74021, 74022, 74051, 74052,        # 2018A
                 76707, 76708, 76829, 76830, 76988, 76989, 76991, 76992, 77008, 77009,               # 2018S1
                 77113, 77114, 77420, 77421, 
                 92057, 92060, 92061, 92062, 92064, 92065, 92067, 92068]                             # taken in 2020

on['I12112'] = [94993, 94994, 95302, 95303,
                98184, 98185, 98299, 98300, 98302, 98303,              
                98422, 98423]

on['I12112a'] = [71635, 71636, 72977, 72978, 73749, 73750, 73939, 73940, 75152, 75153,               # 2018A
                 76288, 76289, 76579, 76580, 76712, 76713, 76879, 76880, 77013, 77014, 77118, 77119, # 2018S1
                 92071, 92072, 92074, 92075, 92077, 92078, 92080, 92081, 92083, 92084, 92086, 92087] # taken in 2020


on['I17208'] = [95306, 95307, 95524, 95525, 98594, 98595, 98649, 98650]

on['I17208a'] = [76304, 76305, 76307, 76308, 76310, 76311, 77439, 77440, 78136, 78137]               # 2018S1 (none in 2018A)

#  doesn't seem to work too well
#on['mwc349a'] = [98534, 98535, 100114, 100114, 101103, 101104, 101106, 101107]


#       common parameters per source on the first dryrun (run1, run2)
pars1 = {}

pars1['I10565']   = "xlines=110.51,0.15,108.65,0.3,85.2,0.4"
pars1['I10565a']  = "xlines=110.51,0.15,108.65,0.3,85.2,0.4"
pars1['I12112']   = "xlines=107.40,0.25"
pars1['I12112a']  = "xlines=107.40,0.25"
pars1['I17208']   = "xlines=110.50,0.20,108.8,0.3"
pars1['I17208a']  = "xlines=110.50,0.20"

#        common parameters per source on subsequent runs (run1a, run2a)
pars2 = {}
pars2['I10565']   = ""
pars2['I10565a']  = ""
pars2['I12112']   = ""
pars2['I12112a']  = ""
pars2['I17208']   = ""
pars2['I17208a']  = ""


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

