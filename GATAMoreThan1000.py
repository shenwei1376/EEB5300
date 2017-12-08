from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import GC
import pandas as pd

#open the gene list txt file, and save it as a list, and remove the new line character
gene=open("./genelistMoreThan1000.txt","r")
GeneList=gene.readlines()
GeneName=[(gene.strip()) for gene in GeneList]
print len(GeneName)

#scan through the gff file and find the chromosomes information, gene start/end, and strand
GeneStart=[]
GeneEnd=[]
Strand=[]
Chromosome=[]
GeneFound=[]

gff=open("./drosophila_melanogaster/Drosophila_melanogaster.BDGP6.90.chr.gff3","r")
GffList=gff.readlines()
for line in GffList:
    if line[0]!="#":
        column=line.split("\t")
        name=column[8].split(";")
        if column[2]=="gene" and name[0].split(":")[1] in GeneName:
            Chromosome.append(column[0])
            GeneStart.append(int(column[3])-1)
            GeneEnd.append(int(column[4])-1)
            Strand.append(column[6])
            GeneFound.append(name[0].split(":")[1])
print len(Chromosome)
print len(GeneStart)
print len(GeneEnd)
print len(Strand)
print len(GeneFound)

#go through the fasta file and find the GATA counts in gene's promoter region
Seq=SeqIO.index("./dna/Drosophila_melanogaster.BDGP6.dna.toplevel.fa","fasta")
columns=['Chr', 'FBgn', 'GATAcounts', 'GATAAcounts', 'Strand', 'PromoterSequence']
GATAresult=pd.DataFrame(columns=columns)
for gene in GeneFound:
    index=GeneFound.index(gene)
    sequence=Seq[Chromosome[index]].seq
    Start=GeneStart[index]
    promoter_seq=sequence[(int(Start)-500):int(Start)].upper() #upper() converts all the characters into upper cases
    if Strand[index]=="+":
        promoter=promoter_seq
    elif Strand[index]=="-":
        promoter=promoter_seq.reverse_complement()       
    GATAcounts=promoter.count("GATA")
    GATAAcounts=promoter.count("GATAA")    
    df=pd.DataFrame([[Chromosome[index], gene, GATAcounts, GATAAcounts, Strand[index], promoter]], columns=columns)
    GATAresult=GATAresult.append(df)
GATAresult.to_csv('./GATAcountsMoreThan1000.csv')
