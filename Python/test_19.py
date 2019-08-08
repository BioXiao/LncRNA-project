#!/usr/bin/env python
#python test_19.py  -i novel_noncoding.txt    -o1 novel_induced_expression.txt  -o2 novel_inhibited_expression.txt
import argparse
import sys
import re
parser = argparse.ArgumentParser(description="This is just a test")
parser.add_argument("-i","--input",help="the first argument")
parser.add_argument("-o1","--output1",help="the second argument")
parser.add_argument("-o2","--output2",help="the third argument")
args = parser.parse_args()
file1=open(args.input,'r')
file2=open(args.output1,'w')
file3=open(args.output2,'w')
dict_id={}
for eachline in file1:
    eachline=eachline.strip('\n')
    line=eachline.split("\t")
    if (line[4]=="-" and line[5]=="-") and (line[6]!="-" or line[7]!="-"):
        file2.writelines(eachline+'\n')
    elif (line[6]=="-" and line[7]=="-") and (line[4]!="-" or line[5]!="-"):
        file3.writelines(eachline+'\n')
    else:
        continue
file1.close()
file2.close()
file3.close()
