// Brian Goldman

// This is an implementation of the 1+(lambda,lambda) optimization
// algorithm, which comes from the paper:
// "Lessons from the black-box: fast crossover-based genetic algorithms"
// by B. Doerr, C. Doerr, and F. Ebel

#ifndef FASTONEPLUSONE_H_
#define FASTONEPLUSONE_H_

#include "Optimizer.h"
#include "Util.h"
#include <map>

// Inherits and implements the Optimizer interface
class FastOnePlusOne : public Optimizer {
 public:
  FastOnePlusOne(Random& _rand, shared_ptr<Evaluator> _evaluator,
               Configuration& _config);
  virtual bool iterate() override;
  create_optimizer(FastOnePlusOne);

 private:
  // Uses a population size of 1
  vector<bool> solution;
  float fitness;
  // Parameter used to control mutation rate and offspring number
  float lambda;
  // Collection of distributions of incrementally smaller size
  vector<std::uniform_int_distribution<>> selectors;
  vector<size_t> options;
  // Power law distribution
  std::discrete_distribution<int>power_dist;
  // returns a random solution with a hamming distance of "flips" from the parent
  vector<bool> mutate(const vector<bool>& parent, const int flips);
};

#endif /* FASTONEPLUSONE_H_ */
