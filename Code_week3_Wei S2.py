#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 10:17:49 2017

@author: weishen
"""

### 1. open the fasta file and save it to the variable lines
fh=open("/Users/weishen/documents/Courses/EEB5300/week3_codechallenge/PitaIlluminaGeneSet.fasta","r")
lines=fh.readlines()


### 2. print the number of genes in the fasta file
genecounts=0
for line in lines:
    if line[0]==">":
        genecounts=genecounts+1
print genecounts


### 3. calculate statistics for the given file
# creating 3 lists containing gene name, gene sequence and sequence length
SequenceNames=[]
Sequences=[]
SequenceLength=[]
for line in lines:
    if line[0]==">":
        SequenceNames.append(line)
    elif line[0]!=">":
        Sequences.append(line)
#counting the nucleotides 
        nucleotides=0
        for nuc in line: 
            if nuc=="A":
                nucleotides=nucleotides+1
            elif nuc=="a":
                nucleotides=nucleotides+1
            elif nuc=="T":
                nucleotides=nucleotides+1
            elif nuc=="t":
                nucleotides=nucleotides+1
            elif nuc=="G":
                nucleotides=nucleotides+1
            elif nuc=="g":
                nucleotides=nucleotides+1   
            elif nuc=="C":
                nucleotides=nucleotides+1
            elif nuc=="c":
                nucleotides=nucleotides+1  
        SequenceLength.append(nucleotides)            
        
# a. print the minmum length of the sequence and the sequence name associated with this minmun length
indexmin=SequenceLength.index(min(SequenceLength))
MinimumSeq=Sequences[indexmin]
print MinimumSeq

MinimumSeqName=SequenceNames[indexmin]
print MinimumSeqName

# b. print the maximum length of the sequence and the sequence name associated with this maximum length
indexmax=SequenceLength.index(max(SequenceLength))
MaximumSeq=Sequences[indexmax]
print MaximumSeq

MaximumSeqName=SequenceNames[indexmax]
print MaximumSeqName

# c. print the average length of the sequences
AverageLen=sum(SequenceLength)/490
print AverageLen


### output a file with sequence anmes whoses length is less than 500 base pairs
# extract the position information for all the genes that are less than 500 bps
indexless500=[]
for len in SequenceLength:
    if len<500:
        indexless500.append(SequenceLength.index(len))
        
# extract the genes based on the position information and put them into a new list of PitalluminaGeneSetSub
PitaIlluminaGeneSetSub=[]
for i in indexless500:
    PitaIlluminaGeneSetSub.append(lines[i*2])
    PitaIlluminaGeneSetSub.append(lines[i*2+1])

# write the genes into an output file
with open("temp.fasta", "w") as fout:
    for item in PitaIlluminaGeneSetSub:
        fout.write(item)
        
### the temp.fasta file appear in my home directory:  /Users/weishen/



