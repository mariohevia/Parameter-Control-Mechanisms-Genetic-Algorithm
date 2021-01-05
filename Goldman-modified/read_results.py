#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 09:55:31 2020

@author: mario_hevia
"""
import os, statistics
import numpy as np
import matplotlib.pyplot as plt

def getPaths():
    data_path = 'results'
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
lengths = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
y8 = []
z1 = []
z2 = []
z3 = []
z4 = []
z5 = []
z6 = []
z7 = []
z8 = []
w1 = []
w2 = []
w3 = []
w4 = []
w5 = []
w6 = []
w7 = []
w8 = []

# Comment the lines with True for different graphs
verbose = False
verbose = True # If True prints the values for each point in the graph
fmedian = False
fmedian = True # If True graphs the medians, otherwise graphs quintile 75%
fMSAT = False
fMSAT = True # If True graphs the results for MAXSAT otherwise graphs ISG

if fMSAT:
    problemString = 'MAXSAT'
else: 
    problemString = 'IsingSpinGlass'
# max_eval = 2147483647 
max_eval = 2100000000 # Maximum value to consider a successful run
for filepath in filepaths:
    part = "0"
    problem, length, solver, extension = filepath.split('.')
    problem = problem.split('/')[1]
    if any(char.isdigit() for char in solver):
        solver, part = solver.split('_')
    if extension == "dat" and problem == problemString: 
        lengths.append(int(length))
        with open(filepath, 'r') as f:
            firstline = f.readline()
            if part != "2":
                evals = []    
                failures = 0
                exp_num = 0
            elif problemString == 'IsingSpinGlass' and part == "2":
                evals = []
                failures = 0
                exp_num = 100
            for line in f.readlines():
                exp_num += 1
                fitness, evaluations = line.split()
                # The next line is to avoid taking instances that were not used by Goldman and Punch
                if problemString == 'IsingSpinGlass' and exp_num<=100:# and False:
                    do_nothing = True
                else:
                    if float(fitness) == 1 and int(evaluations)<max_eval:
                        evals.append(int(evaluations))
                    else:
                        failures += 1
                        evals.append(1 * max_eval)
            evals.sort()
            if part != "1":
                median = statistics.median(evals)
                mean = statistics.mean(evals)
                MAD = calcMAD(evals, median)
                quantile75 = np.quantile(np.array(evals, dtype='object'), 0.75)
                if verbose:
                    print(problem, length, solver)
                    print('Runs:', len(evals))
                    print("Median:", median, "\nMean:", mean, 
                          "\nMAD:", MAD, "\nFailures:", failures)
                    print('Quantile 0.75:', quantile75)
                    print()
                if solver == 'OnePlusOne' and fmedian:
                    y1.append(median)
                elif solver == 'FastOnePlusOne' and fmedian:
                    y2.append(median)
                elif solver == 'LambdaLambda' and fmedian:
                    y3.append(median)
                elif solver == 'FastLambdaLambda' and fmedian:
                    y4.append(median)
                elif solver == 'DFastLambdaLambda' and fmedian:
                    y5.append(median)
                elif solver == 'LambdaLambdaCap' and fmedian:
                    y6.append(median)
                elif solver == 'LambdaLambdaReset' and fmedian:
                    y7.append(median)
                elif solver == 'LambdaLambdaResetF' and fmedian:
                    y8.append(median)
                elif solver == 'OnePlusOne' and not fmedian:
                        y1.append(quantile75)
                elif solver == 'FastOnePlusOne' and not fmedian:
                        y2.append(quantile75)
                elif solver == 'LambdaLambda' and not fmedian:
                        y3.append(quantile75)
                elif solver == 'FastLambdaLambda' and not fmedian:
                        y4.append(quantile75)
                elif solver == 'DFastLambdaLambda' and not fmedian:
                        y5.append(quantile75)
                elif solver == 'LambdaLambdaCap' and not fmedian:
                        y6.append(quantile75)
                elif solver == 'LambdaLambdaReset' and not fmedian:
                        y7.append(quantile75)
                elif solver == 'LambdaLambdaResetF' and not fmedian:
                        y8.append(quantile75)
                if solver == 'OnePlusOne':
                    w1.append(mean)
                elif solver == 'FastOnePlusOne':
                    w2.append(mean)
                elif solver == 'LambdaLambda':
                    w3.append(mean)
                elif solver == 'FastLambdaLambda':
                    w4.append(mean)
                elif solver == 'DFastLambdaLambda':
                    w5.append(mean)
                elif solver == 'LambdaLambdaCap':
                    w6.append(mean)
                elif solver == 'LambdaLambdaReset':
                    w7.append(mean)
                elif solver == 'LambdaLambdaResetF':
                    w8.append(mean)
                if solver == 'OnePlusOne':
                    z1.append(failures)
                elif solver == 'FastOnePlusOne':
                    z2.append(failures)
                elif solver == 'LambdaLambda':
                    z3.append(failures)
                elif solver == 'FastLambdaLambda':
                    z4.append(failures)
                elif solver == 'DFastLambdaLambda':
                    z5.append(failures)
                elif solver == 'LambdaLambdaCap':
                    z6.append(failures)
                elif solver == 'LambdaLambdaReset':
                    z7.append(failures)
                elif solver == 'LambdaLambdaResetF':
                    z8.append(failures)
                

x = list(set(lengths))
x.sort()
x = [str(i) for i in x] 

MARKER_SIZE = 8
fig = plt.figure(figsize=(13, 12))
fig.subplots_adjust(hspace=0.05)
ax1 = fig.add_subplot(311)
ax1.set_ylabel('Median')
ax1.set_yscale('log')
ax1.set_xticklabels([])
plt.grid(True, axis = 'x')
plt.plot(x, y1, '-', label='(1+1) EA p=1/n', color = "black", marker = "o", markersize=MARKER_SIZE)
plt.plot(x, y2, '-', label='(1+1) fEA β=1.5', color = "purple", marker = "s", markersize=MARKER_SIZE)
plt.plot(x, y3, '-', label='Vanilla SA (1+(λ,λ)) GA', color = "green", marker = "^", markersize=MARKER_SIZE)
plt.plot(x, y4, '-', label='(1+(λ,λ)) fGA', color = "darkcyan", marker = "X", markersize=MARKER_SIZE)
plt.plot(x, y5, '-', label='Non-standard (1+(λ,λ)) GA', color = "mediumblue", marker = "*", markersize=MARKER_SIZE)
plt.plot(x, y6, '-', label='SA (1+(λ,λ)) GA λ_max = n/2', color = "teal", marker = "P", markersize=MARKER_SIZE)
plt.plot(x, y7, '-', label='SA (1+(λ,λ)) GA reset', color = "red", marker = "X", markersize=MARKER_SIZE)
plt.plot(x, y8, '-', label='SA (1+(λ,λ)) GA reset F = (1+1/n)^4', color = "mediumblue", marker = "D", markersize=MARKER_SIZE)

ax2 = fig.add_subplot(312)
ax2.set_ylabel('Mean')
ax2.set_yscale('log')
ax2.set_xticklabels([])
plt.grid(True, axis = 'x')
plt.plot(x, w1, '-', label='(1+1) EA p=1/n', color = "black", marker = "o", markersize=MARKER_SIZE)
plt.plot(x, w2, '-', label='(1+1) fEA β=1.5', color = "purple", marker = "s", markersize=MARKER_SIZE)
plt.plot(x, w3, '-', label='Vanilla SA (1+(λ,λ)) GA', color = "green", marker = "^", markersize=MARKER_SIZE)
plt.plot(x, w4, '-', label='(1+(λ,λ)) fGA', color = "darkcyan", marker = "X", markersize=MARKER_SIZE)
plt.plot(x, w5, '-', label='Non-standard (1+(λ,λ)) GA', color = "mediumblue", marker = "*", markersize=MARKER_SIZE)
plt.plot(x, w6, '-', label='SA (1+(λ,λ)) GA λ_max = n/2', color = "teal", marker = "P", markersize=MARKER_SIZE)
plt.plot(x, w7, '-', label='SA (1+(λ,λ)) GA reset', color = "red", marker = "X", markersize=MARKER_SIZE)
plt.plot(x, w8, '-', label='SA (1+(λ,λ)) GA reset F = (1+1/n)^4', color = "mediumblue", marker = "D", markersize=MARKER_SIZE)

ax3 = fig.add_subplot(313)
ax3.set_xlabel('n')
ax3.set_ylabel('Failures')
plt.grid(True, axis = 'x')
plt.plot(x, z1, '-', label='(1+1) EA p=1/n', color = "black", marker = "o", markersize=MARKER_SIZE)
plt.plot(x, z2, '-', label='(1+1) fEA β=1.5', color = "purple", marker = "s", markersize=MARKER_SIZE)
plt.plot(x, z3, '-', label='Vanilla SA (1+(λ,λ)) GA', color = "green", marker = "^", markersize=MARKER_SIZE)
plt.plot(x, z4, '-', label='(1+(λ,λ)) fGA', color = "darkcyan", marker = "X", markersize=MARKER_SIZE)
plt.plot(x, z5, '-', label='Non-standard (1+(λ,λ)) GA', color = "mediumblue", marker = "*", markersize=MARKER_SIZE)
plt.plot(x, z6, '-', label='SA (1+(λ,λ)) GA λ_max = n/2', color = "teal", marker = "P", markersize=MARKER_SIZE)
plt.plot(x, z7, '-', label='SA (1+(λ,λ)) GA reset', color = "red", marker = "X", markersize=MARKER_SIZE)
plt.plot(x, z8, '-', label='SA (1+(λ,λ)) GA reset F = (1+1/n)^4', color = "mediumblue", marker = "D", markersize=MARKER_SIZE)

ax2.legend()
plt.show()
            