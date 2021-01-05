#!/bin/bash
#$ -l rmem=24G #number of memory
#$ -l h_rt=96:00:00
#$ -j y # normal and error outputs into a single file (the file above)
#$ -cwd # Run job from current directory
# Request 1 CPU cores
#$ -pe smp 1

cd ../
module load libs/boost/1.64.0/gcc-4.9.4

./Release/P3 config/default.cfg config/IsingSpinGlass.0144.FastLambdaLambda.cfg