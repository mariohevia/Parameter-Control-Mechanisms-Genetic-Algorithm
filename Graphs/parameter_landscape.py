#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:56:58 2020

@author: mario_hevia
"""
import math
import matplotlib.pyplot as plt
from scipy.special import comb
from decimal import Decimal
import decimal

decimal.getcontext().prec = 250

import os, re, statistics
def getPaths():
    data_path = 'Landscape_experiments'
    filepaths = []
    for subdir, dirs, files in os.walk(data_path):
        for file in files:
            filepaths.append(os.path.join(subdir, file))
    filepaths.sort()
    return filepaths

def crossover_success(n, k, L):
    p = Decimal(L)/Decimal(n)
    c = Decimal(1)/Decimal(L)
    B = 0
    for ell in range(k+1, 2*k):
        B += (Decimal(comb(n, ell)) * p**Decimal(ell) * (1-p)**Decimal((n-ell)) * 
              (Decimal(comb(n-k, ell-k))/Decimal(comb(n, ell)))**Decimal(L) * 
              (1-(1-c**Decimal(k)*(1-c)**Decimal((ell-k)))**Decimal(L)))
    C = 0
    for ell in range(2*k, n+1):
        C += (Decimal(comb(n, ell)) * p**Decimal(ell) * (1-p)**Decimal((n-ell)) * 
              (1-(1-Decimal(comb(n-k, ell-k))/Decimal(comb(n, ell)))**Decimal(L)) * 
              (1-(1-c**Decimal(k)*(1-c)**Decimal((ell-k)))**Decimal(L)))
    return B+C

def crossover_success2(n, k, L):
    p = Decimal(L)/Decimal(n)
    c = min(Decimal(k)/Decimal(L), 1)
    A = 0
    # A = comb(n, k) * p**k * (1-p)**(n-k) * (1-(1-1/comb(n, k))**L) * (1-(1-c**k)**L)
    B = 0
    for ell in range(k+1, 2*k):
        B += (Decimal(comb(n, ell)) * p**Decimal(ell) * (1-p)**Decimal((n-ell)) * 
              (Decimal(comb(n-k, ell-k))/Decimal(comb(n, ell)))**Decimal(L) * 
              (1-(1-c**Decimal(k)*(1-c)**Decimal((ell-k)))**Decimal(L)))
    C = 0
    for ell in range(2*k, n+1):
        C += (Decimal(comb(n, ell)) * p**Decimal(ell) * (1-p)**Decimal((n-ell)) * 
              (1-(1-Decimal(comb(n-k, ell-k))/Decimal(comb(n, ell)))**Decimal(L)) * 
              (1-(1-c**Decimal(k)*(1-c)**Decimal((ell-k)))**Decimal(L)))
    return A+B+C

def crossover_success3(n, k, L, i):
    p = Decimal(L)/Decimal(n)
    c = min(Decimal(i)/Decimal(L), 1)
    A = 0
    # A = comb(n, k) * p**k * (1-p)**(n-k) * (1-(1-1/comb(n, k))**L) * (1-(1-c**k)**L)
    B = 0
    for ell in range(k+1, 2*k):
        B += (Decimal(comb(n, ell)) * p**Decimal(ell) * (1-p)**Decimal((n-ell)) * 
              (Decimal(comb(n-k, ell-k))/Decimal(comb(n, ell)))**Decimal(L) * 
              (1-(1-c**Decimal(k)*(1-c)**Decimal((ell-k)))**Decimal(L)))
    C = 0
    for ell in range(2*k, n+1):
        C += (Decimal(comb(n, ell)) * p**Decimal(ell) * (1-p)**Decimal((n-ell)) * 
              (1-(1-Decimal(comb(n-k, ell-k))/Decimal(comb(n, ell)))**Decimal(L)) * 
              (1-(1-c**Decimal(k)*(1-c)**Decimal((ell-k)))**Decimal(L)))
    return A+B+C

def mutation_success(n, k, L):
    A = Decimal(comb(n, k))*((Decimal(L)/Decimal(n))**Decimal(k))*(1-Decimal(L)/Decimal(n))**Decimal(n-k)
    B = 1-(1-1/Decimal(comb(n, k)))**Decimal(L)
    return A*B
    
n = 60
k = 4
print("n:", n,"k:", k)
runtimes = []
lambdas = [x for x in range(2, math.floor(n/2)+1)]

for x in lambdas:
    ab = crossover_success(n, k, x)
    c = mutation_success(n, k, x)
    abc = 2*x/(ab+c)
    runtimes.append(abc)

A = []
B = []

if n == 60 and k == 4:
    filepaths = getPaths()
    mins = []
    maxes = []
    means = []
    std = []
    for filepath in filepaths:
        L = int(filepath.split('_')[5][1:])
        with open(filepath, 'r') as f:
            A.append(L)
            evaluations = [int(re.findall("\d+", line.split(':')[4])[0]) for line in f.readlines() if 'Final' in line]
            mins.append(min(evaluations))
            maxes.append(max(evaluations))
            means.append(statistics.mean(evaluations))
            std.append(statistics.stdev(evaluations))

fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(111)
ax1.set_xlabel('$λ_{\max}$')
ax1.set_ylabel('Fitness evaluations')
ax1.set_yscale('log')
plt.plot(lambdas, runtimes, '-.', color = "black")
plt.plot(A, means, 'o', color = "red")
plt.show()


# ###############################################################################
enes = [100,200,300]
kas = {100:[3, 4, 5, 6],
        200:[3, 4, 5, 6],
        300:[3, 4, 5, 6]}


runtimes = []
lambdas = []

for n in enes:
    current_lambdas = [x for x in range(2, n)]
    for k in kas[n]:
        runtime_k = []
        for x in current_lambdas:
            ab = crossover_success(n, k, x)
            c = mutation_success(n, k, x)
            abc = 2*x/(ab+c)
            runtime_k.append(abc)
        runtimes.append(runtime_k)
    lambdas.append(current_lambdas)

fig = plt.figure(figsize=(13, 10))

ax1 = fig.add_subplot(441)
ax1.set_xlabel('$λ_{\max}$')
# ax1.set_ylabel('Fitness evaluations')
ax1.set_yscale('log')
plt.title('k = 3')
plt.plot(lambdas[0], runtimes[0], '-.', label='runtime Upper bounds', color = "black", marker = ".")

ax2 = fig.add_subplot(442)
ax2.set_xlabel('$λ_{\max}$')
# ax2.set_ylabel('Fitness evaluations')
ax2.set_yscale('log')
plt.title('k = 4')
plt.plot(lambdas[0], runtimes[1], '-.', label='runtime Upper bounds', color = "black", marker = ".")

ax3 = fig.add_subplot(443)
ax3.set_xlabel('$λ_{\max}$')
# ax3.set_ylabel('Fitness evaluations')
ax3.set_yscale('log')
plt.title('k = 5')
plt.plot(lambdas[0], runtimes[2], '-.', label='runtime Upper bounds', color = "black", marker = ".")

ax4 = fig.add_subplot(444)
ax4.set_xlabel('$λ_{\max}$')
# ax4.set_ylabel('Fitness evaluations')
ax4.set_yscale('log')
plt.title('k = 6')
plt.plot(lambdas[0], runtimes[3], '-.', label='runtime Upper bounds', color = "black", marker = ".")

ax5 = fig.add_subplot(445)
ax5.set_xlabel('$λ_{\max}$')
ax5.set_ylabel('Fitness evaluations')
ax5.set_yscale('log')
# plt.title('k = 2')
plt.plot(lambdas[1], runtimes[4], '-.', label='runtime Upper bounds', color = "black", marker = ".")

ax6 = fig.add_subplot(446)
ax6.set_xlabel('$λ_{\max}$')
# ax6.set_ylabel('Fitness evaluations')
ax6.set_yscale('log')
# plt.title('k = 3')
plt.plot(lambdas[1], runtimes[5], '-.', label='runtime Upper bounds', color = "black", marker = ".")

ax7 = fig.add_subplot(447)
ax7.set_xlabel('$λ_{\max}$')
# ax7.set_ylabel('Fitness evaluations')
ax7.set_yscale('log')
# plt.title('k = 4')
plt.plot(lambdas[1], runtimes[6], '-.', label='runtime Upper bounds', color = "black", marker = ".")

ax8 = fig.add_subplot(448)
ax8.set_xlabel('$λ_{\max}$')
# ax8.set_ylabel('Fitness evaluations')
ax8.set_yscale('log')
# plt.title('k = 5')
plt.plot(lambdas[1], runtimes[7], '-.', label='runtime Upper bounds', color = "black", marker = ".")

ax9 = fig.add_subplot(449)
ax9.set_xlabel('$λ_{\max}$')
# ax9.set_ylabel('Fitness evaluations')
ax9.set_yscale('log')
# plt.title('k = 2')
plt.plot(lambdas[2], runtimes[8], '-.', label='runtime Upper bounds', color = "black", marker = ".")

ax10 = fig.add_subplot(4,4,10)
ax10.set_xlabel('$λ_{\max}$')
# ax10.set_ylabel('Fitness evaluations')
ax10.set_yscale('log')
# plt.title('k = 3')
plt.plot(lambdas[2], runtimes[9], '-.', label='runtime Upper bounds', color = "black", marker = ".")

ax11 = fig.add_subplot(4,4,11)
ax11.set_xlabel('$λ_{\max}$')
# ax11.set_ylabel('Fitness evaluations')
ax11.set_yscale('log')
# plt.title('k = 4')
plt.plot(lambdas[2], runtimes[10], '-.', label='runtime Upper bounds', color = "black", marker = ".")

ax12 = fig.add_subplot(4,4,12)
ax12.set_xlabel('$λ_{\max}$')
# ax12.set_ylabel('Fitness evaluations')
ax12.set_yscale('log')
# plt.title('k = 5')
plt.plot(lambdas[2], runtimes[11], '-.', label='runtime Upper bounds', color = "black", marker = ".")
plt.show()


