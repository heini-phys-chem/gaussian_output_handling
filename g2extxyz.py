#!/usr/bin/env python
import glob
import os
import sys
from itertools import islice
from subprocess import call

PSE={'1':"H",'6':"C",'7':"N",'8':"O",'9':"F",'15':"P",'16':"S",'17':"Cl",'35':"Br",'46':"Pd"}

files = open("out.lst","r")
for line in files:
    line = line[:-5]

    fin=str(line) + ".out"
    fout=str(line) + ".xyz"

    print fin, fout

    xyz = []

    # loop through file to get number of atoms, energy and xyz coordinates
    with open(fin) as input_file:
        for i, line in enumerate(input_file):
            #if 'SCF Done' in line:
            #    E=line.split()[4]
            if 'NAtoms=' in line and 'NActive=' not in line:
                nAtoms=int(line.split()[1])
            if ' Standard orientation:' in line:
                coords=''.join(islice(input_file, nAtoms+4))

                for i in range(4,nAtoms+4):
                    line= PSE[coords.split('\n')[i].split()[1]], coords.split('\n')[i].split()[3], coords.split('\n')[i].split()[4], coords.split('\n')[i].split()[5]
                    xyz.append(line)

    #print xyz 

    # write to file
    target = open("../xyz/" + fout, 'w')
    target.write(str(nAtoms))
    target.write('\n')
    target.write('\n')

    for i in range(nAtoms):
        line='\t'.join(xyz[i])
        target.write(str(line))
        target.write('\n')
    target.close()

