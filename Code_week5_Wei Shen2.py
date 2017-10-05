#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:38:18 2017

@author: weishen
"""

# open the file and save the line information in the gfflines
fh=open("/Users/weishen/documents/Courses/EEB5300/week5/Pita_MakerAlignments.gff3","r")
gfflines=fh.readlines()

# analyze each line and break the column by tab
genecounts=0
ExonNumber=[]
exoncounts=0
ExonLength=[]
geneID=[]
exonless20geneID=[]
for line in gfflines:
    if line[0]!="#":
        column=line.split("\t")
# count the number of gene
        if column[2]=="gene":            
            genecounts=genecounts+1
# extract all genes' ID
            geneID.append(column[8])
# count the number of exon for previous gene
            ExonNumber.append(exoncounts)
# re-start counting the number of exons
            exoncounts=0                       
        elif column[2]=="exon":
            exoncounts=exoncounts+1
# calculate the length of each exon, the number should be confirmed with "sum(ExnoNumber)", make sure they are the same
            exonlength=int(column[4])-int(column[3])
            ExonLength.append(exonlength)
# extract the gene ID with exon less than 20 bps          
            if exonlength<20:
                exonless20geneID.append(column[8])
            
# !!!answer for the question1: how many genes are present in the gff file?
print genecounts

# clean the ExonNumber list with removing the first 0 and adding the last exoncounts  
ExonNumber.pop(0)
ExonNumber.append(exoncounts)
# count the multiexonic genes
multiexonicGene=0
monoexonicGene=0
for n in ExonNumber:
    if n>1:
       multiexonicGene=multiexonicGene+1
# count the monoexonic genes 
    elif n==1:
        monoexonicGene=monoexonicGene+1

# !!!answer for the question2: How many multiexonic genes are found in the gff file?
print multiexonicGene

# !!!answer for the question3: How many monoexonic genes are found in the gff file?
print monoexonicGene

# !!!minimum length of the exons
miniExon=min(ExonLength)
print miniExon

# !!!maximum lengh of the exons
maxExon=max(ExonLength)
print maxExon

# !!!average length of the exons
meanExon=sum(ExonLength)/len(ExonLength)
print meanExon

# !!!median length of the exons. the size of the ExonLenth is a even numuber, so I directly go for the calculation
meanExon=(ExonLength[len(ExonLength)/2-1]+ExonLength[len(ExonLength)/2])+1
print meanExon

# Create a new gff file such that there are only multiexonic genes present and the mutliexonic genes have all exons that are at least 20 base pairs. 
# create a list containing gene ID of monoexon gene
def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs
monoexongeneIndex=list_duplicates_of(ExonNumber, 1)
monoexongeneID=[]
for index in monoexongeneIndex:
    monoexongeneID.append(geneID[index])
    
# remove the monoexon gene from geneID list
geneID_multiexon=list(set(geneID)-set(monoexongeneID))

# remove the gene with exon less than 20
# isolate the Gene Name and remove "\n", put all the genenames in a new list
GeneName_multiexon=[]
for line2 in geneID_multiexon:
    GeneName=line2.split(";")[1]
    GeneName_multiexon.append(GeneName.rstrip())
# find the index inforamtion of genes with exon less than 20 bps, and remove them from the list
GeneNameLess20Index=[]
for genename in GeneName_multiexon:
    for exonname in exonless20geneID:
        if genename in exonname:
            genenameIndex=GeneName_multiexon.index(genename)
            GeneNameLess20Index.append(genenameIndex)
GeneIDless20=[]
for index in GeneNameLess20Index:
    GeneIDless20.append(geneID_multiexon[index])
#final list after removed the monoexon gene and short exon gene
geneID_multiexon_removeExonLess20=list(set(geneID_multiexon)-set(GeneIDless20))

#create a sub gff file and list the above new genes into it
ita_MakerAlignmentsSub=[]
# work through each line, find the lines that contain the genename in the geneID_multiexon_removeExonLess20 list
for line in gfflines:
    if line[0]!="#":
        column=line.split("\t")
        name=column[8]
        for GeneName2 in geneID_multiexon_removeExonLess20:
            GeneName3=GeneName2.split(";")[1]
            GeneName4=GeneName3.rstrip()
            if GeneName4 in column[8]:
                ita_MakerAlignmentsSub.append(line)
# write the gene information into a new gff file           
with open("/Users/weishen/documents/Courses/EEB5300/week5/ita_MakerAlignmentsSub.gff3", "w") as fout:
    for item in ita_MakerAlignmentsSub:
        fout.write(item)
