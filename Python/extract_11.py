#!/usr/bin/env python
#count FPKM of transcripts
#python extract_11.py -i1 all_transcript.txt -i2 ZIKVnovel.tracking  -o fpkm.txt
import argparse
import re
parser = argparse.ArgumentParser(description="This is just a test")
parser.add_argument("-i1","--input1",help="the first argument")
parser.add_argument("-i2","--input2",help="the second argument")
parser.add_argument("-o","--output",help="the third argument")
args = parser.parse_args()
file1=open(args.input1,'r')
file2=open(args.input2,'r')
file3=open(args.output,'w')
code=['i','j','o','u','x']
dict_transcript={}
each=[]
num=[]
def getfpkm(content,marker):
    for i in range(len(content)):      
        if content[i] != '-':
            num=content[i].split(',')
            if len(num)==1:
                fpkm=content[i].split('|')[3]
                if float(fpkm) == 0.0:
                    continue
                if i%2 ==1:
                    rep=2
                    j=i-1
                else:
                    rep=1
                    j=i
                file3.writelines(str(fpkm)+'\t'+marker+'\t'+str(j)+'hpi_'+str(rep)+'\n')
            elif len(num)==2:
                fpkm=float(num[0].split('|')[3])+float(num[1].split('|')[3])
                if float(fpkm) == 0.0:
                    continue
                if i%2 ==1:
                    rep=2
                    j=i-1
                else:
                    rep=1
                    j=i
                file3.writelines(str(fpkm)+'\t'+marker+'\t'+str(j)+'hpi_'+str(rep)+'\n')
        else:
            continue
for each_transcript in file1:
    each_transcript=each_transcript.strip('\n')
    dict_transcript[each_transcript.split('\t')[0]]=each_transcript.split('\t')[1]
gene=''
for eachline in file2:
    eachline=eachline.strip('\n')
    each=eachline.split('\t')
    if each[3] in code:
        if each[0] in dict_transcript:
            getfpkm(each[4:],dict_transcript[each[0]])
    elif each[3] =='=':
        gene=each[2].split('|')[0]
        if gene in dict_transcript:
            getfpkm(each[4:],dict_transcript[gene])
    else:
        continue
file1.close()
file2.close()
file3.close()
