// Brian Goldman

// This is an implementation of the 1+(lambda,lambda) optimization
// algorithm, which comes from the paper:
// "Lessons from the black-box: fast crossover-based genetic algorithms"
// by B. Doerr, C. Doerr, and F. Ebel

#ifndef DFASTLAMBDALAMBDA_H_
#define DFASTLAMBDALAMBDA_H_

#include "Optimizer.h"
#include "Util.h"

// Inherits and implements the Optimizer interface
class DFastLambdaLambda : public Optimizer {
 public:
  DFastLambdaLambda(Random& _rand, shared_ptr<Evaluator> _evaluator,
               Configuration& _config);
  virtual bool iterate() override;
  create_optimizer(DFastLambdaLambda);

 private:
  // Uses a population size of 1
  vector<bool> solution;
  float fitness;
  // Parameter used to control mutation rate and offspring number
  float lambda;
  // Collection of distributions of incrementally smaller size
  vector<std::uniform_int_distribution<>> selectors;
  vector<size_t> options;
  // Power law distributions
  std::discrete_distribution<int>power_dist_lambda;
  std::discrete_distribution<int>power_dist_s;
  // returns a random solution with a hamming distance of "flips" from the parent
  vector<bool> mutate(const vector<bool>& parent, const int flips);
  // returns a uniform crossover of the solutions using the crossover probability
  vector<bool> crossover(const vector<bool>& p1, const vector<bool>& p2,
      std::bernoulli_distribution& prob);
};

#endif /* DFASTLAMBDALAMBDA_H_ */