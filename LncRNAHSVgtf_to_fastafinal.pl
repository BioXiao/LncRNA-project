#!/usr/bin/perl  
use strict;
use warnings;
open "IN1","<geneid.txt";
open "IN2","<LncRNAHSVgtf_to_fastatreat.fa";
open "OUT1",">LncRNAHSVgtf_to_fastafinal.fa";
my (%hash1,%hash2);
while (<IN1>){
    chomp;
    $hash1{$_}=0; 
}
local $/ = ">";
<IN2>;
while (<IN2>){
    my $id1=(split /\n/,$_)[0];
    my $id2=(split /\s+/,$id1)[2];
    my $id3=(split /\=/,$id2)[1];
    if (exists $hash1{$id3}){
        print OUT1 "$_";
    }   
}
local $/ = "\n";
close IN1;
close IN2;
close OUT1;
open "IN3","<LncRNAHSVgtf_to_fastafinal.fa";
my $i;
while (<IN3>){
    $i++ if /\>/;
}
print "$i\n/";
close IN3;