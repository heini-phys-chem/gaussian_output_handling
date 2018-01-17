#!/usr/bin/env python
import os
import sys
import random
import numpy as np
from itertools import islice


class atom(object):
    def __init__(self, label, x, y, z):
        self.label  = label
        self.x      = x
        self.y      = y
        self.z      = z

class molecule(object):
    def __init__(self, fout, SCF):
        self.atom_list = []
        self.fout = fout
        self.SCF = SCF

    def get_natom(self):
        return len(self.atom_list)

    def add_atom(self, atom):
        self.atom_list.append(atom)

    def print_geom(self):
        print str(self.get_natom()) + "\n"
        for i in self.atom_list:
            print str(i.label) + "\t" + str(i.x) + "\t" + str(i.y) + "\t" + str(i.z)

    def write_geom(self):
        f = open(self.fout,'w')
        f.write(str(self.get_natom()) + "\n" + str(self.SCF) + "\n")
        for i in self.atom_list:
            f.write(str(i.label) + "\t" + str(i.x) + "\t" + str(i.y) + "\t" + str(i.z) + "\n")
        f.close()

    def return_geom(self):
        return [str(i.label) + "\t" + str(i.x) + "\t" + str(i.y) + "\t" + str(i.z) for i in self.atom_list]

    def return_distorted_geom(self):
        return [str(i.label) + "\t" + str(float(i.x) + np.random.normal(0.0,0.1)) + "\t" + str(float(i.y) + np.random.normal(0.0,0.1)) + "\t" + str(float(i.z) + np.random.normal(0.0,0.1)) for i in self.atom_list]

def print_list(lst):
    for i, p  in enumerate(lst):
        f = open("distorted/dis_" + str(i) + ".xyz", "w")
        f.write("14\n\n")
        for q in p: f.write(q + "\n")
        f.close()

PSE={'1':"H",'6':"C",'7':"N",'8':"O",'9':"F",'15':"P",'16':"S",'17':"Cl",'35':"Br",'46':"Pd",'28':"Ni",'78':"Pt",'29':"Cu",'47':"Ag",'79':"Au"}

fileName = sys.argv[1]
list_of_mols = []

f = open(fileName)

fin=str(fileName[:-4]) + ".log"
fout=str(fileName[:-4]) + ".xyz"
fout = fout[fout.rindex('/')+1:]

molecule_list = []

with open(fin) as input_file:
    for i, line in enumerate(input_file):
        if 'NAtoms=' in line:
            nAtoms = int(line.split()[1])
        if 'SCF Done:' in line:
            SCF = float(line.split()[4])
        if 'Stationary point found' in line:
            for i, line in enumerate(input_file):
                if 'Standard orientation:' in line:
                    one_mol = molecule(fout,SCF)

                    coords=''.join(islice(input_file, nAtoms+4))

                    for i in range(4,nAtoms+4):
                        one_atom = atom(PSE[coords.split('\n')[i].split()[1]], coords.split('\n')[i].split()[3], coords.split('\n')[i].split()[4], coords.split('\n')[i].split()[5])
                        one_mol.add_atom(one_atom)

                    one_mol.write_geom()


f.close()
