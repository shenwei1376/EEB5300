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

jellyfish count -t 8 -C -m 15 -s 5G -o out_15mer --min-qual-char=? DRR097196_1.fastq DRR097196_2.fastq
jellyfish count -t 8 -C -m 17 -s 5G -o out_17mer --min-qual-char=? DRR097196_1.fastq DRR097196_2.fastq
jellyfish count -t 8 -C -m 19 -s 5G -o out_19mer --min-qual-char=? DRR097196_1.fastq DRR097196_2.fastq
jellyfish count -t 8 -C -m 21 -s 5G -o out_21mer --min-qual-char=? DRR097196_1.fastq DRR097196_2.fastq

echo  "mer done"

