# Theoretical and Empirical Analysis of Parameter Control Mechanisms in the (1+(λ,λ)) Genetic Algorithm
This is the implementation, and results for the "Theoretical and Empirical Analysis of Parameter Control Mechanisms in the (1+(λ,λ)) Genetic Algorithm" publication.

# Code structure
The code is divided into two different parts. One is the implementation of all the algorithms to test all problems except IsingSpinGlass and MAX3SAT. And the other one is a modification of the code created by Goldman and Punch that can be found in `https://github.com/brianwgoldman/P3` to run the experiments on the IsingSpinGlass and MAX3SAT problems.

The first part is comprised of Python code in the directory `Python-code/` and can be executed from the file `master.py` with the appropriate command line options. An example is:

    python master.py -t OneMax -n 100 -l 100 -r 500 -c 1 -a JA.OnePlusLambdaCommaLambdaSAReset -G 1.5 --seed 885480221 -v

The second part is comprised of C++ code in the directory `Goldman-modified/`. To compile the second part you need C++11. The build system uses Makefiles to build. You can compile the release version by changing directory to `Goldman-modified/Release/` and calling "make". All of the source code of this part is available in the `Goldman-modified/src` directory.

To run an experiment, call the executable with command line arguments for configuration. This will run the default test configuration:

    Release/P3 config/default.cfg
    
# Results

The results of all experiments have been captured into the file `Results.ods` with the raw results in the directories `Raw/` and `Goldman-modified/results/`. The directory `processed-results/` contains the processed data from the results in `Raw/` with one file per algorithm-problem pair. 
