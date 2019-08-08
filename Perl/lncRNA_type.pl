#!/usr/bin/perl
#extract target gene from HCV differential expression genes list
#lncRNA_type.pl  novel_LncRNA_ref.gtf novel_lncRNA_sig.txt     novel_lncRNA_sig_type.txt
use strict;
use warnings;
open "IN1","<",shift;
open "IN2","<",shift;
open "OUT",">",shift;
my %hash_id;
while(<IN1>){
    chomp;
    my $string=(split "\t",$_)[8];
    $string=~/class_code \"(.*?)\";/;
    my $class_code=$1;
    my $id=(split "; ",$string)[0];
    my $gene_id=(split '"',$id)[1];
    $hash_id{$gene_id}=$class_code;
}
while(<IN2>){
    chomp;
    my $gene_name=(split "\t",$_)[1];
    if(exists $hash_id{$gene_name}){
        print OUT "$_\t$hash_id{$gene_name}\n";
    }
}
close IN1;
close IN2;
close OUT;
