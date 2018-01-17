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
    def __init__(self):
        self.atom_list = []

    def get_natom(self):
        return len(self.atom_list)

    def add_atom(self, atom):
        self.atom_list.append(atom)

    def print_geom(self):
        print str(self.get_natom()) + "\n"
        for i in self.atom_list:
            print str(i.label) + "\t" + str(i.x) + "\t" + str(i.y) + "\t" + str(i.z)

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

def get_nAtoms(fxyz):
    with open(fxyz) as f:
        return f.readline()


if __name_ = "__main__":
    PSE={'1':"H",'6':"C",'7':"N",'8':"O",'9':"F",'15':"P",'16':"S",'17':"Cl",'35':"Br",'46':"Pd",'28':"Ni",'78':"Pt",'29':"Cu",'47':"Ag",'79':"Au"}

    flog = sys.argv[1]
    fxyz = sys.argv[2]
    nAtoms = get_nAtoms(fxzy)

    list_of_mols = []
    molecule_list = []

    with open(flog) as input_file:
        for i, line in enumerate(input_file):
            if 'Input orientation:' in line:
                one_mol = molecule()

                coords=''.join(islice(input_file, nAtoms+4))

                for i in range(4,nAtoms+4):
                    one_atom = atom(PSE[coords.split('\n')[i].split()[1]], coords.split('\n')[i].split()[3], coords.split('\n')[i].split()[4], coords.split('\n')[i].split()[5])
                    one_mol.add_atom(one_atom)

                #list_of_mols.append(one_mol.return_geom())
                list_of_mols.append(one_mol.return_distorted_geom())

    A = list_of_mols[:len(list_of_mols)/2 - 2]
    B = list_of_mols[len(list_of_mols)/2 + 2:]

    one_mol.print_geom()
