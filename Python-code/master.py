#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 13:00:35 2018

@author: mario_hevia
"""
# Input examples
# -t OneMax -n 100 -l 100 -r 500 -c 1 -a JA.OnePlusLambdaCommaLambdaSAReset -v -G 1.5 --seed 885480221
# -t Jump -n 40 -k 4 -p 0.1 -l 1 -r 500 -a JA.OnePlusLambdaJUMP -v --seed 792614162
# -r 500 -n 50 -l 1 -t WeightedNearestPeak -a JA.FastOnePlusLambda -v --extra [50,10,0],[40,9,0],[40,9,0],[40,9,0],[40,9,0],[40,9,0] --seed 2020

import numpy as np
import random
from utils.inputs import CommandLine
from utils.functions import *
import utils.journalalgorithms as JA
from datetime import date, datetime
from utils.outputs import Outputs


def execute_experiment():
    text_log = ''
    configuration = CommandLine()
    problem_string = (configuration.problem + '(' + 
                      str(configuration.problem_size) + ', ' + 
                      str(configuration.jump_size) + ')')
    if configuration.problem == 'NearestPeak' or configuration.problem == 'WeightedNearestPeak':
        problem_string = (configuration.problem + '(' + 
                          str(configuration.problem_size) + ', ' + 
                          str(configuration.jump_size) + ', ' + 
                          '"' + configuration.extra + '"' + ')')
    if configuration.problem == 'IsingSpinGlass':
        problem_string = (configuration.problem + '(' + 
                          str(configuration.problem_size) + ', ' + 
                          str(configuration.jump_size) + ', ' + 
                          '"IsingSpinGlass_pm_' + 
                          str(configuration.problem_size) + '_" + str((run-1)+100) + ".txt"' + ')')
    if configuration.problem == 'MaxSat':
        problem_string = (configuration.problem + '(' + 
                          str(configuration.problem_size) + ', ' + 
                          str(configuration.jump_size) + ', ' + 
                          '"maxsat_' + 
                          str(configuration.problem_size) + '_" + str((run-1)%200) + ".txt"' + ')')
    algorithm_string = (configuration.algorithm + '(' + 'problem,' +
                      str(configuration.problem_size) + ',' +
                      str(configuration.mut_prob) + ',' +
                      str(configuration.offspring_size) + ',' +
                      str(configuration.cross_prob) + ',' +
                      str(configuration.mut_update_factor) + ',' +
                      str(configuration.offspring_update_factor) + ',' +
                      str(configuration.success_ratio) + ')')
    
    text_log += 'Experiment configurations\n'
    text_log += ('Seed: ' + str(configuration.seed) +
                 '\nProblem: ' + str(configuration.problem) + '\nSize: ' + 
                str(configuration.problem_size) + '\tk: ' + 
                str(configuration.jump_size) + '\tExtra: ' + 
                str(configuration.extra) +
                '\nRuns: ' + str(configuration.num_runs) +
                '\nStop criteria: ' + str(configuration.stop_criteria) +
                '\nMax generations (if aplicable): ' + 
                str(configuration.max_generations) +
                '\nMax evaluations (if aplicable): ' + 
                str(configuration.max_evaluations) + '\nAlgorithm: ' + 
                str(configuration.algorithm) + '\nInitial mutation probability: ' +
                str(configuration.mut_prob) + '\nInitial offspring population size: ' +
                str(configuration.offspring_size) + '\nInitial crossover probability' +
                '(if aplicable): ' + str(configuration.cross_prob) + '\nMutation update' +
                'factor (if aplicable): ' + str(configuration.mut_update_factor) +
                '\nOffspring population size update factor (if aplicable): ' +
                str(configuration.offspring_update_factor) + 
                '\nSuccess ratio (if aplicable): ' +
                str(configuration.success_ratio) + '\n' +
                '\n------------------------------------------------------------------\n')
    
    if configuration.verbose:
        print(text_log)
    generations = []
    evaluations = []
    fitness = []
    lambdas = []
    for run in range(1, configuration.num_runs + 1):        
        np.random.seed(configuration.seed+run)
        random.seed(configuration.seed+run)
        problem = eval(problem_string)
        algorithm = eval(algorithm_string)
        if configuration.stop_criteria == 'solved':
            max_eval = 1000000000000
            while not algorithm.solved:
                next(algorithm)
                if (algorithm.evaluations > max_eval):
                    break
        elif configuration.stop_criteria == 'ngenerations':
            for i in range(configuration.max_generations):
                next(algorithm)
                if algorithm.solved:
                    break
        else:
            while algorithm.evaluations < configuration.max_evaluations:
                next(algorithm)
                if algorithm.solved:
                    break
        
        generations.append(algorithm.generations)
        evaluations.append(algorithm.evaluations)
        fitness.append(algorithm.fit_gen[-1])
        lambdas.append(algorithm.lambda_gen[-1])
        # fitness.append(algorithm.fit_gen)
        # lambdas.append(algorithm.lambda_gen)
        # mut_rates.append(algorithm.mut_prob_gen)
        
        
        text_log += ('Final results: ' + 
                    '{0:<4} {1:<4} {2:<5} {3:<7} {4:<6} {5:<7} {6:<2} {7} {8} {9} {10:<7} {11}'.format(
                            'Run:', run, 'Gens:', algorithm.generations, 'Evals:', 
                            algorithm.evaluations, 'λ:', algorithm.lambda_gen[-1], 
                            'p:', algorithm.mut_prob_gen[-1], 'Solved:', 
                            algorithm.solved) + '\n')
        if configuration.verbose:
            print('Final results: ' + 
                  '{0:<4} {1:<4} {2:<5} {3:<7} {4:<6} {5:<7} {6:<2} {7} {8} {9} {10:<7} {11}'.format(
                    'Run:', run, 'Gens:', algorithm.generations, 'Evals:', 
                    algorithm.evaluations, 'λ:', algorithm.lambda_gen[-1], 
                    'p:', algorithm.mut_prob_gen[-1], 'Solved:', 
                    algorithm.solved))
    text_log += '\n------------------------------------------------------------------\n'
    if configuration.verbose:
        print('\n------------------------------------------------------------'
              '------\n')
    
    avg_lambda = sum(lambdas)/len(lambdas)
    avg_fit = sum(fitness)/len(fitness)
    
    
    # Calculates average of generations and evaluations per run 
    avg_gen = sum(generations)/len(generations)
    avg_eval = sum(evaluations)/len(evaluations)
    
    results = {}
    results['Avg_generations'] = avg_gen
    results['Avg_evaluations'] = avg_eval
    results['Avg_fitness'] = avg_fit
    results['Avg_lambda'] = avg_lambda
    text_log += ('Average generations to solve:' + str(results['Avg_generations']) + '\n' +
                 'Average evaluations to solve:' + str(results['Avg_evaluations']) + '\n' +
                 'Average fitness:' + str(results['Avg_fitness'])  + '\n' +
                 'Average lambda:' + str(results['Avg_lambda']))
    results['Text_log'] = text_log
    
    res = Outputs(configuration.problem_size, results)    
    today = date.today()
    today = today.strftime("%y-%m-%d")
    now = datetime.now()
    now = now.strftime("%H:%M:%S")
    name = ('_'+ today+ '_'+ now +'_'+configuration.problem+'_n'+str(configuration.problem_size)+'_'+
            configuration.algorithm+'_λ'+str(configuration.offspring_size))
    if configuration.verbose:
        res.show_results()
    res.save(name)
    
    return results
    
if __name__ == '__main__':
    res = execute_experiment()
