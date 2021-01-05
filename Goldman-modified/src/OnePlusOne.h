// Brian Goldman

// This is an implementation of the 1+(lambda,lambda) optimization
// algorithm, which comes from the paper:
// "Lessons from the black-box: fast crossover-based genetic algorithms"
// by B. Doerr, C. Doerr, and F. Ebel

#ifndef ONEPLUSONE_H_
#define ONEPLUSONE_H_

#include "Optimizer.h"
#include "Util.h"

// Inherits and implements the Optimizer interface
class OnePlusOne : public Optimizer {
 public:
  OnePlusOne(Random& _rand, shared_ptr<Evaluator> _evaluator,
               Configuration& _config);
  virtual bool iterate() override;
  create_optimizer(OnePlusOne);

 private:
  // Uses a population size of 1
  vector<bool> solution;
  float fitness;
  // Parameter used to control mutation rate and offspring number
  float lambda;
  // Collection of distributions of incrementally smaller size
  vector<std::uniform_int_distribution<>> selectors;
  vector<size_t> options;
  // returns a random solution with a hamming distance of "flips" from the parent
  vector<bool> mutate(const vector<bool>& parent, const int flips);
};

#endif /* ONEPLUSONE_H_ */
