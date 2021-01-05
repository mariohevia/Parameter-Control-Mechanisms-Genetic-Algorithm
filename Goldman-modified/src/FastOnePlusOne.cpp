// Brian Goldman

// Implementation of the 1+(lambda,lambda) algorithm
// Includes the following modifications from the original paper:
// * Keeps best mutant if it has a higher fitness than the best crossover offspring
// * Prevents duplicated evaluations when the crossover offspring is identical to
//   one of its parents
// * If two crossover offspring have the same fitness, selects the one with maximum hamming
//   distance from the parent
// * If lamdba exceeds the solution length, reset lambda to 1

#include "FastOnePlusOne.h"

// Constructs some tools used during evolution, performs initial evaluation
FastOnePlusOne::FastOnePlusOne(Random& _rand, shared_ptr<Evaluator> _evaluator,
                           Configuration& _config)
    : Optimizer(_rand, _evaluator, _config),
      selectors(length),
      options(length) {
  // create and evaluate initial solution
  solution = rand_vector(rand, length);
  fitness = evaluator->evaluate(solution);

  // Tool for choosing random mutation locations
  for (size_t i = 0; i < length; i++) {
    selectors[i] = std::uniform_int_distribution<>(i, length - 1);
  }
  std::iota(options.begin(), options.end(), 0);

  // Power-law distribution
  float B = 1.5;
  vector<double> pmf(length);
  std::iota(pmf.begin(), pmf.end(), 1);
  for(size_t i = 0; i < length; i++) {
    pmf[i] = 1.0 / pow(pmf[i], B);
  }
  pmf.insert(pmf.begin(), 0);
  power_dist = std::discrete_distribution<int>(pmf.begin(),pmf.end());
}

// Selects "flips" number of random locations to perform bit flips.
vector<bool> FastOnePlusOne::mutate(const vector<bool>& parent, const int flips) {
  vector<bool> mutant(solution);
  for (int j = 0; j < flips; j++) {
    // Swaps a random option into location j
    std::swap(options[j], options[selectors[j](rand)]);
    // Flip the bit
    mutant[options[j]] = not mutant[options[j]];
  }
  return mutant;
}

// Performs a full generation of the algorithm.
bool FastOnePlusOne::iterate() {
  // Variables for number of bit flips
  int flips;

  // Distributions needed at the current alpha
  int alpha = power_dist(rand);
  std::binomial_distribution<> binom(length, 1.0 * alpha / length);
  flips = binom(rand);
  
  // Mutation loop
  vector<bool> next_offspring = mutate(solution, flips);
  float next_offspring_fitness = evaluator->evaluate(next_offspring);


  // only replace parent if offspring was no worse
  if (fitness <= next_offspring_fitness) {
    fitness = next_offspring_fitness;
    solution = next_offspring;
  }

  // This algorithm never reaches stagnation, so always return true
  return true;
}
