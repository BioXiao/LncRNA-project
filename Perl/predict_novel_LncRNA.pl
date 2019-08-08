#!/usr/bin/perl
#extract novel LncRNA from RNA-seq data by Benxia Hu 2015.09.09
#  perl  predict_novel_LncRNA.pl  -input1 Homo_sapiens.GRCh37.74.gtf -input2 HCV.combined.gtf    -output LncRNA_ref.gtf
#use strict;
#use warnings;
use Getopt::Long;
my($input1_file,$input2_file,$output_file,$input1,$input2,$output,$flag,$feature);
GetOptions('input1=s' => \$input1_file,'input2=s' => \$input2_file,'output=s' => \$output_file);
open $input1,"<",$input1_file;
open $input2,"<",$input2_file;
open $output,">",$output_file;
my (%hash_feature,%hash_id,%hash_count);
my (@raw_data);
while(<$input1>){
	chomp;
	$feature=(split "\t")[8];
	$feature=~/gene_name \"(.*?)\"\;/;
	$hash_feature{$1}=(split "; ",$feature)[0];	
}
while(<$input2>){
	chomp;
	my $list=(split "\t")[8];
	$list=~/class_code \"(.*?)\";/;
	my $flag=$1;
	next if ($flag eq 'c') || ($flag eq '=')|| ($flag eq 'e')|| ($flag eq 'p')|| ($flag eq 'r')|| ($flag eq 's')|| ($flag eq '.');
	my @code=split "; ",$list;
	push @{$hash_id{$code[1]}},[$_];
	$hash_count{$code[1]}+=1;
}
foreach(keys %hash_id){
	next if $hash_count{$_} == 1;
	my $length=0;
	my @seq;
	foreach my $key1(@{$hash_id{$_}}){
		foreach my $data(@$key1){
			@raw_data=split "\t",$data;
			my @pos=split "; ",$raw_data[8];
			my $name=(split '"',$pos[3])[1];
			if(exists $hash_feature{$name}){
				$pos[0]=$hash_feature{$name};
			}
			$raw_data[8]=join "; ",@pos;
			push @seq, join "\t",@raw_data;
			$length+=$raw_data[4]-$raw_data[3]+1;
		}
	}
	if ($length > 199){
		foreach my $key2(@seq){
			print $output "$key2\n";
		}
	}
}
close $input1;
close $input2;
close $output;
