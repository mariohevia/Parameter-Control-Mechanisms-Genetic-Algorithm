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

bash_file_pt1 = """#!/bin/bash
#$ -l rmem=24G #number of memory
#$ -l h_rt=96:00:00
#$ -j y # normal and error outputs into a single file (the file above)
#$ -cwd # Run job from current directory
# Request 1 CPU cores
#$ -pe smp 1

cd ../
module load libs/boost/1.64.0/gcc-4.9.4

./Release/P3 config/default.cfg """

for length in LENGTHS_ISING:
    for i, optimizer in enumerate(OPTIMIZERS):
        config_name = 'IsingSpinGlass.' + str(length).zfill(4) + '.' + optimizer
        config_file = 'config/' + config_name + ".cfg"
        file = "bash_files/ISG" + str(length) + "_" + str(i) + ".sh"
        final = bash_file_pt1 + config_file
        with open(file,"w") as f:
            f.write(final)

for length in LENGTHS_MAXSAT:
    for i, optimizer in enumerate(OPTIMIZERS):
        config_name = 'MAXSAT.' + str(length).zfill(4) + '.' + optimizer
        config_file = 'config/' + config_name + ".cfg"
        file = "bash_files/MSAT" + str(length) + "_" + str(i) + ".sh"
        final = bash_file_pt1 + config_file
        with open(file,"w") as f:
            f.write(final)