#load the libary biomaRt and convert the ensembl IDs gene name and entrezgene
library("biomaRt")
data<-read_excel("ensembl ID.xlsx")
ensembl=useMart("ensembl", dataset="hsapiens_gene_ensembl")
ensemblIDConversion<-getBM(attributes = c('ensembl_gene_id_version','chromosome_name','external_gene_name','entrezgene'),
      filters = 'ensembl_gene_id_version',
      values = data,
      mart=ensembl)
#write out the result into a .csv file
write.csv(ensemblIDConversion, "/Users/weishen/Documents/Courses/EEB5300/final project/ensemblIDConversion.csv")

#clean the gene list with clean the duplication and remove the genes with no ID
ensemblIDConversion_CleanDuplcate<-ensemblIDConversion[!duplicated(ensemblIDConversion[,1]),]
write.csv(ensemblIDConversion_CleanDuplcate, "/Users/weishen/Documents/Courses/EEB5300/final project/ensemblIDConversion_CleanDuplcate.csv")

CountsData<-read_excel("Counts.xlsx")
Counts_RemoveGeneWithNoID<-subset(CountsData, CountsData$ensembl_gene_id_version %in% ensemblIDConversion$ensembl_gene_id_version)
write.csv(Counts_RemoveGeneWithNoID, "/Users/weishen/Documents/Courses/EEB5300/final project/Counts_RemoveGeneWithNoID.csv")

#The genes with expression level higher than 1000 are pasted out and saved in entrezgene.xlsx file. The following analysis is based on this high expression gene list
#genename are extracted and saved in a list
genename<-read_excel("entrezgene.xlsx")
genelist<-genename$genename
#protein sequence fasta files are extraedt from biomart 
genesquence<-getSequence(id = genelist, type = "external_gene_name", seqType = "peptide", mart = ensembl)
write.csv(genesquence, "/Users/weishen/Documents/Courses/EEB5300/final project/genesquence.csv")
exportFASTA(genesquence, file="/Users/weishen/Documents/Courses/EEB5300/final project/genesquence.fa")

#analyze the data from signalP prediction
#read the result
SignalPrediction<-read.csv("SignalPResult.csv")
#remove duplicate of the list, the duplication is due to multiple isoforms for each gene transcription
SignalPrediction_CleanDuplcate<-SignalPrediction[!duplicated(SignalPrediction[,1]),]
write.csv(SignalPrediction_CleanDuplcate, "/Users/weishen/Documents/Courses/EEB5300/final project/SignalPrediction_CleanDuplcate.csv")
#subset the dataframe with secretory proteins only
PreidctedSecretoryProducts<-subset(SignalPrediction_CleanDuplcate, SignalPrediction_CleanDuplcate$X.=="Y" & SignalPrediction_CleanDuplcate$Networks.used=="SignalP-noTM")
write.csv(PreidctedSecretoryProducts, "/Users/weishen/Documents/Courses/EEB5300/final project/PreidctedSecretoryProducts.csv")

#expression level of secretory product
ensemblIDConversion_CleanDuplcate2<-read.csv("ensemblIDConversion_CleanDuplcate 2.csv")
PredictedSecretoryProductWithExpressionLevel<-subset(ensemblIDConversion_CleanDuplcate2, ensemblIDConversion_CleanDuplcate2$external_gene_name %in% PreidctedSecretoryProducts$name)
write.csv(PredictedSecretoryProductWithExpressionLevel, "/Users/weishen/Documents/Courses/EEB5300/final project/PredictedSecretoryProductWithExpressionLevel.csv")
PredictedSecretoryProductWithExpressionLevel_CleanDuplcate<-PredictedSecretoryProductWithExpressionLevel[!duplicated(PredictedSecretoryProductWithExpressionLevel[,5]),]
write.csv(PredictedSecretoryProductWithExpressionLevel_CleanDuplcate, "/Users/weishen/Documents/Courses/EEB5300/final project/PredictedSecretoryProductWithExpressionLevel_CleanDuplcate.csv")
