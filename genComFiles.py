#!/usr/bin/env python
import glob
import os
import sys
from itertools import islice
from subprocess import call

# dic to convert atomic numbers to atomic labels
PSE={'1':"H",'6':"C",'7':"N",'8':"O",'9':"F",'15':"P",'16':"S",'17':"Cl",'35':"Br",'46':"Pd"}
numFG={'cn':2,'nh2':3,'cl':1,'f':1,'br':1,'coh':3,'cooh':4,'ch3':4,'cbr3':4,'cf3':4,'ccl3':4,'cocbr3':6,'coccl3':6,'cocf3':6,'ph':11,'oh':2}

# .log file
filename = sys.argv[1]
filename = filename[:-4]

# in and out files
fin=str(filename) + ".xyz"
fout=str(filename) + "_preopt.com"

numPreOpt = numFG[filename.split('_')[3]]

print fin, fout
xyz         = []

# loop through file to get number of atoms and xyz coordinates
f = open(fin)
for i,line in enumerate(f):
    if (i == 0):
        nAtoms=int(line)
    if (i == 2):
        for line in f:
            xyz.append(line)

f.close()

# write to file
target = open(fout, 'w')
#target.write(str(nAtoms) + "\n" + numPreOpt +"\n")
target.write("%Chk=preopt.chk\n%nprocshared=8\n%mem=2GB\n#n b3lyp 6-31g* opt=(calcall,noeigentest,readoptimize)\n\n titel\n\n0 1\n")
for coord in xyz:
    target.write(coord)
target.write("\nnoatoms atoms=" + str(nAtoms-numPreOpt+1) + "-" + str(nAtoms))
target.close()
