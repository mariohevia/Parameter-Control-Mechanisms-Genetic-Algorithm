#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 14:17:08 2020

@author: mario_hevia
"""

LENGTHS_ISING=[16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 
         361, 400, 441, 484, 529, 576, 625, 676, 729, 784]

LENGTHS_MAXSAT=[10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]

OPTIMIZERS = ["LambdaLambda", "LambdaLambdaCap", "LambdaLambdaReset", 
              "LambdaLambdaResetF", "OnePlusOne", "FastOnePlusOne",
              "FastLambdaLambda", "DFastLambdaLambda"]

Ising_file_pt1 = """
# Experiment Related
experiment multirun # Specifies the high level experiment to perform, could be "multirun" "singlerun" or "bisection"
runs 200 # How many full restarts to perform
eval_limit 2147483647 # Limit at 2+ billion evaluations maximum integer
fitness_limit 1.0 # If this (or better) fitness is reached, stop
precision 65536 # Used in rounding
seed -1 # Seed at the start of the experiment.  -1 seeds using system device
verbosity 1 # How much information to output to the screen"""

Ising_file_pt2 = """
disable_solution_outfile 1

# Problem Related
problem IsingSpinGlass # Select which problem to optimize
ising_type pm # Used to specify Ising topologies"""

Ising_file_pt3 = """ # Sets the number of bits in the problem
problem_seed 0 # When generating random problems, seed with this + run number
problem_folder problem_files/ # Where to find/save problem files

# Optimizer
optimizer """

for length in LENGTHS_ISING:
    for optimizer in OPTIMIZERS:
        file_name = 'IsingSpinGlass.' + str(length).zfill(4) + '.' + optimizer
        file = file_name + ".cfg"
        cfg_file = "\ncfg_file results/" + file_name + ".cfg"
        dat_file = "\ndat_file results/" + file_name + ".dat"
        length_line = "\nlength "+ str(length)
        final = Ising_file_pt1 + cfg_file + dat_file + Ising_file_pt2 + length_line + Ising_file_pt3 + optimizer
        with open(file,"w") as f:
            f.write(final)
            
MAXSAT_file_pt1 = """
# Experiment Related
experiment multirun # Specifies the high level experiment to perform, could be "multirun" "singlerun" or "bisection"
runs 100 # How many full restarts to perform
eval_limit 2147483647 # Limit at 2+ billion evaluations maximum integer
fitness_limit 1.0 # If this (or better) fitness is reached, stop
precision 65536 # Used in rounding
seed -1 # Seed at the start of the experiment.  -1 seeds using system device
verbosity 1 # How much information to output to the screen"""

MAXSAT_file_pt2 = """
disable_solution_outfile 1

# Problem Related
problem MAXSAT # Select which problem to optimize"""

MAXSAT_file_pt3 = """ # Sets the number of bits in the problem
clause_ratio 4.27 # Used by MAXSAT
problem_seed 100 # When generating random problems, seed with this + run number
problem_folder problem_files/ # Where to find/save problem files

# Optimizer
optimizer """

for length in LENGTHS_MAXSAT:
    for optimizer in OPTIMIZERS:
        file_name = 'MAXSAT.' + str(length).zfill(4) + '.' + optimizer
        file = file_name + ".cfg"
        cfg_file = "\ncfg_file results/" + file_name + ".cfg"
        dat_file = "\ndat_file results/" + file_name + ".dat"
        length_line = "\nlength "+ str(length)
        final = MAXSAT_file_pt1 + cfg_file + dat_file + MAXSAT_file_pt2 + length_line + MAXSAT_file_pt3 + optimizer
        with open(file,"w") as f:
            f.write(final)
            