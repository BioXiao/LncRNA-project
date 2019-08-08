#!/usr/bin/perl  
use strict;
use warnings;
open "IN1","<LncRNAHSVgffread.fa";
open "IN2","<LncRNAHSVgtf_to_fasta.fa";
open "OUT1",">LncRNAHSVgtf_to_fastatreat.fa";
my (%hash1,%hash2);
while (<IN1>){
    chomp;
    if (/\>/){
        $_=~s/^>(.+)/$1/;
        $hash1{(split /\s+/)[0]}=$_; 
    }
}
while (<IN2>){
    chomp;
    if (/\>/){
        my @pos=split /\s+/;
        $hash2{$pos[1]}=0;
        if (exists $hash1{$pos[1]}){
            print OUT1 "$pos[0]\t$hash1{$pos[1]}\t$pos[2]\t$pos[3]\n";
        }   
    }else{
        print OUT1 "$_\n";
    }
}
close IN1;
close IN2;
close OUT1;
