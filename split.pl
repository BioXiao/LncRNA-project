#!/usr/bin/perl
#���ն��ŷָ�ÿһ�еĻ���
use strict;
use warnings;
my ($input,$output);
open $input,"<",shift;
open $output,">",shift;
my $string=<$input>;
print $output "$string";
while(<$input>){
	chomp;
	my @name=split "\t";
	foreach(split ",",$name[2]){
		$name[2]=$_;
		print $output join "\t",@name,"\n";
		}
}
close $input;
close $output;