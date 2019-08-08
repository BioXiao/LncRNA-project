#!/usr/bin/env python
#python extract2.py  -i1 noncoding.txt  -i2 ref_lncRNA.gtf  -o noncoding_name.txt 
import argparse
import sys
import re
parser = argparse.ArgumentParser(description="This is just a test")
parser.add_argument("-i1","--input1",help="the first argument")
parser.add_argument("-i2","--input2",help="the second argument")
parser.add_argument("-o","--output",help="the third argument")
args = parser.parse_args()
file1=open(args.input1,'r')
file2=open(args.input2,'r')
file3=open(args.output,'w')
dict_id={}
for eachline in file1:
    eachline=eachline.strip('\n')
    dict_id[eachline]=''
for line in file2:
    line=line.strip('\n')
    trans_id=re.search('transcript_id \"(.*?)\"\;',line.split('\t')[8])
    gene_id=re.search('gene_id \"(.*?)\"\;',line.split('\t')[8])
    code_id=re.search('class_code \"(.*?)\"\;',line.split('\t')[8])
    if trans_id.group(1) in dict_id:
        file3.writelines(gene_id.group(1)+'\t'+code_id.group(1)+'\n')
    else:
        continue
file1.close()
file2.close()
file3.close()
