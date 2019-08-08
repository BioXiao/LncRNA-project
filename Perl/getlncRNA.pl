#!/usr/bin/perl  
use strict;
use warnings;
open "IN1","<LncRNAID.txt";
open "IN2","<LncRNAHSVgtf_to_fastafinal.fa";
open "IN3","<LncRNAHSVDE.txt";
open "OUT1",">LncRNAHSVDEfinal.txt";
my (%hash1,%hash2,%hash3);
my @id;
while (<IN1>){
    chomp;
    next unless $_;
    $hash1{$_}=0;
}
local $/ = ">";   #定义换行符
<IN2>;            #除去第一个>
while (<IN2>){
    my $id1=(split /\n/,$_)[0];             #得到第一行
    my $id2=(split /\s+/,$id1)[0];          #对第一行分割
    my $id3=(split /\s+/,$id1)[2];       #对第一行第三列分割
    my $id4=(split /\=/,$id3)[1];
    next if exists $hash3{$id4};
    $hash3{$id4}=0;
    if(exists $hash1{$id2}){
        push @id,$id4;
    }   
}
local $/ = "\n";
while(<IN3>){
    chomp;
    $hash2{(split /\t/,$_)[2]}=$_;
}
foreach (@id){
    print OUT1 "$hash2{$_}\n";
}
close IN1;
close IN2;
close IN3;
close OUT1;
