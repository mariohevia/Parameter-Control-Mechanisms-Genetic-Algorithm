#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 20:36:55 2018

@author: mario_hevia
"""

import numpy as np
from operator import itemgetter


# New optimised
class OneMax:
    def __init__(self, problem_size, not_used):
        self.max_fitness = problem_size
        
    def evaluate(self, bit_string):
        fitness_value = bin(bit_string).count('1')
        if fitness_value == self.max_fitness:
            optimal_fitness = True
        else:
            optimal_fitness = False
        return fitness_value, optimal_fitness

class LeadingOnes:
    def __init__(self, problem_size, not_used):
        self.max_fitness = problem_size
        
    def evaluate(self, bit_string):
        fitness_value = 0
        for bit in format(bit_string, '0'+str(self.max_fitness)+'b'):
            if bit == '1':
                fitness_value += 1
            else:
                break
        if fitness_value == self.max_fitness:
            optimal_fitness = True
        else:
            optimal_fitness = False
        return fitness_value, optimal_fitness

class Ridge:
    def __init__(self, problem_size, not_used):
        self.problem_size = problem_size
        self.max_fitness = 2*problem_size
        
    def evaluate(self, bit_string):
        OM = bin(bit_string).count('1')
        LO = 0
        for bit in format(bit_string, '0'+str(self.problem_size)+'b'):
            if bit == '1':
                LO += 1
            else:
                break
        if LO == OM:
            fitness_value = self.problem_size + OM
        else:
            fitness_value = self.problem_size - OM
        if fitness_value == self.max_fitness:
            optimal_fitness = True
        else:
            optimal_fitness = False
        return fitness_value, optimal_fitness

class Trap:
    def __init__(self, problem_size, not_used):
        self.max_fitness = problem_size + 1
        
    def evaluate(self, bit_string):
        fitness_value = bin(bit_string).count('1')
        if fitness_value == 0:
            fitness_value = self.max_fitness
        if fitness_value == self.max_fitness:
            optimal_fitness = True
        else:
            optimal_fitness = False
        return fitness_value, optimal_fitness

class Needle:
    def __init__(self, problem_size, not_used):
        self.max_fitness = problem_size
        
    def evaluate(self, bit_string):
        fitness_value = bin(bit_string).count('1')
        if fitness_value == self.max_fitness:
            fitness_value = self.max_fitness
        else:
            fitness_value = 0
        if fitness_value == self.max_fitness:
            optimal_fitness = True
        else:
            optimal_fitness = False
        return fitness_value, optimal_fitness

class Jump:
    def __init__(self, problem_size, jump_size):
        self.problem_size = problem_size
        self.max_fitness = jump_size + problem_size
        self.jump_size = jump_size
        
    def evaluate(self, bit_string):
        one_max = bin(bit_string).count('1')
        if one_max <= self.problem_size - self.jump_size or one_max == self.problem_size:
            fitness_value = self.jump_size + one_max
        else:
            fitness_value = self.problem_size - one_max
        if fitness_value == self.max_fitness:
            optimal_fitness = True
        else:
            optimal_fitness = False
        return fitness_value, optimal_fitness

class Cliff:
    def __init__(self, problem_size, jump_size):
        self.problem_size = problem_size
        self.max_fitness = self.problem_size
        self.jump_size = jump_size
        
    def evaluate(self, bit_string):
        one_max = bin(bit_string).count('1')
        if one_max < self.problem_size - self.jump_size or one_max == self.problem_size:
            fitness_value = one_max
        else:
            fitness_value = one_max - self.jump_size + 1/2
        if fitness_value == self.max_fitness:
            optimal_fitness = True
        else:
            optimal_fitness = False
        return fitness_value, optimal_fitness
    
class Plateau:
    def __init__(self, problem_size, plateau_size):
        self.max_fitness = problem_size + 2
        self.problem_size = problem_size
        self.plateau_size = plateau_size
        
    def evaluate(self, bit_string):
        one_max = bin(bit_string).count('1')
        leading_ones = 0
        for bit in format(bit_string, '0'+str(self.max_fitness)+'b'):
            if bit == '1':
                leading_ones += 1
            else:
                break
        if leading_ones == 0:
            fitness_value = self.problem_size - one_max
        elif leading_ones < self.problem_size:
            fitness_value = self.problem_size + 1
        else:
            fitness_value = self.problem_size + 2
        if fitness_value == self.max_fitness :
            optimal_fitness = True
        else:
            optimal_fitness = False
        return fitness_value, optimal_fitness

class NearestPeak:
    def __init__(self, problem_size, not_used, peak_settings):
        # peak_settings should be: '[p1,a1,b1],[p2,a2,b2],...' without spaces
        # pi := number of ones in peak (chosen at random)
        # ai := slope
        # bi := offset
        self.problem_size = problem_size
        pre_peaks = peak_settings.split('],')
        self.peaks = []
        for p in pre_peaks:
            tmp_p = p.strip('[]').split(',')
            tmp_peak_indexes = np.random.choice(self.problem_size, size = int(tmp_p[0]),
                                                replace=False)
            tmp_peak = sum([2**int(i) for i in tmp_peak_indexes])
            self.peaks.append([tmp_peak, int(tmp_p[1]), int(tmp_p[2])])
            
        #for i, p in enumerate(self.peaks):
        #    print(i, p[0], format(p[0], '0'+str(self.problem_size)+'b'))
            
        self.max_fitness = 0
        for p, a, b in self.peaks:
            if self.problem_size*a+b>self.max_fitness:
                self.max_fitness = self.problem_size*a+b
        
    def evaluate(self, bit_string):
        eval_peaks = []
        for p, a, b in self.peaks:
            G = self.problem_size - bin(p^bit_string).count('1')#Change to bin?
            eval_peaks.append((G, a*G+b))
        eval_peaks.sort(key=itemgetter(0,1), reverse=True)
        fitness_value = eval_peaks[0][1]
        if fitness_value == self.max_fitness:
            optimal_fitness = True
        else:
            optimal_fitness = False 
        return fitness_value, optimal_fitness

class WeightedNearestPeak:
    def __init__(self, problem_size, not_used, peak_settings):
        # peak_settings should be: '[p1,a1,b1],[p2,a2,b2],...' without spaces
        # pi := number of ones in peak (chosen at random)
        # ai := slope
        # bi := offset
        self.problem_size = problem_size
        pre_peaks = peak_settings.split('],')
        self.peaks = []
        for p in pre_peaks:
            tmp_p = p.strip('[]').split(',')
            tmp_peak_indexes = np.random.choice(self.problem_size, size = int(tmp_p[0]),
                                                replace=False)
            tmp_peak = sum([2**int(i) for i in tmp_peak_indexes])
            self.peaks.append([tmp_peak, int(tmp_p[1]), int(tmp_p[2])])
            
        #for i, p in enumerate(self.peaks):
        #    print(i, p[0], format(p[0], '0'+str(self.problem_size)+'b'))
            
        self.max_fitness = 0
        for p, a, b in self.peaks:
            if self.problem_size*a+b>self.max_fitness:
                self.max_fitness = self.problem_size*a+b
        
    def evaluate(self, bit_string):
        eval_peaks = []
        for p, a, b in self.peaks:
            G = self.problem_size - bin(p^bit_string).count('1')#Change to bin?
            eval_peaks.append((G, a*G+b))
        eval_peaks.sort(key=itemgetter(1), reverse=True)
        fitness_value = eval_peaks[0][1]
        if fitness_value == self.max_fitness:
            optimal_fitness = True
        else:
            optimal_fitness = False 
        return fitness_value, optimal_fitness

class MakespanScheduling:
    def __init__(self, problem_size, not_used):
        self.weights = np.random.uniform(low=0, high=1, size=(problem_size,))
        self.sum_weights = np.sum(self.weights)
        self.max_fitness = self.sum_weights - self.aprox_solution()
        self.problem_size = problem_size
        
    def evaluate(self, bit_string):
        bit_string = format(bit_string, '0'+str(self.problem_size)+'b')
        sum_0 = sum([self.weights[i] for i, char in enumerate(bit_string) if char == '0'])
        sum_1 = sum([self.weights[i] for i, char in enumerate(bit_string) if char == '1'])
        fitness_value = self.sum_weights - max(sum_0, sum_1)
        if fitness_value >= self.max_fitness:
            optimal_fitness = True
        else:
            optimal_fitness = False
        return fitness_value, optimal_fitness
    
    def aprox_solution(self):
        jobs_sorted = np.flip(np.sort(self.weights), 0)
        sums = [0, 0]
        for job in jobs_sorted:
            min_index, min_value = min(enumerate(sums), 
                                       key=itemgetter(1))
            sums[min_index] += job
        return max(sums)

class IsingSpinGlass:
    def __init__(self, problem_size, not_used, file_name):
        self.problem_size = problem_size
        self.dependencies = []
        file = "utils/problem_files/" + file_name
        with open(file,"r") as f:
            first_line = f.readline().split()
            self.max_fitness = -int(first_line[0])
            self.max_string = int(first_line[1],2)
            num_dependencies = int(f.readline())
            for line in f.readlines():
                self.dependencies.append([int(i) for i in line.split()])
            
        
    def evaluate(self, bit_string):
        # bit_string = format(bit_string, '0'+str(self.problem_size)+'b')
        # bit_string = [1 if i=="1" else -1 for i in bit_string]
        bit_string = [1 if x=="1" else -1 for x in format(bit_string, '0'+str(self.problem_size)+'b')]
        fitness_value = sum([bit_string[i]*bit_string[j]*factor for
                             i, j, factor in self.dependencies])
        if fitness_value == self.max_fitness:
            optimal_fitness = True
        else:
            optimal_fitness = False
        return fitness_value, optimal_fitness

    
class MaxSat:
    def __init__(self, problem_size, not_used, file_name):
        self.problem_size = problem_size
        self.clauses = []
        self.signs = []
        file = "utils/problem_files/" + file_name
        with open(file,"r") as f:
            self.max_string = int(f.readline().strip(),2)
            for line in f.readlines():
                clause = []
                sign = []
                for pair in line.strip().split(' '):
                    s, v = pair.split(',')  
                    clause.append(int(v))
                    sign.append(s)
                self.clauses.append(clause)
                self.signs.append(sign)
        self.max_fitness = 0
        self.max_fitness = self.evaluate(self.max_string)[0]
            
        
    def evaluate(self, bit_string):
        # if bit_string == self.max_string:
        #     return self.max_fitness, True
        bit_string = format(bit_string, '0'+str(self.problem_size)+'b')
        fitness_value = 0
        for (c1, c2, c3), (s1, s2, s3) in zip(self.clauses, self.signs):
            if (bit_string[c1] == s1):
                fitness_value += 1
            elif (bit_string[c2] == s2):
                fitness_value += 1
            elif (bit_string[c3] == s3):
                fitness_value += 1
        if fitness_value == self.max_fitness:
            optimal_fitness = True
        else:
            optimal_fitness = False
        return fitness_value, optimal_fitness
