#!/bin/bash
#$ -N GenomeEstimationScript
#$ -M wei.shen@uconn.edu
#$ -q highmem.q
#$ -m ea
#$ -S /bin/bash
#$ -cwd
#$ -pe smp 8
#$ -o $JOB_ID.out
#$ -e $JOB_ID.err

module load jellyfish/2.2.6

jellyfish histo -o 15mer_out.histo out_15mer
jellyfish histo -o 17mer_out.histo out_17mer
jellyfish histo -o 19mer_out.histo out_19mer
jellyfish histo -o 21mer_out.histo out_21mer

echo  "mer done"

