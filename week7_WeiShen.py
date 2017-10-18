#load the fasta file and save it as a list
from Bio import SeqIO
from Bio.SeqUtils import GC
from Bio.Seq import Seq
SeqList=list(SeqIO.parse("/Users/weishen/documents/Courses/EEB5300/week7/Adarlingi_v1.fna","fasta"))

#create GeneName list
gene=open("/Users/weishen/documents/Courses/EEB5300/week7/genes.txt","r")
GeneList=gene.readlines()
GeneName=[]
for gene in GeneList:
    name=gene.strip()
    GeneName.append(name)
print len(GeneName)

#create lists for chromosome, Gene start position, gene end position and gene strand information
gff=open("/Users/weishen/documents/Courses/EEB5300/week7/Adarlingi_v1.gff","r")
GffList=gff.readlines()
ChromosomeList=[]
GeneStart=[]
GeneEnd=[]
GeneStrand=[]
for line in GffList:
    if line[0]!="#":
        column=line.split("\t")
        if column[2]=="gene":
            for gene in GeneName:
                if gene in column[8]:
                    ChromosomeList.append(column[0])
                    GeneStart.append(column[3])
                    GeneEnd.append(column[4])
                    GeneStrand.append(column[6])
print len(ChromosomeList)
print len(GeneStart)
print len(GeneEnd)
print len(GeneStrand)

#find the genes that contain GATA sequence in their promoter region: 500 bps upstream of the transcriptional start site
GeneWithGATA=[]
GeneSeqWithGATA_includePromoterSeq=[]
for record in SeqList:
    if record.id in ChromosomeList:
        index=ChromosomeList.index(record.id)
        if GeneStrand[index]=="+":
            promoter=record.seq[(int(GeneStart[index])-500):(int(GeneStart[index])-1)]
            [x.upper() for x in promoter]
            GATACounts=promoter.count("GATA")
            if GATACounts>=1:
                GeneWithGATA.append(GeneName[index])
# extract the gene sequence and promoter sequence
                GeneSeqWithGATA_includePromoterSeq.append(str(record.seq[(int(GeneStart[index])-500):(int(GeneEnd[index]))]))
        elif GeneStrand[index]=="-":
            promoter2=record.seq[(int(GeneStart[index])-500):(int(GeneStart[index])-1)]
            promoter3=promoter2.reverse_complement()
            [x.upper() for x in promoter3]
            GATACounts2=promoter2.count("GATA")
            if GATACounts2>=1:
                GeneWithGATA.append(GeneName[index])
#extract the gene sequence and promoter sequence
                GeneSeqWithGATA_includePromoterSeq.append(str(record.seq[(int(GeneStart[index])-500):(int(GeneEnd[index]))].reverse_complement()))
print len(GeneWithGATA)

#write the promoter sequence and the gene sequence out to a fastq file
with open("/Users/weishen/documents/Courses/EEB5300/week7/Adarlingi_v1_sub.gff","w") as fout:
    for item in GeneSeqWithGATA_includePromoterSeq:
        fout.write(item)
#each sequence contains gene sequence plus 500 bps upstream of the transcript start site, and all the "-" strand are reverse complemented
