// Brian Goldman

// Implementation of the 1+(lambda,lambda) algorithm
// Includes the following modifications from the original paper:
// * Keeps best mutant if it has a higher fitness than the best crossover offspring
// * Prevents duplicated evaluations when the crossover offspring is identical to
//   one of its parents
// * If two crossover offspring have the same fitness, selects the one with maximum hamming
//   distance from the parent
// * If lamdba exceeds the solution length, reset lambda to 1

#include "LambdaLambdaReset.h"

// Constructs some tools used during evolution, performs initial evaluation
LambdaLambdaReset::LambdaLambdaReset(Random& _rand, shared_ptr<Evaluator> _evaluator,
                           Configuration& _config)
    : Optimizer(_rand, _evaluator, _config),
      selectors(length),
      options(length) {
  // create and evaluate initial solution
  solution = rand_vector(rand, length);
  fitness = evaluator->evaluate(solution);
  lambda = 1;

  // Tool for choosing random mutation locations
  for (size_t i = 0; i < length; i++) {
    selectors[i] = std::uniform_int_distribution<>(i, length - 1);
  }
  std::iota(options.begin(), options.end(), 0);
}

// Selects "flips" number of random locations to perform bit flips.
vector<bool> LambdaLambdaReset::mutate(const vector<bool>& parent, const int flips) {
  vector<bool> mutant(solution);
  for (int j = 0; j < flips; j++) {
    // Swaps a random option into location j
    std::swap(options[j], options[selectors[j](rand)]);
    // Flip the bit
    mutant[options[j]] = not mutant[options[j]];
  }
  return mutant;
}

// Uses the "prob" to determine if a gene should come from p1 or p2
vector<bool> LambdaLambdaReset::crossover(const vector<bool>& p1,
                                     const vector<bool>& p2,
                                     std::bernoulli_distribution& prob) {
  // Copy over all of p1
  vector<bool> offspring(p1);
  for (size_t j = 0; j < length; j++) {
    // Take p2 at set probability
    if (prob(rand)) {
      offspring[j] = p2[j];
    }
  }
  return offspring;
}

// Performs a full generation of the algorithm.
bool LambdaLambdaReset::iterate() {
  // Variables for number of offspring / mutation rate
  int flips;
  
  // Variables to select the best offspring
  vector<vector<bool>> population;

  // Distributions needed at the current lambda
  std::binomial_distribution<> binom(length, lambda / length);
  std::bernoulli_distribution cross(1 / lambda);
  flips = binom(rand);
  
  // Mutation loop
  vector<bool> best_offspring = mutate(solution, flips);
  float best_offspring_fitness = evaluator->evaluate(best_offspring);
  population.push_back(best_offspring);
  for (int i = 1; i < round(lambda); i++) {
    vector<bool> next = mutate(solution, flips);
    float next_fitness = evaluator->evaluate(next);
    if (best_offspring_fitness < next_fitness) {
      best_offspring_fitness = next_fitness;
      population.clear();
      population.push_back(next);
    }
    if (best_offspring_fitness == next_fitness) {
      population.push_back(next);
    }
  }
  best_offspring = select_rand(rand, population);
  population.clear();

  // Crossover loop
  // Keeps the best mutation offspring if its better than all crossover
  vector<bool> next_parent(best_offspring);
  float next_parent_fitness = best_offspring_fitness;
  float next_fitness;
  population.push_back(next_parent);
  for (int i = 0; i < round(lambda); i++) {
    vector<bool> next = crossover(solution, best_offspring, cross);
    next_fitness = evaluator->evaluate(next);

    // Keeps the best offspring in population
    if (next_parent_fitness < next_fitness) {
      next_parent_fitness = next_fitness;
      population.clear();
      population.push_back(next);
    }
    if (next_parent_fitness == next_fitness) {
      population.push_back(next);
    }
  }
  next_parent = select_rand(rand, population);
  
  // update lambda

  // If lambda exceeds the solution length, reset lambda to 1
  if (lambda == length) {
    lambda = 1;
  }

  if (fitness < next_parent_fitness) {
    // Magic number from the original paper
    lambda = lambda / 1.5;
    if (lambda < 1) {
      lambda = 1;
    }
  } else {
    // If lambda is at its maximum, reset lambda to 1
    if (lambda == length) {
      lambda = 1;
    } else {
      // Magic number for 1.5 ** 0.25
      lambda *= 1.1067;
      if (lambda > length) {
        lambda = length;
      }
    }
  }

  // only replace parent if offspring was no worse
  if (fitness <= next_parent_fitness) {
    fitness = next_parent_fitness;
    solution = next_parent;
  }

  // This algorithm never reaches stagnation, so always return true
  return true;
}
