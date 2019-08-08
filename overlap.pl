#!/usr/bin/perl
#extract target gene from HCV differential expression genes list
#overlap.pl   CNCI_index.txt   LncRNA_ref.gtf   novel_LncRNA_ref.gtf
use strict;
use warnings;
open "IN1","<",shift;
open "IN2","<",shift;
open "OUT",">",shift;
my %hash_id;
while(<IN1>){
	chomp;
	s/\s+//g;
	$hash_id{$_}=1;
	#print "$_\n";
}
while(<IN2>){
	chomp;
	my $string=(split "\t",$_)[8];
	my $id=(split "; ",$string)[1];
	my $key_id=(split '"',$id)[1];
	#print "$key_id\n";
	if(exists $hash_id{$key_id}){
		print OUT "$_\n";
	}
}
close IN1;
close IN2;
close OUT;