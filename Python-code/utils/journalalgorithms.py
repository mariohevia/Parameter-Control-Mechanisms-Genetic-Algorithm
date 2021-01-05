#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:34:24 2020

@author: mario_hevia
"""

import numpy as np
import scipy.stats as stats
import random
import heapq
import math

class OnePlusLambda:
    def __init__(self, problem, problem_size, mutation_probability, 
                 offspring_size, not_used_1, not_used_2, not_used_3, not_used_4):
        self.problem = problem
        self.problem_size = problem_size
        self.mutation_probability = mutation_probability
        self.offspring_size = offspring_size
        self.bit_string = random.randint(0,2**problem_size-1)
        # print(self.bit_string)
        self.solved = False
        self.evaluations = 0
        self.generations = 0
        self.fit_gen = []
        self.lambda_gen = []
        self.mut_prob_gen = []
        self.parent = [self.problem.evaluate(self.bit_string), 
                        self.bit_string]
        self.no_mut_flag = False
        
    def __next__(self):
        # print()
        # print(self.parent, format(self.parent[1], '0'+str(self.problem_size)+'b'))
        offspring = []
        self.mut_prob_gen.append(self.mutation_probability)
        self.lambda_gen.append(self.offspring_size)
        for i in range(self.offspring_size):
            mutated_string = self.mutate()
            if self.no_mut_flag == True:
                self.no_mut_flag = False
                offspring.append((self.parent[0], self.parent[1]))    
            else:
                # print((self.problem.evaluate(mutated_string), mutated_string), format(mutated_string, '0'+str(self.problem_size)+'b'))
                offspring.append((self.problem.evaluate(mutated_string), 
                                  mutated_string))
        self.select(offspring)
        self.generations += 1
        self.evaluations += self.offspring_size
    
    def mutate(self):
        l = np.random.binomial(self.problem_size, self.mutation_probability)
        if l == 0:
            self.no_mut_flag = True
            return self.parent[1]
        mut_indexes = np.random.choice(self.problem_size, size = l,
                                       replace=False)
        mut_int = sum([2**int(i) for i in mut_indexes])
        mutated_string = mut_int^self.parent[1]
        return mutated_string
    
    def select(self, offspring):
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        if eval_fittest[0] >= self.parent[0][0]:
            self.parent = [eval_fittest, 
                           int(fittest)]
            self.fit_gen.append(eval_fittest[0])
        else:
            self.fit_gen.append(self.parent[0][0])
        if eval_fittest[1]:
            self.solved = True


###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

class OnePlusLambdaJUMP: 
    def __init__(self, problem, problem_size, mutation_probability, 
                 offspring_size, not_used_1, not_used_2, not_used_3, not_used_4):
        self.problem = problem
        self.problem_size = problem_size
        self.mutation_probability = mutation_probability
        self.offspring_size = offspring_size
        self.bit_string = random.randint(0,2**problem_size-1)
        # print(self.bit_string)
        self.solved = False
        self.evaluations = 0
        self.generations = 0
        self.fit_gen = []
        self.lambda_gen = []
        self.mut_prob_gen = []
        self.parent = [self.problem.evaluate(self.bit_string), 
                        self.bit_string]
        self.no_mut_flag = False
        
    def __next__(self):
        offspring = []
        self.mut_prob_gen.append(self.mutation_probability)
        self.lambda_gen.append(self.offspring_size)
        if self.problem_size == self.parent[0][0]:
            for i in range(self.offspring_size):
                mutated_string = self.mutate2()
                if mutated_string != None:
                    offspring.append((self.problem.evaluate(mutated_string), 
                                      mutated_string))
            if len(offspring)>0:
                self.select(offspring)
        else:
            for i in range(self.offspring_size):
                mutated_string = self.mutate()
                if self.no_mut_flag == True:
                    self.no_mut_flag = False
                    offspring.append((self.parent[0], self.parent[1]))    
                else:
                    offspring.append((self.problem.evaluate(mutated_string), 
                                      mutated_string))
            self.select(offspring)
        self.generations += 1
        self.evaluations += self.offspring_size
    
    def mutate(self):
        l = np.random.binomial(self.problem_size, self.mutation_probability)
        if l == 0:
            self.no_mut_flag = True
            return self.parent[1]
        mut_indexes = np.random.choice(self.problem_size, size = l,
                                       replace=False)
        mut_int = sum([2**int(i) for i in mut_indexes])
        mutated_string = mut_int^self.parent[1]
        return mutated_string
    
    def mutate2(self):
        l = np.random.binomial(self.problem_size, self.mutation_probability)
        if l != self.problem.jump_size:
            return
        mut_indexes = np.random.choice(self.problem_size, size = l,
                                       replace=False)
        mut_int = sum([2**int(i) for i in mut_indexes])
        mutated_string = mut_int^self.parent[1]
        return mutated_string
    
    def select(self, offspring):
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        if eval_fittest[0] >= self.parent[0][0]:
            self.parent = [eval_fittest, 
                           int(fittest)]
            self.fit_gen.append(eval_fittest[0])
        else:
            self.fit_gen.append(self.parent[0][0])
        if eval_fittest[1]:
            self.solved = True


###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################


class OnePlusOneJUMP: 
    def __init__(self, problem, problem_size, mutation_probability, 
                 not_used_0, not_used_1, not_used_2, not_used_3, not_used_4):
        self.problem = problem
        self.problem_size = problem_size
        self.mutation_probability = mutation_probability
        self.bit_string = random.randint(0,2**problem_size-1)
        # print(self.bit_string)
        self.solved = False
        self.evaluations = 0
        self.generations = 0
        self.fit_gen = []
        self.lambda_gen = []
        self.mut_prob_gen = []
        self.parent = [self.problem.evaluate(self.bit_string), 
                        self.bit_string]
        self.no_mut_flag = False
        
    def __next__(self):
        self.mut_prob_gen.append(self.mutation_probability)
        self.lambda_gen.append(1)
        SIZE = 1000000
        if self.problem_size == self.parent[0][0]:    
            elles = np.random.binomial(self.problem_size, self.mutation_probability, size = SIZE)
            filtered_elles = elles[np.where(elles == self.problem.jump_size)]
            i = 0
            for elle in filtered_elles:
                mutated_string = self.mutate2(elle)
                fitness , solved = self.problem.evaluate(mutated_string)
                if solved:
                    self.solved = True
                    self.evaluations += int(np.where(elles == self.problem.jump_size)[0][i])
                    self.generations += int(np.where(elles == self.problem.jump_size)[0][i])
                    self.fit_gen.append(self.parent[0][0])
                    break
                i+=1
            if self.solved == False:                
                self.fit_gen.append(self.parent[0][0])
                self.evaluations += SIZE
                self.generations += SIZE
        else:
            mutated_string = self.mutate()
            if self.no_mut_flag == True:
                self.no_mut_flag = False 
            else:
                fitness, solved = self.problem.evaluate(mutated_string)
                if fitness>=self.parent[0][0]:
                    self.parent = [(fitness, solved), mutated_string]
                if solved:
                    self.solved = True
            self.fit_gen.append(self.parent[0][0])
            self.evaluations += 1
            self.generations += 1
    
    def mutate(self):
        l = np.random.binomial(self.problem_size, self.mutation_probability)
        if l == 0:
            self.no_mut_flag = True
            return self.parent[1]
        mut_indexes = np.random.choice(self.problem_size, size = l,
                                       replace=False)
        mut_int = sum([2**int(i) for i in mut_indexes])
        mutated_string = mut_int^self.parent[1]
        return mutated_string
    
    def mutate2(self, l):
        mut_indexes = np.random.choice(self.problem_size, size = l,
                                       replace=False)
        mut_int = sum([2**int(i) for i in mut_indexes])
        mutated_string = mut_int^self.parent[1]
        return mutated_string


###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################


class FastOnePlusLambda:
    def __init__(self, problem, problem_size, mutation_probability, 
                 offspring_size, not_used_1, not_used_2, not_used_3, not_used_4):
        self.problem = problem
        self.problem_size = problem_size
        self.mutation_probability = mutation_probability
        self.offspring_size = offspring_size
        self.bit_string = random.randint(0,2**problem_size-1)
        # print(self.bit_string)
        self.solved = False
        self.evaluations = 0
        self.generations = 0
        self.fit_gen = []
        self.lambda_gen = []
        self.mut_prob_gen = []
        self.parent = [self.problem.evaluate(self.bit_string), 
                        self.bit_string]
        self.no_mut_flag = False
        B = 1.5
        n = math.floor(self.problem_size)
        x = np.arange(1, n+1, dtype='float')
        pmf = 1/x**B
        pmf /= pmf.sum()
        # print(pmf, sum(pmf))
        self.power_dist = stats.rv_discrete(values=(range(1, n+1), pmf))
        
    def __next__(self):
        offspring = []
        self.mut_prob_gen.append(self.mutation_probability)
        self.lambda_gen.append(self.offspring_size)
        for i in range(self.offspring_size):
            mutated_string = self.mutate()
            if self.no_mut_flag == True:
                self.no_mut_flag = False
                offspring.append((self.parent[0], self.parent[1]))    
            else:
                offspring.append((self.problem.evaluate(mutated_string), 
                                  mutated_string))
        self.select(offspring)
        self.generations += 1
        self.evaluations += self.offspring_size
    
    def mutate(self):
        alpha = self.power_dist.rvs(0)/self.problem_size
        l = np.random.binomial(self.problem_size, alpha)
        if l == 0:
            self.no_mut_flag = True
            return self.parent[1]
        mut_indexes = np.random.choice(self.problem_size, size = l,
                                       replace=False)
        mut_int = sum([2**int(i) for i in mut_indexes])
        mutated_string = mut_int^self.parent[1]
        return mutated_string
    
    def select(self, offspring):
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        if eval_fittest[0] >= self.parent[0][0]:
            self.parent = [eval_fittest, 
                           int(fittest)]
            self.fit_gen.append(eval_fittest[0])
        else:
            self.fit_gen.append(self.parent[0][0])
        if eval_fittest[1]:
            self.solved = True


###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################


class FastOnePlusLambdaJUMP:
    def __init__(self, problem, problem_size, mutation_probability, 
                 offspring_size, not_used_1, not_used_2, not_used_3, not_used_4):
        self.problem = problem
        self.problem_size = problem_size
        self.mutation_probability = mutation_probability
        self.offspring_size = offspring_size
        self.bit_string = random.randint(0,2**problem_size-1)
        # print(self.bit_string)
        self.solved = False
        self.evaluations = 0
        self.generations = 0
        self.fit_gen = []
        self.lambda_gen = []
        self.mut_prob_gen = []
        self.parent = [self.problem.evaluate(self.bit_string), 
                        self.bit_string]
        self.no_mut_flag = False
        B = 1.5
        n = math.floor(self.problem_size)
        x = np.arange(1, n+1, dtype='float')
        pmf = 1/x**B
        pmf /= pmf.sum()
        self.power_dist = stats.rv_discrete(values=(range(1, n+1), pmf))
        
    def __next__(self):
        offspring = []
        self.mut_prob_gen.append(self.mutation_probability)
        self.lambda_gen.append(self.offspring_size)
        if self.problem_size == self.parent[0][0]:
            for i in range(self.offspring_size):
                mutated_string = self.mutate2()
                if mutated_string != None:
                    offspring.append((self.problem.evaluate(mutated_string), 
                                      mutated_string))
            if len(offspring)>0:
                self.select(offspring)
        else:
            for i in range(self.offspring_size):
                mutated_string = self.mutate()
                if self.no_mut_flag == True:
                    self.no_mut_flag = False
                    offspring.append((self.parent[0], self.parent[1]))    
                else:
                    offspring.append((self.problem.evaluate(mutated_string), 
                                      mutated_string))
            self.select(offspring)
        self.generations += 1
        self.evaluations += self.offspring_size
    
    def mutate(self):
        alpha = self.power_dist.rvs(0)/self.problem_size
        l = np.random.binomial(self.problem_size, alpha)
        if l == 0:
            self.no_mut_flag = True
            return self.parent[1]
        mut_indexes = np.random.choice(self.problem_size, size = l,
                                       replace=False)
        mut_int = sum([2**int(i) for i in mut_indexes])
        mutated_string = mut_int^self.parent[1]
        return mutated_string
    
    def mutate2(self):
        alpha = self.power_dist.rvs(0)/self.problem_size
        l = np.random.binomial(self.problem_size, alpha)
        if l != self.problem.jump_size:
            return
        mut_indexes = np.random.choice(self.problem_size, size = l,
                                       replace=False)
        mut_int = sum([2**int(i) for i in mut_indexes])
        mutated_string = mut_int^self.parent[1]
        return mutated_string
    
    def select(self, offspring):
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        if eval_fittest[0] >= self.parent[0][0]:
            self.parent = [eval_fittest, 
                           int(fittest)]
            self.fit_gen.append(eval_fittest[0])
        else:
            self.fit_gen.append(self.parent[0][0])
        if eval_fittest[1]:
            self.solved = True


###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################


class FastOnePlusOneJUMP:
    def __init__(self, problem, problem_size, mutation_probability, 
                 not_used_0, not_used_1, not_used_2, not_used_3, not_used_4):
        self.problem = problem
        self.problem_size = problem_size
        self.mutation_probability = mutation_probability
        self.bit_string = random.randint(0,2**problem_size-1)
        self.solved = False
        self.evaluations = 0
        self.generations = 0
        self.fit_gen = []
        self.lambda_gen = []
        self.mut_prob_gen = []
        self.parent = [self.problem.evaluate(self.bit_string), 
                        self.bit_string]
        self.no_mut_flag = False
        B = 1.5
        n = math.floor(self.problem_size)
        x = np.arange(1, n+1, dtype='float')
        pmf = 1/x**B
        pmf /= pmf.sum()
        self.power_dist = stats.rv_discrete(values=(range(1, n+1), pmf))
        
    def __next__(self):
        self.mut_prob_gen.append(self.mutation_probability)
        self.lambda_gen.append(1)
        SIZE = 1000000
        if self.problem_size == self.parent[0][0]:    
            alphas = self.power_dist.rvs(size=SIZE)/self.problem_size
            elles = np.random.binomial(self.problem_size, alphas)
            filtered_elles = elles[np.where(elles == self.problem.jump_size)]
            i = 0
            for elle in filtered_elles:
                mutated_string = self.mutate2(elle)
                fitness , solved = self.problem.evaluate(mutated_string)
                if solved:
                    self.solved = True
                    self.evaluations += int(np.where(elles == self.problem.jump_size)[0][i])
                    self.generations += int(np.where(elles == self.problem.jump_size)[0][i])
                    self.fit_gen.append(self.parent[0][0])
                    break
                i+=1
            if self.solved == False:                
                self.fit_gen.append(self.parent[0][0])
                self.evaluations += SIZE
                self.generations += SIZE
        else:
            mutated_string = self.mutate()
            if self.no_mut_flag == True:
                self.no_mut_flag = False
            else:
                fitness, solved = self.problem.evaluate(mutated_string)
                if fitness>=self.parent[0][0]:
                    self.parent = [(fitness, solved), mutated_string]
                if solved:
                    self.solved = True
            self.fit_gen.append(self.parent[0][0])
            self.generations += 1
            self.evaluations += 1
    
    def mutate(self):
        alpha = self.power_dist.rvs(0)/self.problem_size
        l = np.random.binomial(self.problem_size, alpha)
        if l == 0:
            self.no_mut_flag = True
            return self.parent[1]
        mut_indexes = np.random.choice(self.problem_size, size = l,
                                       replace=False)
        mut_int = sum([2**int(i) for i in mut_indexes])
        mutated_string = mut_int^self.parent[1]
        return mutated_string
    
    def mutate2(self, l):
        mut_indexes = np.random.choice(self.problem_size, size = l,
                                       replace=False)
        mut_int = sum([2**int(i) for i in mut_indexes])
        mutated_string = mut_int^self.parent[1]
        return mutated_string


###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

class OnePlusLambdaCommaLambda:
    def __init__(self, problem, problem_size, mutation_probability, 
                 offspring_size, crossover_probability, not_used_1, 
                 not_used_2, not_used_3):
        self.problem = problem
        self.problem_size = problem_size
        self.offspring_size = offspring_size
        self.mutation_probability = mutation_probability
        self.crossover_probability = crossover_probability
        self.bit_string = random.randint(0,2**problem_size-1)
        self.solved = False
        self.evaluations = 0
        self.generations = 0
        self.fit_gen = []
        self.lambda_gen = []
        self.mut_prob_gen = []
        self.parent = [self.problem.evaluate(self.bit_string), 
                       self.bit_string]
        
    def __next__(self):
        offspring = []
        self.mut_prob_gen.append(self.mutation_probability)
        self.lambda_gen.append(round(self.offspring_size))
        l = np.random.binomial(self.problem_size, self.mutation_probability)
        if l > 0:
            for i in range(round(self.offspring_size)):
                mutated_string = self.mutate(l)
                offspring.append((self.problem.evaluate(mutated_string), 
                                  mutated_string))
            fittest_mut = self.select_1(offspring)
            # offspring = []
            for i in range(round(self.offspring_size)):
                cross_string = self.crossover(fittest_mut)
                offspring.append((self.problem.evaluate(cross_string), 
                                  cross_string))
        self.evaluations += 2*round(self.offspring_size)
        self.select_2(offspring)
        self.generations += 1
        
    def mutate(self, l):
        mut_indexes = np.random.choice(self.problem_size, size = l,
                                       replace=False)
        mut_int = sum([2**int(i) for i in mut_indexes])
        mutated_string = mut_int^self.parent[1]
        return mutated_string
        
    def select_1(self, offspring):
        # eval_fittest = tuple - (fitness_value, problem_solved)
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        # fittest_offspring = list - [offspring_bit_strings]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        # fittest = bit_string
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        return fittest

    def crossover(self, second_parent):
        p_c = [1 - self.crossover_probability, self.crossover_probability]
        bit_array = np.random.choice([False, True], self.problem_size, p = p_c)
        first_parent = format(self.parent[1], '0'+str(self.problem_size)+'b')
        second_parent = format(second_parent, '0'+str(self.problem_size)+'b')
        cross_list = [second_parent[i] if bit_array[i] else first_parent[i] 
                      for i in range(self.problem_size)]
        return int(''.join(cross_list), 2)
    
    def select_2(self, offspring):
        offspring = [child for child in offspring if 
                     child[1] != self.parent[1]]
        if len(offspring) == 0:
            self.s = 0
            self.fit_gen.append(self.parent[0][0])
            return
        # eval_fittest = tuple - (fitness_value, problem_solved)
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        # fitter_offspring = list - [offspring_bit_strings]
        fitter_offspring = [child[1] for child in offspring if 
                             child[0][0] > self.parent[0][0]]
        self.s = len(fitter_offspring)
        # fittest_offspring = list - [offspring_bit_strings]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        # fittest = bit_string
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        if eval_fittest[0] >= self.parent[0][0]:
            self.parent = [eval_fittest, 
                           int(fittest)]
            self.bit_string = fittest
            self.fit_gen.append(eval_fittest[0])
        else:
            self.fit_gen.append(self.parent[0][0])
        if eval_fittest[1]:
            self.solved = True

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################


class OnePlusLambdaCommaLambdaJUMP:
    def __init__(self, problem, problem_size, mutation_probability, 
                 offspring_size, crossover_probability, not_used_1, 
                 not_used_2, not_used_3):
        self.problem = problem
        self.problem_size = problem_size
        self.offspring_size = offspring_size
        self.mutation_probability = mutation_probability
        self.crossover_probability = crossover_probability
        self.bit_string = random.randint(0,2**problem_size-1)
        self.solved = False
        self.evaluations = 0
        self.generations = 0
        self.fit_gen = []
        self.lambda_gen = []
        self.mut_prob_gen = []
        self.parent = [self.problem.evaluate(self.bit_string), 
                       self.bit_string]
        
    def __next__(self):
        offspring = []
        self.mut_prob_gen.append(self.mutation_probability)
        self.lambda_gen.append(round(self.offspring_size))
        l = np.random.binomial(self.problem_size, self.mutation_probability)
        if self.problem_size == self.parent[0][0]:
            if l < self.problem.jump_size:
                self.evaluations += 2*round(self.offspring_size)
            else:
                for i in range(round(self.offspring_size)):
                    mutated_string = self.mutate(l)
                    offspring.append((self.problem.evaluate(mutated_string), 
                                      mutated_string))
                    self.evaluations += 1
                fittest_mut = self.select_1(offspring)
                if (2**self.problem_size)-1 != fittest_mut|self.parent[1]:
                    self.evaluations += round(self.offspring_size)
                else:
                    for i in range(round(self.offspring_size)):
                        cross_string = self.crossover(fittest_mut)
                        offspring.append((self.problem.evaluate(cross_string), 
                                          cross_string))
                    self.evaluations += round(self.offspring_size)
                    self.select_2(offspring)
        else:
            for i in range(round(self.offspring_size)):
                mutated_string = self.mutate(l)
                offspring.append((self.problem.evaluate(mutated_string), 
                                  mutated_string))
            fittest_mut = self.select_1(offspring)
            # offspring = []
            for i in range(round(self.offspring_size)):
                cross_string = self.crossover(fittest_mut)
                offspring.append((self.problem.evaluate(cross_string), 
                                  cross_string))
            self.select_2(offspring)
            self.evaluations += 2*round(self.offspring_size)
        self.generations += 1
        
    def mutate(self, l):
        mut_indexes = np.random.choice(self.problem_size, size = l,
                                       replace=False)
        mut_int = sum([2**int(i) for i in mut_indexes])
        mutated_string = mut_int^self.parent[1]
        return mutated_string
        
    def select_1(self, offspring):
        # eval_fittest = tuple - (fitness_value, problem_solved)
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        # fittest_offspring = list - [offspring_bit_strings]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        # fittest = bit_string
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        return fittest

    def crossover(self, second_parent):
        p_c = [1 - self.crossover_probability, self.crossover_probability]
        bit_array = np.random.choice([False, True], self.problem_size, p = p_c)
        first_parent = format(self.parent[1], '0'+str(self.problem_size)+'b')
        second_parent = format(second_parent, '0'+str(self.problem_size)+'b')
        cross_list = [second_parent[i] if bit_array[i] else first_parent[i] 
                      for i in range(self.problem_size)]
        return int(''.join(cross_list), 2)
    
    def select_2(self, offspring):
        offspring = [child for child in offspring if 
                     child[1] != self.parent[1]]
        if len(offspring) == 0:
            self.s = 0
            self.fit_gen.append(self.parent[0][0])
            return
        # eval_fittest = tuple - (fitness_value, problem_solved)
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        # fitter_offspring = list - [offspring_bit_strings]
        fitter_offspring = [child[1] for child in offspring if 
                             child[0][0] > self.parent[0][0]]
        self.s = len(fitter_offspring)
        # fittest_offspring = list - [offspring_bit_strings]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        # fittest = bit_string
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        if eval_fittest[0] >= self.parent[0][0]:
            self.parent = [eval_fittest, 
                           int(fittest)]
            self.bit_string = fittest
            self.fit_gen.append(eval_fittest[0])
        else:
            self.fit_gen.append(self.parent[0][0])
        if eval_fittest[1]:
            self.solved = True

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################


class OnePlusLambdaCommaLambdaSA:
    def __init__(self, problem, problem_size, not_used_0, 
                 offspring_size, crossover_rate, not_used_2, 
                 offspring_update_factor, not_used_4):
        self.problem = problem
        self.problem_size = problem_size
        self.offspring_size = 1
        self.offspring_size_max = min(offspring_size, problem_size)
        self.offspring_update_factor = offspring_update_factor
        self.mutation_probability = self.offspring_size / self.problem_size
        self.crossover_rate = crossover_rate
        self.crossover_probability = min(1, crossover_rate / self.offspring_size)
        self.bit_string = random.randint(0,2**problem_size-1)
        self.solved = False
        self.evaluations = 0
        self.generations = 0
        self.fit_gen = []
        self.lambda_gen = []
        self.mut_prob_gen = []
        self.parent = [self.problem.evaluate(self.bit_string), 
                       self.bit_string]
        
    def __next__(self):
        offspring = []
        self.mut_prob_gen.append(self.mutation_probability)
        self.lambda_gen.append(round(self.offspring_size))
        l = np.random.binomial(self.problem_size, self.mutation_probability)
        if l > 0:
            for i in range(round(self.offspring_size)):
                mutated_string = self.mutate(l)
                offspring.append((self.problem.evaluate(mutated_string), 
                                  mutated_string))
            fittest_mut = self.select_1(offspring)
            # offspring = []
            for i in range(round(self.offspring_size)):
                cross_string = self.crossover(fittest_mut)
                offspring.append((self.problem.evaluate(cross_string), 
                                  cross_string))
            self.select_2(offspring)
        else:
            self.s = 0
        self.evaluations += 2*round(self.offspring_size)
        self.generations += 1
        self.update()
        
    def mutate(self, l):
        mut_indexes = np.random.choice(self.problem_size, size = l,
                                       replace=False)
        mut_int = sum([2**int(i) for i in mut_indexes])
        mutated_string = mut_int^self.parent[1]
        return mutated_string
        
    def select_1(self, offspring):
        # eval_fittest = tuple - (fitness_value, problem_solved)
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        # fittest_offspring = list - [offspring_bit_strings]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        # fittest = bit_string
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        return fittest

    def crossover(self, second_parent):
        p_c = [1 - self.crossover_probability, self.crossover_probability]
        bit_array = np.random.choice([False, True], self.problem_size, p = p_c)
        first_parent = format(self.parent[1], '0'+str(self.problem_size)+'b')
        second_parent = format(second_parent, '0'+str(self.problem_size)+'b')
        cross_list = [second_parent[i] if bit_array[i] else first_parent[i] 
                      for i in range(self.problem_size)]
        return int(''.join(cross_list), 2)
    
    def select_2(self, offspring):
        offspring = [child for child in offspring if 
                     child[1] != self.parent[1]]
        if len(offspring) == 0:
            self.s = 0
            self.fit_gen.append(self.parent[0][0])
            return
        # eval_fittest = tuple - (fitness_value, problem_solved)
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        # fitter_offspring = list - [offspring_bit_strings]
        fitter_offspring = [child[1] for child in offspring if 
                             child[0][0] > self.parent[0][0]]
        self.s = len(fitter_offspring)
        # fittest_offspring = list - [offspring_bit_strings]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        # fittest = bit_string
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        if eval_fittest[0] >= self.parent[0][0]:
            self.parent = [eval_fittest, 
                           int(fittest)]
            self.bit_string = fittest
            self.fit_gen.append(eval_fittest[0])
        else:
            self.fit_gen.append(self.parent[0][0])
        if eval_fittest[1]:
            self.solved = True
    
    def update(self):
        if self.s > 0:
            self.offspring_size /= self.offspring_update_factor
        else:
            self.offspring_size *= math.pow(self.offspring_update_factor, 1/4)
        self.offspring_size = max(self.offspring_size, 1)
        self.offspring_size = min(self.offspring_size, self.offspring_size_max)
        self.mutation_probability = self.offspring_size / self.problem_size
        self.crossover_probability = min(1, self.crossover_rate / self.offspring_size)

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################


class OnePlusLambdaCommaLambdaSAJUMP:
    def __init__(self, problem, problem_size, not_used_0, 
                 offspring_size, crossover_rate, not_used_2, 
                 offspring_update_factor, not_used_4):
        self.problem = problem
        self.problem_size = problem_size
        self.offspring_size = 1
        self.offspring_size_max = min(offspring_size, problem_size)
        self.offspring_update_factor = offspring_update_factor
        self.mutation_probability = self.offspring_size / self.problem_size
        self.crossover_rate = crossover_rate
        self.crossover_probability = min(1, crossover_rate / self.offspring_size)
        self.bit_string = random.randint(0,2**problem_size-1)
        self.solved = False
        self.evaluations = 0
        self.generations = 0
        self.fit_gen = []
        self.lambda_gen = []
        self.mut_prob_gen = []
        self.parent = [self.problem.evaluate(self.bit_string), 
                       self.bit_string]
        
    def __next__(self):
        offspring = []
        self.mut_prob_gen.append(self.mutation_probability)
        self.lambda_gen.append(round(self.offspring_size))
        l = np.random.binomial(self.problem_size, self.mutation_probability)
        if (self.problem_size == self.parent[0][0] and 
            round(self.offspring_size) == self.problem_size):
            self.crossover2()
            self.s = 0
        elif (self.problem_size == self.parent[0][0]):
            if l < self.problem.jump_size:
                self.s = 0
            else:
                for i in range(round(self.offspring_size)):
                    mutated_string = self.mutate(l)
                    offspring.append((self.problem.evaluate(mutated_string), 
                                      mutated_string))
                fittest_mut = self.select_1(offspring)
                if (2**self.problem_size)-1 == fittest_mut|self.parent[1]:
                    for i in range(round(self.offspring_size)):
                        cross_string = self.crossover(fittest_mut)
                        offspring.append((self.problem.evaluate(cross_string), 
                                          cross_string))
                    self.select_2(offspring)
                else:
                    self.s = 0
        else:
            if l > 0:
                for i in range(round(self.offspring_size)):
                    mutated_string = self.mutate(l)
                    offspring.append((self.problem.evaluate(mutated_string), 
                                      mutated_string))
                fittest_mut = self.select_1(offspring)
                # offspring = []
                for i in range(round(self.offspring_size)):
                    cross_string = self.crossover(fittest_mut)
                    offspring.append((self.problem.evaluate(cross_string), 
                                      cross_string))
                self.select_2(offspring)
            else:
                self.s = 0
        self.evaluations += 2*round(self.offspring_size)
        self.generations += 1
        self.update()
        
    def mutate(self, l):
        mut_indexes = np.random.choice(self.problem_size, size = l,
                                       replace=False)
        mut_int = sum([2**int(i) for i in mut_indexes])
        mutated_string = mut_int^self.parent[1]
        return mutated_string
        
    def select_1(self, offspring):
        # eval_fittest = tuple - (fitness_value, problem_solved)
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        # fittest_offspring = list - [offspring_bit_strings]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        # fittest = bit_string
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        return fittest

    def crossover(self, second_parent):
        p_c = [1 - self.crossover_probability, self.crossover_probability]
        bit_array = np.random.choice([False, True], self.problem_size, p = p_c)
        first_parent = format(self.parent[1], '0'+str(self.problem_size)+'b')
        second_parent = format(second_parent, '0'+str(self.problem_size)+'b')
        cross_list = [second_parent[i] if bit_array[i] else first_parent[i] 
                      for i in range(self.problem_size)]
        return int(''.join(cross_list), 2)
    
    def crossover2(self):
        elles = np.random.binomial(self.problem_size, self.crossover_probability, self.problem_size)
        elles = elles[np.where(elles == self.problem.jump_size)]
        if len(elles)==0:
            return
        else:
            for elle in elles:
                mut_indexes = np.random.choice(self.problem_size, size = elle,
                                               replace=False)
                mut_int = sum([2**int(i) for i in mut_indexes])
                mutated_string = mut_int^self.parent[1]
                eval_fittest = self.problem.evaluate(mutated_string)
                if eval_fittest[1]:            
                    self.solved = True
            return
    
    def select_2(self, offspring):
        offspring = [child for child in offspring if 
                     child[1] != self.parent[1]]
        if len(offspring) == 0:
            self.s = 0
            self.fit_gen.append(self.parent[0][0])
            return
        # eval_fittest = tuple - (fitness_value, problem_solved)
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        # fitter_offspring = list - [offspring_bit_strings]
        fitter_offspring = [child[1] for child in offspring if 
                             child[0][0] > self.parent[0][0]]
        self.s = len(fitter_offspring)
        # fittest_offspring = list - [offspring_bit_strings]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        # fittest = bit_string
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        if eval_fittest[0] >= self.parent[0][0]:
            self.parent = [eval_fittest, 
                           int(fittest)]
            self.bit_string = fittest
            self.fit_gen.append(eval_fittest[0])
        else:
            self.fit_gen.append(self.parent[0][0])
        if eval_fittest[1]:
            self.solved = True
    
    def update(self):
        if self.s > 0:
            self.offspring_size /= self.offspring_update_factor
        else:
            self.offspring_size *= math.pow(self.offspring_update_factor, 1/4)
        self.offspring_size = max(self.offspring_size, 1)
        self.offspring_size = min(self.offspring_size, self.offspring_size_max)
        self.mutation_probability = self.offspring_size / self.problem_size
        self.crossover_probability = min(1, self.crossover_rate / self.offspring_size)

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################


class OnePlusLambdaCommaLambdaSAReset:
    def __init__(self, problem, problem_size, not_used_0, 
                 offspring_size, crossover_rate, not_used_2, 
                 offspring_update_factor, not_used_4):
        self.problem = problem
        self.problem_size = problem_size
        self.offspring_size = 1
        self.offspring_size_max = min(offspring_size, problem_size)
        self.offspring_update_factor = offspring_update_factor
        self.mutation_probability = self.offspring_size / self.problem_size
        self.crossover_rate = crossover_rate
        if crossover_rate >= 1:
            self.crossover_probability = min(1, crossover_rate / self.offspring_size)
        else:
            self.crossover_probability = crossover_rate
        self.bit_string = random.randint(0,2**problem_size-1)
        self.solved = False
        self.evaluations = 0
        self.generations = 0
        self.fit_gen = []
        self.lambda_gen = []
        self.mut_prob_gen = []
        self.parent = [self.problem.evaluate(self.bit_string), 
                       self.bit_string]
        
    def __next__(self):
        offspring = []
        self.mut_prob_gen.append(self.mutation_probability)
        self.lambda_gen.append(round(self.offspring_size))
        l = np.random.binomial(self.problem_size, self.mutation_probability)
        if l > 0:
            for i in range(round(self.offspring_size)):
                mutated_string = self.mutate(l)
                offspring.append((self.problem.evaluate(mutated_string), 
                                  mutated_string))
            fittest_mut = self.select_1(offspring)
            # offspring = []
            for i in range(round(self.offspring_size)):
                cross_string = self.crossover(fittest_mut)
                offspring.append((self.problem.evaluate(cross_string), 
                                  cross_string))
            self.select_2(offspring)
        else:
            self.s = 0
        self.evaluations += 2*round(self.offspring_size)
        self.generations += 1
        self.update()
        
    def mutate(self, l):
        mut_indexes = np.random.choice(self.problem_size, size = l,
                                       replace=False)
        mut_int = sum([2**int(i) for i in mut_indexes])
        mutated_string = mut_int^self.parent[1]
        return mutated_string
        
    def select_1(self, offspring):
        # eval_fittest = tuple - (fitness_value, problem_solved)
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        # fittest_offspring = list - [offspring_bit_strings]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        # fittest := bit_string
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        return fittest

    def crossover(self, second_parent):
        p_c = [1 - self.crossover_probability, self.crossover_probability]
        bit_array = np.random.choice([False, True], self.problem_size, p = p_c)
        first_parent = format(self.parent[1], '0'+str(self.problem_size)+'b')
        second_parent = format(second_parent, '0'+str(self.problem_size)+'b')
        cross_list = [second_parent[i] if bit_array[i] else first_parent[i] 
                      for i in range(self.problem_size)]
        return int(''.join(cross_list), 2)
    
    def select_2(self, offspring):
        offspring = [child for child in offspring if 
                     child[1] != self.parent[1]]
        if len(offspring) == 0:
            self.s = 0
            self.fit_gen.append(self.parent[0][0])
            return
        # eval_fittest = tuple - (fitness_value, problem_solved)
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        # fitter_offspring = list - [offspring_bit_strings]
        fitter_offspring = [child[1] for child in offspring if 
                             child[0][0] > self.parent[0][0]]
        self.s = len(fitter_offspring)
        # fittest_offspring = list - [offspring_bit_strings]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        # fittest = bit_string
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        if eval_fittest[0] >= self.parent[0][0]:
            self.parent = [eval_fittest, 
                           int(fittest)]
            self.bit_string = fittest
            self.fit_gen.append(eval_fittest[0])
        else:
            self.fit_gen.append(self.parent[0][0])
        if eval_fittest[1]:
            self.solved = True
    
    def update(self):
        if self.s > 0:
            self.offspring_size /= self.offspring_update_factor
        elif self.offspring_size == self.offspring_size_max:
            self.offspring_size = 1
        else:
            self.offspring_size *= math.pow(self.offspring_update_factor, 1/4)
        self.offspring_size = max(self.offspring_size, 1)
        self.offspring_size = min(self.offspring_size, self.offspring_size_max)
        self.mutation_probability = self.offspring_size / self.problem_size
        if self.crossover_rate >= 1:
            self.crossover_probability = min(1, self.crossover_rate / self.offspring_size)

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################


class OnePlusLambdaCommaLambdaSAResetJUMP:
    def __init__(self, problem, problem_size, not_used_0, 
                 offspring_size, crossover_rate, not_used_2, 
                 offspring_update_factor, not_used_4):
        self.problem = problem
        self.problem_size = problem_size
        self.offspring_size = 1
        self.offspring_size_max = min(offspring_size, problem_size)
        self.offspring_update_factor = offspring_update_factor
        self.mutation_probability = self.offspring_size / self.problem_size
        self.crossover_rate = crossover_rate
        if crossover_rate >= 1:
            self.crossover_probability = min(1, crossover_rate / self.offspring_size)
        else:
            self.crossover_probability = crossover_rate
        self.bit_string = random.randint(0,2**problem_size-1)
        self.solved = False
        self.evaluations = 0
        self.generations = 0
        self.fit_gen = []
        self.lambda_gen = []
        self.mut_prob_gen = []
        self.parent = [self.problem.evaluate(self.bit_string), 
                       self.bit_string]
        
    def __next__(self):
        offspring = []
        self.mut_prob_gen.append(self.mutation_probability)
        self.lambda_gen.append(round(self.offspring_size))
        l = np.random.binomial(self.problem_size, self.mutation_probability)
        if (self.problem_size == self.parent[0][0] and 
            round(self.offspring_size) == self.problem_size):
            self.crossover2()
            self.s = 0
        elif (self.problem_size == self.parent[0][0]):
            if l < self.problem.jump_size:
                self.s = 0
            else:
                for i in range(round(self.offspring_size)):
                    mutated_string = self.mutate(l)
                    offspring.append((self.problem.evaluate(mutated_string), 
                                      mutated_string))
                fittest_mut = self.select_1(offspring)
                if (2**self.problem_size)-1 == fittest_mut|self.parent[1]:
                    for i in range(round(self.offspring_size)):
                        cross_string = self.crossover(fittest_mut)
                        offspring.append((self.problem.evaluate(cross_string), 
                                          cross_string))
                    self.select_2(offspring)
                else:
                    self.s = 0
        else:
            if l > 0:
                for i in range(round(self.offspring_size)):
                    mutated_string = self.mutate(l)
                    offspring.append((self.problem.evaluate(mutated_string), 
                                      mutated_string))
                fittest_mut = self.select_1(offspring)
                # offspring = []
                for i in range(round(self.offspring_size)):
                    cross_string = self.crossover(fittest_mut)
                    offspring.append((self.problem.evaluate(cross_string), 
                                      cross_string))
                self.select_2(offspring)
            else:
                self.s = 0
        self.evaluations += 2*round(self.offspring_size)
        self.generations += 1
        self.update()
        
    def mutate(self, l):
        mut_indexes = np.random.choice(self.problem_size, size = l,
                                       replace=False)
        mut_int = sum([2**int(i) for i in mut_indexes])
        mutated_string = mut_int^self.parent[1]
        return mutated_string
        
    def select_1(self, offspring):
        # eval_fittest = tuple - (fitness_value, problem_solved)
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        # fittest_offspring = list - [offspring_bit_strings]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        # fittest = bit_string
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        return fittest

    def crossover(self, second_parent):
        p_c = [1 - self.crossover_probability, self.crossover_probability]
        bit_array = np.random.choice([False, True], self.problem_size, p = p_c)
        first_parent = format(self.parent[1], '0'+str(self.problem_size)+'b')
        second_parent = format(second_parent, '0'+str(self.problem_size)+'b')
        cross_list = [second_parent[i] if bit_array[i] else first_parent[i] 
                      for i in range(self.problem_size)]
        return int(''.join(cross_list), 2)
    
    def crossover2(self):
        elles = np.random.binomial(self.problem_size, self.crossover_probability, self.problem_size)
        elles = elles[np.where(elles == self.problem.jump_size)]
        if len(elles)==0:
            return
        else:
            for elle in elles:
                mut_indexes = np.random.choice(self.problem_size, size = elle,
                                               replace=False)
                mut_int = sum([2**int(i) for i in mut_indexes])
                mutated_string = mut_int^self.parent[1]
                eval_fittest = self.problem.evaluate(mutated_string)
                if eval_fittest[1]:            
                    self.solved = True
            return
    
    def select_2(self, offspring):
        offspring = [child for child in offspring if 
                     child[1] != self.parent[1]]
        if len(offspring) == 0:
            self.s = 0
            self.fit_gen.append(self.parent[0][0])
            return
        # eval_fittest = tuple - (fitness_value, problem_solved)
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        # fitter_offspring = list - [offspring_bit_strings]
        fitter_offspring = [child[1] for child in offspring if 
                             child[0][0] > self.parent[0][0]]
        self.s = len(fitter_offspring)
        # fittest_offspring = list - [offspring_bit_strings]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        # fittest = bit_string
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        if eval_fittest[0] >= self.parent[0][0]:
            self.parent = [eval_fittest, 
                           int(fittest)]
            self.bit_string = fittest
            self.fit_gen.append(eval_fittest[0])
        else:
            self.fit_gen.append(self.parent[0][0])
        if eval_fittest[1]:
            self.solved = True
    
    def update(self):
        if self.s > 0:
            self.offspring_size /= self.offspring_update_factor
        elif self.offspring_size == self.offspring_size_max:
            self.offspring_size = 1
        else:
            self.offspring_size *= math.pow(self.offspring_update_factor, 1/4)
        self.offspring_size = max(self.offspring_size, 1)
        self.offspring_size = min(self.offspring_size, self.offspring_size_max)
        self.mutation_probability = self.offspring_size / self.problem_size
        if self.crossover_rate >= 1:
            self.crossover_probability = min(1, self.crossover_rate / self.offspring_size)
        

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

class FastOnePlusLambdaCommaLambda:
    def __init__(self, problem, problem_size, not_used_0, 
                 not_used_1, not_used_2, not_used_3, 
                 not_used_4, not_used_5):
        self.problem = problem
        self.problem_size = problem_size        
        self.bit_string = random.randint(0,2**problem_size-1)
        self.solved = False
        self.evaluations = 0
        self.generations = 0
        self.fit_gen = []
        self.lambda_gen = []
        self.mut_prob_gen = []
        self.parent = [self.problem.evaluate(self.bit_string), 
                       self.bit_string]
        B = 2.5
        u = math.ceil(math.log(self.problem_size)**2)
        u = math.ceil(self.problem_size/2)
        x = np.arange(1, u+1, dtype='float')
        pmf = 1/x**B
        pmf /= pmf.sum()
        # print(pmf, sum(pmf))
        self.power_dist = stats.rv_discrete(values=(range(1, u+1), pmf))
        
    def __next__(self):
        offspring = []
        
        self.offspring_size = self.power_dist.rvs(0)
        self.mutation_probability = self.offspring_size / self.problem_size
        self.crossover_probability = 1 / self.offspring_size
        
        self.mut_prob_gen.append(self.mutation_probability)
        self.lambda_gen.append(round(self.offspring_size))
        l = np.random.binomial(self.problem_size, self.mutation_probability)
        if l > 0:
            for i in range(round(self.offspring_size)):
                mutated_string = self.mutate(l)
                offspring.append((self.problem.evaluate(mutated_string), 
                                  mutated_string))
            fittest_mut = self.select_1(offspring)
            # offspring = []
            for i in range(round(self.offspring_size)):
                cross_string = self.crossover(fittest_mut)
                offspring.append((self.problem.evaluate(cross_string), 
                                  cross_string))
        self.evaluations += 2*round(self.offspring_size)
        self.select_2(offspring)
        self.generations += 1
        
    def mutate(self, l):
        mut_indexes = np.random.choice(self.problem_size, size = l,
                                       replace=False)
        mut_int = sum([2**int(i) for i in mut_indexes])
        mutated_string = mut_int^self.parent[1]
        return mutated_string
        
    def select_1(self, offspring):
        # eval_fittest = tuple - (fitness_value, problem_solved)
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        # fittest_offspring = list - [offspring_bit_strings]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        # fittest = bit_string
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        return fittest

    def crossover(self, second_parent):
        p_c = [1 - self.crossover_probability, self.crossover_probability]
        bit_array = np.random.choice([False, True], self.problem_size, p = p_c)
        first_parent = format(self.parent[1], '0'+str(self.problem_size)+'b')
        second_parent = format(second_parent, '0'+str(self.problem_size)+'b')
        cross_list = [second_parent[i] if bit_array[i] else first_parent[i] 
                      for i in range(self.problem_size)]
        return int(''.join(cross_list), 2)
    
    def select_2(self, offspring):
        offspring = [child for child in offspring if 
                     child[1] != self.parent[1]]
        if len(offspring) == 0:
            self.s = 0
            self.fit_gen.append(self.parent[0][0])
            return
        # eval_fittest = tuple - (fitness_value, problem_solved)
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        # fitter_offspring = list - [offspring_bit_strings]
        fitter_offspring = [child[1] for child in offspring if 
                             child[0][0] > self.parent[0][0]]
        self.s = len(fitter_offspring)
        # fittest_offspring = list - [offspring_bit_strings]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        # fittest = bit_string
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        if eval_fittest[0] >= self.parent[0][0]:
            self.parent = [eval_fittest, 
                           int(fittest)]
            self.bit_string = fittest
            self.fit_gen.append(eval_fittest[0])
        else:
            self.fit_gen.append(self.parent[0][0])
        if eval_fittest[1]:
            self.solved = True
            
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

class FastOnePlusLambdaCommaLambdaJUMP:
    def __init__(self, problem, problem_size, not_used_0, 
                 not_used_1, not_used_2, not_used_3, 
                 not_used_4, not_used_5):
        self.problem = problem
        self.problem_size = problem_size        
        self.bit_string = random.randint(0,2**problem_size-1)
        self.solved = False
        self.evaluations = 0
        self.generations = 0
        self.fit_gen = []
        self.lambda_gen = []
        self.mut_prob_gen = []
        self.parent = [self.problem.evaluate(self.bit_string), 
                       self.bit_string]
        B = 2.5
        # u = math.ceil(math.log(self.problem_size)**2)
        u = math.ceil(self.problem_size/2)
        x = np.arange(1, u+1, dtype='float')
        pmf = 1/x**B
        pmf /= pmf.sum()
        self.power_dist = stats.rv_discrete(values=(range(1, u+1), pmf))
        
    def __next__(self):
        offspring = []
        
        self.offspring_size = self.power_dist.rvs(0)
        self.mutation_probability = self.offspring_size / self.problem_size
        self.crossover_probability = 1 / self.offspring_size
        
        self.mut_prob_gen.append(self.mutation_probability)
        self.lambda_gen.append(round(self.offspring_size))
        l = np.random.binomial(self.problem_size, self.mutation_probability)
        if self.problem_size == self.parent[0][0]:
            if l < self.problem.jump_size:
                self.evaluations += 2*round(self.offspring_size)
            else:
                for i in range(round(self.offspring_size)):
                    mutated_string = self.mutate(l)
                    offspring.append((self.problem.evaluate(mutated_string), 
                                      mutated_string))
                    self.evaluations += 1
                fittest_mut = self.select_1(offspring)
                if (2**self.problem_size)-1 != fittest_mut|self.parent[1]:
                    self.evaluations += round(self.offspring_size)
                else:
                    for i in range(round(self.offspring_size)):
                        cross_string = self.crossover(fittest_mut)
                        offspring.append((self.problem.evaluate(cross_string), 
                                          cross_string))
                    self.evaluations += round(self.offspring_size)
                    self.select_2(offspring)
        else:
            for i in range(round(self.offspring_size)):
                mutated_string = self.mutate(l)
                offspring.append((self.problem.evaluate(mutated_string), 
                                  mutated_string))
            fittest_mut = self.select_1(offspring)
            # offspring = []
            for i in range(round(self.offspring_size)):
                cross_string = self.crossover(fittest_mut)
                offspring.append((self.problem.evaluate(cross_string), 
                                  cross_string))
            self.select_2(offspring)
            self.evaluations += 2*round(self.offspring_size)
        self.generations += 1
        
    def mutate(self, l):
        mut_indexes = np.random.choice(self.problem_size, size = l,
                                       replace=False)
        mut_int = sum([2**int(i) for i in mut_indexes])
        mutated_string = mut_int^self.parent[1]
        return mutated_string
        
    def select_1(self, offspring):
        # eval_fittest = tuple - (fitness_value, problem_solved)
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        # fittest_offspring = list - [offspring_bit_strings]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        # fittest = bit_string
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        return fittest

    def crossover(self, second_parent):
        p_c = [1 - self.crossover_probability, self.crossover_probability]
        bit_array = np.random.choice([False, True], self.problem_size, p = p_c)
        first_parent = format(self.parent[1], '0'+str(self.problem_size)+'b')
        second_parent = format(second_parent, '0'+str(self.problem_size)+'b')
        cross_list = [second_parent[i] if bit_array[i] else first_parent[i] 
                      for i in range(self.problem_size)]
        return int(''.join(cross_list), 2)
    
    def select_2(self, offspring):
        offspring = [child for child in offspring if 
                     child[1] != self.parent[1]]
        if len(offspring) == 0:
            self.s = 0
            self.fit_gen.append(self.parent[0][0])
            return
        # eval_fittest = tuple - (fitness_value, problem_solved)
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        # fitter_offspring = list - [offspring_bit_strings]
        fitter_offspring = [child[1] for child in offspring if 
                             child[0][0] > self.parent[0][0]]
        self.s = len(fitter_offspring)
        # fittest_offspring = list - [offspring_bit_strings]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        # fittest = bit_string
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        if eval_fittest[0] >= self.parent[0][0]:
            self.parent = [eval_fittest, 
                           int(fittest)]
            self.bit_string = fittest
            self.fit_gen.append(eval_fittest[0])
        else:
            self.fit_gen.append(self.parent[0][0])
        if eval_fittest[1]:
            self.solved = True
        

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

class DoubleFastOnePlusLambdaCommaLambda:
    def __init__(self, problem, problem_size, not_used_0, 
                 not_used_1, not_used_2, not_used_3, 
                 not_used_4, not_used_5):
        self.problem = problem
        self.problem_size = problem_size        
        self.bit_string = random.randint(0,2**problem_size-1)
        self.solved = False
        self.evaluations = 0
        self.generations = 0
        self.fit_gen = []
        self.lambda_gen = []
        self.mut_prob_gen = []
        self.parent = [self.problem.evaluate(self.bit_string), 
                       self.bit_string]
        Bs = 1
        us = self.problem_size
        x = np.arange(1, us+1, dtype='float')
        pmf = 1/x**Bs
        pmf /= pmf.sum()
        self.power_dist_s = stats.rv_discrete(values=(range(1, us+1), pmf))
        
        Bl = 2
        try:
            ul = min(math.ceil(5**(self.problem_size/10)), 1000000)
        except OverflowError:
            ul = 1000000
        x = np.arange(1, ul+1, dtype='float')
        pmf = 1/x**Bl
        pmf /= pmf.sum()
        self.power_dist_l = stats.rv_discrete(values=(range(1, ul+1), pmf))
        
    def __next__(self):
        offspring = []
        
        self.offspring_size = self.power_dist_l.rvs(0)
        s = self.power_dist_s.rvs(0)
        self.mutation_probability = math.sqrt(s / self.problem_size)
        self.crossover_probability = math.sqrt(s / self.problem_size)
        
        self.mut_prob_gen.append(self.mutation_probability)
        self.lambda_gen.append(round(self.offspring_size))
        l = np.random.binomial(self.problem_size, self.mutation_probability)
        if l > 0:
            # mutated_strings = [self.mutate(l) for i in range(round(self.offspring_size))]
            # offspring = [(self.problem.evaluate(mutated_string), mutated_string) for mutated_string in mutated_strings]
            # fittest_mut, eval_fittest = self.select_1(offspring)
            # offspring = [(eval_fittest, fittest_mut)]
            # cross_strings = [self.crossover(fittest_mut) for i in range(round(self.offspring_size))]
            # offspring.extend([(self.problem.evaluate(cross_string), cross_string) for cross_string in cross_strings])
            for i in range(round(self.offspring_size)):
                mutated_string = self.mutate(l)
                offspring.append((self.problem.evaluate(mutated_string), 
                                  mutated_string))
            fittest_mut, eval_fittest = self.select_1(offspring)
            offspring = [(eval_fittest, fittest_mut)]
            for i in range(round(self.offspring_size)):
                cross_string = self.crossover(fittest_mut)
                offspring.append((self.problem.evaluate(cross_string), 
                                  cross_string))
        self.evaluations += 2*round(self.offspring_size)
        self.select_2(offspring)
        self.generations += 1
        
    def mutate(self, l):
        mut_indexes = np.random.choice(self.problem_size, size = l,
                                       replace=False)
        mut_int = sum([2**int(i) for i in mut_indexes])
        mutated_string = mut_int^self.parent[1]
        return mutated_string
        
    def select_1(self, offspring):
        # eval_fittest = tuple - (fitness_value, problem_solved)
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        # fittest_offspring = list - [offspring_bit_strings]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        # fittest = bit_string
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        return fittest, eval_fittest

    def crossover(self, second_parent):
        p_c = [1 - self.crossover_probability, self.crossover_probability]
        bit_array = np.random.choice([False, True], self.problem_size, p = p_c)
        first_parent = format(self.parent[1], '0'+str(self.problem_size)+'b')
        second_parent = format(second_parent, '0'+str(self.problem_size)+'b')
        cross_list = [second_parent[i] if bit_array[i] else first_parent[i] 
                      for i in range(self.problem_size)]
        return int(''.join(cross_list), 2)
    
    def select_2(self, offspring):
        offspring = [child for child in offspring if 
                     child[1] != self.parent[1]]
        if len(offspring) == 0:
            self.s = 0
            self.fit_gen.append(self.parent[0][0])
            return
        # eval_fittest = tuple - (fitness_value, problem_solved)
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        # fitter_offspring = list - [offspring_bit_strings]
        fitter_offspring = [child[1] for child in offspring if 
                             child[0][0] > self.parent[0][0]]
        self.s = len(fitter_offspring)
        # fittest_offspring = list - [offspring_bit_strings]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        # fittest = bit_string
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        if eval_fittest[0] >= self.parent[0][0]:
            self.parent = [eval_fittest, 
                           int(fittest)]
            self.bit_string = fittest
            self.fit_gen.append(eval_fittest[0])
        else:
            self.fit_gen.append(self.parent[0][0])
        if eval_fittest[1]:
            self.solved = True
            
            
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

class DoubleFastOnePlusLambdaCommaLambdaJUMP:
    def __init__(self, problem, problem_size, not_used_0, 
                 not_used_1, not_used_2, not_used_3, 
                 not_used_4, not_used_5):
        self.problem = problem
        self.problem_size = problem_size        
        self.bit_string = random.randint(0,2**problem_size-1)
        self.solved = False
        self.evaluations = 0
        self.generations = 0
        self.fit_gen = []
        self.lambda_gen = []
        self.mut_prob_gen = []
        self.parent = [self.problem.evaluate(self.bit_string), 
                       self.bit_string]
        Bs = 1
        us = self.problem_size
        x = np.arange(1, us+1, dtype='float')
        pmf = 1/x**Bs
        pmf /= pmf.sum()
        self.power_dist_s = stats.rv_discrete(values=(range(1, us+1), pmf))
        
        Bl = 2
        try:
            ul = min(math.ceil(5**(self.problem_size/10)), 1000000)
        except OverflowError:
            ul = 1000000
        x = np.arange(1, ul+1, dtype='float')
        pmf = 1/x**Bl
        pmf /= pmf.sum()
        self.power_dist_l = stats.rv_discrete(values=(range(1, ul+1), pmf))
        
    def __next__(self):
        offspring = []
        
        self.offspring_size = self.power_dist_l.rvs(0)
        s = self.power_dist_s.rvs(0)
        self.mutation_probability = math.sqrt(s / self.problem_size)
        self.crossover_probability = math.sqrt(s / self.problem_size)
        
        self.mut_prob_gen.append(self.mutation_probability)
        self.lambda_gen.append(round(self.offspring_size))
        l = np.random.binomial(self.problem_size, self.mutation_probability)
        if self.problem_size == self.parent[0][0]:
            if l < self.problem.jump_size:
                self.evaluations += 2*round(self.offspring_size)
            else:
                for i in range(round(self.offspring_size)):
                    mutated_string = self.mutate(l)
                    offspring.append((self.problem.evaluate(mutated_string), 
                                      mutated_string))
                    self.evaluations += 1
                fittest_mut = self.select_1(offspring)
                if (2**self.problem_size)-1 != fittest_mut|self.parent[1]:
                    self.evaluations += round(self.offspring_size)
                else:
                    for i in range(round(self.offspring_size)):
                        cross_string = self.crossover(fittest_mut)
                        offspring.append((self.problem.evaluate(cross_string), 
                                          cross_string))
                    self.evaluations += round(self.offspring_size)
                    self.select_2(offspring)
        else:
            for i in range(round(self.offspring_size)):
                mutated_string = self.mutate(l)
                offspring.append((self.problem.evaluate(mutated_string), 
                                  mutated_string))
            fittest_mut = self.select_1(offspring)
            # offspring = []
            for i in range(round(self.offspring_size)):
                cross_string = self.crossover(fittest_mut)
                offspring.append((self.problem.evaluate(cross_string), 
                                  cross_string))
            self.select_2(offspring)
            self.evaluations += 2*round(self.offspring_size)
        self.generations += 1
        
    def mutate(self, l):
        mut_indexes = np.random.choice(self.problem_size, size = l,
                                       replace=False)
        mut_int = sum([2**int(i) for i in mut_indexes])
        mutated_string = mut_int^self.parent[1]
        return mutated_string
        
    def select_1(self, offspring):
        # eval_fittest = tuple - (fitness_value, problem_solved)
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        # fittest_offspring = list - [offspring_bit_strings]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        # fittest = bit_string
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        return fittest

    def crossover(self, second_parent):
        p_c = [1 - self.crossover_probability, self.crossover_probability]
        bit_array = np.random.choice([False, True], self.problem_size, p = p_c)
        first_parent = format(self.parent[1], '0'+str(self.problem_size)+'b')
        second_parent = format(second_parent, '0'+str(self.problem_size)+'b')
        cross_list = [second_parent[i] if bit_array[i] else first_parent[i] 
                      for i in range(self.problem_size)]
        return int(''.join(cross_list), 2)
    
    def select_2(self, offspring):
        offspring = [child for child in offspring if 
                     child[1] != self.parent[1]]
        if len(offspring) == 0:
            self.s = 0
            self.fit_gen.append(self.parent[0][0])
            return
        # eval_fittest = tuple - (fitness_value, problem_solved)
        eval_fittest = heapq.nlargest(1, offspring)[0][0]
        # fitter_offspring = list - [offspring_bit_strings]
        fitter_offspring = [child[1] for child in offspring if 
                             child[0][0] > self.parent[0][0]]
        self.s = len(fitter_offspring)
        # fittest_offspring = list - [offspring_bit_strings]
        fittest_offspring = [child[1] for child in offspring if 
                             child[0][0] == eval_fittest[0]]
        # fittest = bit_string
        fittest = np.random.choice(np.array(fittest_offspring, dtype='object'), 1)[0]
        if eval_fittest[0] >= self.parent[0][0]:
            self.parent = [eval_fittest, 
                           int(fittest)]
            self.bit_string = fittest
            self.fit_gen.append(eval_fittest[0])
        else:
            self.fit_gen.append(self.parent[0][0])
        if eval_fittest[1]:
            self.solved = True
