#!/usr/bin/env python
#python test_18.py  -i novel_noncoding.txt  -o novel_noncoding_gene.txt 
import argparse
import sys
import re
parser = argparse.ArgumentParser(description="This is just a test")
parser.add_argument("-i","--input",help="the first argument")
parser.add_argument("-o","--output",help="the second argument")
args = parser.parse_args()
file1=open(args.input,'r')
file2=open(args.output,'w')
dict_id={}
for eachline in file1:
    eachline=eachline.strip('\n')
    gene_id=eachline.split('\t')[2]
    dict_id[gene_id]=''
for key in dict_id:
    file2.writelines(key+'\n')
file1.close()
file2.close()
