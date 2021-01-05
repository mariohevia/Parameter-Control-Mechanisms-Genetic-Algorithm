#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 08:58:07 2020

@author: mario_hevia
"""

import os, statistics
import numpy as np

def getPaths():
    data_path = 'Raw'
    filepaths = []
    for subdir, dirs, files in os.walk(data_path):
        for file in files:
            filepaths.append(os.path.join(subdir, file))
    filepaths.sort()
    return filepaths

def calcMAD(list_evals, median):
    MAD = statistics.median([abs(evals-median) for evals in list_evals])
    return MAD

filepaths = getPaths()
requested_problem = "OneMax"
# requested_problem = "LeadingOnes"
# requested_problem = "Jump"
# requested_problem = "WeightedNearestPeak"
# requested_problem = "NearestPeak"
# requested_problem = "MakespanScheduling"
value = 5000
requested_n = value
requested_k = 1
requested_p = round(1/requested_n,4)
requested_p_text = "1:"+str(requested_n)
requested_c = 1
requested_c_text = "1"
requested_off_size = 1
requested_F = 1.5
requested_F = 2
# requested_F = round((1+1/requested_n)**(4),4)
requested_algorithm = "DoubleFastOnePlusLambdaCommaLambda"
requested_extra = "None"

# requested_extra = "[50,10,0],[40,9,0],[40,9,0],[40,9,0],[40,9,0],[40,9,0]"
# requested_extra = "[50,10,0],[40,9,0],[41,9,0]"
# requested_extra = "[50,10,0],[40,9,0],[40,9,0],[40,9,0],[40,9,0],[40,9,0]"
# requested_extra = "[50,5,0],[40,3,0],[42,2,0],[44,1,0],[42,2,10]"
# requested_extra = "[50,5,0],[42,2,0],[41,4,0],[42,2,10]"

prettyNames = {"OnePlusLambda":"(1+1) EA",
               "OnePlusLambdaJUMP":"(1+1) EA",
               "OnePlusOneJUMP":"(1+1) EA",
               "FastOnePlusLambda":"(1+1) fEA",
               "FastOnePlusLambdaJUMP":"(1+1) fEA",
               "FastOnePlusOneJUMP":"(1+1) fEA",
               "FastOnePlusLambdaCommaLambda":"(1+(λ,λ)) fGA",
               "FastOnePlusLambdaCommaLambdaJUMP":"(1+(λ,λ)) fGA",
               "DoubleFastOnePlusLambdaCommaLambda":"(1+(λ,λ)) dfGA",
               "DoubleFastOnePlusLambdaCommaLambdaJUMP":"(1+(λ,λ)) dfGA",
               "OnePlusLambdaCommaLambdaSA":"SA (1+(λ,λ)) GA",
               "OnePlusLambdaCommaLambdaSAJUMP":"SA (1+(λ,λ)) GA",
               "OnePlusLambdaCommaLambdaSAReset":"SA (1+(λ,λ)) GA Reset",
               "OnePlusLambdaCommaLambdaSAResetJUMP":"SA (1+(λ,λ)) GA Reset"}

num_files = 0
total_runs = 0
evals = []
move_filepaths = []
all_requested_files = []
for filepath in filepaths:
    split_name = filepath.split('_')
    problem = split_name[3]
    n = int(split_name[4][1:])
    algorithm = split_name[5][3:]
    off_pop_size = int(split_name[6][1:][:-4])
    if (requested_problem == problem and requested_n == n and 
        requested_algorithm == algorithm and requested_off_size == off_pop_size):
        with open(filepath, 'r') as f:
            current_file = [line for line in f.readlines()]
            runs = int(current_file[4].split()[1])
            k = int(current_file[3].split()[3])
            extra = current_file[3].split()[5]
            p = round(float(current_file[9].split()[3]),4)
            c = float(current_file[11].split()[4])
            F = round(float(current_file[13].split()[7]),4)
            if (requested_k == k and requested_extra == extra and requested_p == p
                and requested_F == F and requested_c == c):
                print(filepath)
                move_filepaths.append(filepath)
                experiment_lines = current_file[-(6+runs):][:runs]
                num_files += 1
                total_runs += runs
                all_requested_files.extend(current_file)
                all_requested_files.append("\n")
                for experiment in experiment_lines:
                    current_evals = int(experiment.split()[7])
                    evals.append(current_evals)
                    
output_path = ("processed-results/" + prettyNames[requested_algorithm] + "_" + 
               requested_problem + "_n" + str(requested_n) + "_k" + str(requested_k) + 
               "_λ" + str(requested_off_size) + "_p" + str(requested_p_text) + 
               "_c" + str(requested_c) + "_F" + str(requested_F) + 
               "_extra-" + requested_extra)

if len(evals) !=0:
    quantile25 = np.quantile(np.array(evals, dtype='object'), 0.25)
    quantile50 = np.quantile(np.array(evals, dtype='object'), 0.50)
    quantile75 = np.quantile(np.array(evals, dtype='object'), 0.75)

    header = ("Problem: " + requested_problem + "\n" +
              "Algorithm: " + prettyNames[requested_algorithm] + "\n" +
              "Size: " + str(requested_n) + " k: " + str(requested_k) + " Extra: " + requested_extra + "\n" +
              "Number of files: " + str(num_files) + "\n" +
              "Number of runs: " + str(total_runs) + "\n" + 
              "Initial mutation probability: "  + str(requested_p) + "\n" + 
              "Initial crossover probability(if aplicable): "  + str(requested_c_text) + "\n" + 
              "Initial offspring population size: "  + str(requested_off_size) + "\n" + 
              "Offspring population size update factor (if aplicable): " + str(requested_F) + "\n" + 
              "Average evaluations: " + str(statistics.mean(evals)) + "\n" +
              "Median evaluations: " + str(statistics.median(evals)) + "\n" +
              "25% quantile: " + str(quantile25) + "\n" +
              "75% quantile: " + str(quantile75) + "\n" +
              "\n ============================== RAW FILES ============================== \n\n")

    all_requested_files_text = "".join(all_requested_files)
    final = header + all_requested_files_text

    with open(output_path, 'w') as f:
        f.write(final)
        
                
    print("Number of files:", num_files)
    print("Number of runs:", total_runs)
    print("Average:", statistics.mean(evals))
    print("Median:", statistics.median(evals))
    
    print("Quantiles:", quantile25, quantile50, quantile75)