#!/usr/bin/env python
#predict novel lncRNA
#python predict_novel_LncRNA.py -i1 Homo_sapiens.GRCh38.83.gtf -i2 HSVnovel.tracking  -i3 HSVnovel.combined.gtf  -o ref_lncRNA_final.gtf
import argparse
import re
parser = argparse.ArgumentParser(description="This is just a test")
parser.add_argument("-i1","--input1",help="the first argument")
parser.add_argument("-i2","--input2",help="the second argument")
parser.add_argument("-i3","--input3",help="the third argument")
parser.add_argument("-o","--output",help="the fourth argument")
args = parser.parse_args()
file1=open(args.input1,'r')
file2=open(args.input2,'r')
file3=open(args.input3,'r')
file4=open(args.output,'w')
seqline=''
feature=''
name_id=''
dict_feature={}
#select gene name from ENSEMBLE GTF file
for seqline in file1:
    seqline=seqline.strip('\n')
    if re.search('#!',seqline) is not None:
        continue
    feature=seqline.split('\t')[8]
    name_id=re.search('gene_name \"(.*?)\"\;',feature)
    dict_feature[name_id.group(1)]=feature.split(';')[0]
namedict={}
eachline=''
each=[]
CUFF=''
num=[]
#exclude FPKM of transcript <1 from tracking file
for eachline in file2:
    eachline=eachline.strip("\n")
    each=eachline.split("\t")
    for CUFF in each[4:]:
        if CUFF == '-':
            continue
        else:
            num=CUFF.split(',')
            if len(num)==1:            
                if(float(CUFF.split('|')[3])>=1.0):
                    namedict[each[0]]=''
                    continue
                else:
                    continue
            elif len(num)==2:
                fpkm=float(num[0].split('|')[3])+float(num[1].split('|')[3])
                if(fpkm>=1.0):
                    namedict[each[0]]=''
            else:
                continue
lineeach=''
listname=''
name=''
code_flag=[]
flag=''
transcript_id=''
exon_number=0
gene_id=''
dict_id={}
dict_count={}
transcriptid=''
#select i,j,o,u,x and count exon number from combined file
for lineeach in file3:
    lineeach=lineeach.strip('\n')
    listname=lineeach.split('\t')[8]
    name=re.search('class_code \"(.*?)\";',listname)
    flag=name.group(1)
    code_flag=['i','j','o','u','x']
    if (flag not in code_flag):
        continue
    transcriptid=re.search('transcript_id \"(.*?)\"\;',listname)
    transcript_id=transcriptid.group(1)
    if transcript_id not in namedict:
        continue
    exon_number=int(re.search('exon_number \"(.*?)\"\;',listname).group(1))
    gene_id=re.search('gene_id \"(.*?)\"\;',listname).group(1)
    if dict_id.get(transcript_id):
        dict_id[transcript_id].extend([lineeach])
    else:
        dict_id[transcript_id]=[lineeach]
    if transcript_id in dict_count:
        dict_count[transcript_id]=dict_count[transcript_id]+exon_number
    else:
        dict_count[transcript_id]=exon_number
key=''
value=[]
first_line=[]
second_line=''
raw_data=[]
pos=[]
gene_name_id=''

for key in dict_id:
    if int(dict_count[key])==1:
        continue
    value=dict_id[key]
    number=len(value)
    length=0
    for first_line in range(number):
        raw_data=value[first_line].split('\t')
        left=value[0].split('\t')[3]
        right=value[number-1].split('\t')[4]
        length=length+int(right)-int(left)+1
        if length <= 200:
            continue
        pos=raw_data[8].split('; ')
        gene_name_id=pos[3].split('"')[1]
        if gene_name_id in dict_feature:
            pos[0]=dict_feature[gene_name_id]
        raw_data[8]=';'.join(pos)
        file4.writelines('\t'.join(map(str,raw_data))+'\n')
file1.close()
file2.close()
file3.close()
file4.close()


