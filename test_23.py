#!/usr/bin/env python
#python test_23.py  -i1 annotated_lncRNA.txt  -i2 de_single.txt  -o annotated_lncRNA_expression.txt
#python test_23.py  -i1 noncoding_name.txt  -i2 de_single.txt  -o novel_lncRNA_expression.txt  
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
    dict_id[eachline.split('\t')[0]]=eachline
for line in file2:
    line=line.strip('\n')
    #gene_id=line.split('\t')[2]  #annotated
    gene_id=line.split('\t')[1]   #novel
    if gene_id in dict_id:
        file3.writelines(line+'\t'+dict_id[gene_id]+'\n')
    else:
        continue
file1.close()
file2.close()
file3.close()

