#The mutiline fatsa was tranferred to single line fasta by the following code 
#perl -pe '/^>/ ? print "\n" : chomp' Arabidopsis_thaliana_clean.faa | tail -n +2 > Arabidopsis_thaliana_clean_Singalline.faa
#All the rest of the analysis is based on the single line .faa file

#open the faa file and extract the ID information
record=open("../maker_chr4/Arabidopsis_thaliana_clean_Singalline.faa","r")
line=record.readlines()
ID=[]
Seq=[]
for l in line:
    if l[0]==">":
        ID.append(l)
    else:
        Seq.append(l)
print len(ID)
print len(Seq)

#create lists for ID and Seq that matches parsed_arth_prots.4.gff3
IDSub=[]
SeqSub=[]
arth_prots_aligned=[]

#extract the names from parsed_arth_prots.4.gff3 
gff=open("./parsed_arth_prots.4.gff3", "r")
GFF=gff.readlines()

for g in GFF:
    column=g.split("\t")
    if column[2]=="gene":
        name1=column[8].split(";")[1].rstrip()
        name2=name1.lstrip("Name=")
#extract the ID and Seq infos that matches the name from parsed_arth_prots.4.gff3
        for i in ID:
            if name2 in i:
                index=ID.index(i)
                IDSub.append(i)
                arth_prots_aligned.append(i)
                SeqSub.append(Seq[index])
                arth_prots_aligned.append(Seq[index])
print len(IDSub)
print len(SeqSub)
print len(arth_prots_aligned)

#write the new arth_prots_aligned.faa file
with open("./arth_prots_aligned.faa", "w") as fout:
    for item in arth_prots_aligned:
        fout.write(item)
