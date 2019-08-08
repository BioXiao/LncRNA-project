#!/usr/bin/env python
#count length/number of exon
#python extract3.py -i1 noncoding.txt -i2 ref_lncRNA.gtf  -o1 novellncRNA_exon_length.txt -o2 novellncRNA_exon_number.txt
#python extract3.py -i1 protein_name.txt -i2 class_code.gtf  -o1 protein_exon_length.txt -o2 protein_exon_number.txt
#python extract3.py -i1 annotated_LncRNA_name.txt -i2 class_code.gtf  -o1 LncRNA_exon_length.txt -o2 LncRNA_exon_number.txt
import argparse
import re
parser = argparse.ArgumentParser(description="This is just a test")
parser.add_argument("-i1","--input1",help="the first argument")
parser.add_argument("-i2","--input2",help="the second argument")
parser.add_argument("-o1","--output1",help="the third argument")
parser.add_argument("-o2","--output2",help="the third argument")
args = parser.parse_args()
file1=open(args.input1,'r')
file2=open(args.input2,'r')
file3=open(args.output1,'w')
file4=open(args.output2,'w')
dict_exon={}
dict_id={}
for i in file1:
    i=i.strip('\n').split('\t')[0]
    dict_id[i]=''
for j in file2:
    j=j.strip('\n')
    exon=j.split('\t')
    trans_id=re.search('transcript_id \"(.*?)\"\;',exon[8]) #novellncRNA
    #trans_id=re.search('gene_name \"(.*?)\"\;',exon[8])      #annotated gene
    if trans_id.group(1) in dict_id:
        if dict_exon.get(trans_id.group(1)):
            dict_exon[trans_id.group(1)].extend([[exon[3],exon[4]]])
        else:
            dict_exon[trans_id.group(1)]=[[exon[3],exon[4]]]
for k in dict_exon:
    exon_length=0
    exon_number=0
    for m in dict_exon[k]:
        exon_length+=int(m[1])-int(m[0])+1
        exon_number+=1
    file3.writelines(k+'\t'+str(exon_length)+'\n')
    file4.writelines(k+'\t'+str(exon_number)+'\n')
file1.close()
file2.close()
file3.close()
file4.close()
