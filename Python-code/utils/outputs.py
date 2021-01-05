#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 12:19:43 2018

@author: mario_hevia
"""

import pickle
import math
import matplotlib.pyplot as plt

class Outputs:
    def __init__(self, problem_size, results = None):
        self.results = results
        self.problem_size = problem_size
        
    def save(self, name):
        with open('results/results' + name + '.txt', 'w') as f:
            f.write(self.results['Text_log'])
            
            
    def load(self, name):
        with open('results/results' + name + '.pkl', 'rb' ) as f:
            self.results = pickle.load(f)
        
    def show_results(self):
        if self.results is None:
            print('No results available')
            return
        print('Average generations to solve:', self.results['Avg_generations'])
        print('Average evaluations to solve:', self.results['Avg_evaluations'])
        print('Average fitness:', self.results['Avg_fitness'])
        print('Average lambda:', self.results['Avg_lambda'])
