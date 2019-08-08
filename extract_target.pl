#!/usr/bin/perl
#extract target gene(such as LncRNA,miRNA) from HSV-1 differential expression genes list
use strict;
use warnings;
open "IN1","<",shift;
open "IN2","<",shift;
open "OUT",">",shift;
my (%hash_id1,%hash_id2);
while(<IN1>){
	chomp;
	$hash_id1{$_}=0;
}
my $string=<IN2>;
print OUT "$string";
while(<IN2>){
	chomp;
	my $id1=(split "\t",$_)[2];
	if(exists $hash_id1{$id1}){
		print OUT "$_\n";
		#print "$id1\n";
	}
}
close IN1;
close IN2;
close OUT;
