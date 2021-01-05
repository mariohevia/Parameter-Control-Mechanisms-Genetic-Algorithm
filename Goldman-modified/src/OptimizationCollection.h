// Brian Goldman

// This file aggregates optimization methods
// so that they can be chosen through configuration options

#ifndef OPTIMIZATIONCOLLECTION_H_
#define OPTIMIZATIONCOLLECTION_H_

#include "Optimizer.h"
#include "LTGA.h"
#include "Pyramid.h"
#include "RandomRestartHC.h"
#include "LambdaLambda.h"
#include "LambdaLambdaCap.h"
#include "LambdaLambdaReset.h"
#include "LambdaLambdaResetF.h"
#include "OnePlusOne.h"
#include "FastOnePlusOne.h"
#include "FastLambdaLambda.h"
#include "DFastLambdaLambda.h"
#include "HBOA.h"
#include "Popless.h"
#include <unordered_map>

namespace optimize {
// Renaming of the function pointer used to create new optimization methods
using pointer=shared_ptr<Optimizer> (*)(Random& rand, shared_ptr<Evaluator> evaluator, Configuration& config);

// Lookup table translates strings to function pointers
static std::unordered_map<string, pointer> lookup( {
  { "LTGA", LTGA::create },
  { "Pyramid", Pyramid::create },
  { "RandomRestartHC", RandomRestartHC::create },
  { "LambdaLambda", LambdaLambda::create },
  { "LambdaLambdaCap", LambdaLambdaCap::create },
  { "LambdaLambdaReset", LambdaLambdaReset::create },
  { "LambdaLambdaResetF", LambdaLambdaResetF::create },
  { "OnePlusOne", OnePlusOne::create },
  { "FastOnePlusOne", FastOnePlusOne::create },
  { "FastLambdaLambda", FastLambdaLambda::create },
  { "DFastLambdaLambda", DFastLambdaLambda::create },
  { "HBOA", HBOA::create},
  { "Popless", Popless::create},
});
}

#endif /* OPTIMIZATIONCOLLECTION_H_ */
