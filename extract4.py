#!/usr/bin/env python
#python extract4.py  -i1 de_name.txt  -i2 de.txt  -o de_final.txt 
import argparse
import sys
import re
import math
parser = argparse.ArgumentParser(description="This is just a test")
parser.add_argument("-i1","--input1",help="the first argument")
parser.add_argument("-i2","--input2",help="the second argument")
parser.add_argument("-o","--output",help="the third argument")
args = parser.parse_args()
file1=open(args.input1,'r')
file2=open(args.input2,'r')
file3=open(args.output,'w')
dict_id={}
dict_name={}
for eachline in file1:
    eachline=eachline.strip('\n')
    dict_id[eachline.split('\t')[0]]=eachline
for line in file2:
    line=line.strip('\n')
    gene=line.split('\t')
    if gene[0] in dict_id:
        if dict_name.get(gene[0]):
            dict_name[gene[0]].extend([[gene[7],gene[8],gene[13]]])
        else:
            dict_name[gene[0]]=[[gene[7],gene[8],gene[13]]]
for i in dict_name:
    value_zikv=0.0
    value_control=0.0
    w=0
    for j in dict_name[i]:
        value_zikv+=float(j[0])
        value_control+=float(j[1])
        w+=1
    value_zikv=value_zikv/w
    value_control=value_control/w
    file3.writelines(i+'\t'+str(value_zikv)+'\t'+str(value_control)+'\t'+j[2]+'\n')
file1.close()
file2.close()
file3.close()