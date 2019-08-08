#!/usr/bin/env python
#python test_22.py  -i de.txt   -o de_single.txt
import argparse
import sys
import re
parser = argparse.ArgumentParser(description="This is just a test")
parser.add_argument("-i","--input",help="the first argument")
parser.add_argument("-o","--output",help="the second argument")
args = parser.parse_args()
file1=open(args.input,'r')
file2=open(args.output,'w')
eachline=''
each=[]
name=''
seq=''
for eachline in file1:
    eachline=eachline.strip('\n')
    each=eachline.split('\t')
    if each[2].find(','):
        for name in each[2].split(','):
            each[2]=name
            seq='\t'.join(each)
            file2.writelines(seq+'\n')
file1.close()
file2.close()
