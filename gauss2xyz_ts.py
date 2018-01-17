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

# delete suffix
filename = filename[:-4]

# in and out files
fin=str(filename) + ".log"
fout=str(filename) + "_preopt.com"

#numPreOpt = numFG[filename.split('_')[3]]
#print numPreOpt

print fin, fout
xyz         = []

# loop through file to get number of atoms and xyz coordinates
f = open(fin)
for line in f:
    # number of atoms
    if 'NAtoms=' in line:
        nAtoms=int(line.split()[1])
    # end of optimization
    if '-- Stationary point found' in line:
        # search beginning of coordinates
        for line in f:
            if 'Standard orientation:' in line:
                coords=''.join(islice(f, nAtoms+4))

                # store coordinates
                for i in range(4,nAtoms+4):
                    line= PSE[coords.split('\n')[i].split()[1]],\
                        coords.split('\n')[i].split()[3],\
                        coords.split('\n')[i].split()[4],\
                        coords.split('\n')[i].split()[5]
                    xyz.append(line)

f.close()

# write to file
target = open(fout, 'w')
target.write(str(nAtoms) + "\n")
for i in range(nAtoms):
    line='\t'.join(xyz[i])
    target.write(str(line) + "\n")
target.close()
