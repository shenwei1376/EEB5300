from Bio import SeqIO

#open the gff file and save it into lines
gff=open("/tempdata3/Wshen/5300/CodeChallenge5/scripts/arth_prots.4.gff", "r")
BeforeFilter=gff.readlines()
print len(BeforeFilter)

#create a new list only with Chr4 lines, removing all other comment lines, so I will be able to index each line
GFF=[]
for line in BeforeFilter:
    if line[0:3]=="Chr":
        GFF.append(line)
print len(GFF)

#create the line index information for each gene, line with "gene" will be the starting line of that gene and line with "similarity" will be the ending line of that gene 
GenelineIndex=[] #collection of index representing the starting line of the gene
similaritylineIndex=[] #collection of index representing the ending line of the gene
for gffline in GFF:
    column=gffline.split("\t")
    if column[2]=="gene":
        GenelineIndex.append(GFF.index(gffline))
    if column[2]=="similarity":
        similaritylineIndex.append(GFF.index(gffline))
print len(GenelineIndex)
print len(similaritylineIndex)

#locate the gene index that needs to be removed
RemoveGeneList=[]
for g in GenelineIndex:
    geneline=GFF[g]
    column2=geneline.split("\t")
    if int(column2[5])<1000:
        RemoveGeneList.append(g)
    elif int(column2[5])>=1000:
        for c in range(g+1,similaritylineIndex[GenelineIndex.index(g)]):
            nongeneline=GFF[c]
            column3=nongeneline.split("\t")
            if column3[2]=="splice5" and "GT" not in column[8]:
                RemoveGeneList.append(g)
            elif column3[2]=="splice3" and "AG" not in column[8]:
                RemoveGeneList.append(g)
GeneWanted=list(set(GenelineIndex)-set(RemoveGeneList))
print len(GeneWanted)
print len(RemoveGeneList) 
#generate new gff list after filtering
AfterFilter=[]
for g2 in GeneWanted:
    for c2 in range(g2,similaritylineIndex[GenelineIndex.index(g2)]):
        AfterFilter.append(GFF[c2])
print len(AfterFilter)

#write a new gff file parsed_arth_prots.4.gff  
with open("/tempdata3/Wshen/5300/CodeChallenge5/scripts/parsed_arth_prots.4.gff","w") as fout:
    for item in AfterFilter:
        fout.write(item)
