#! /usr/bin/perl -w
#
# xmkqa.pl
# Version of September 6, 2016.  Volker Brendel

use strict; 
use Getopt::Std;

my $subject = "Linux";
my $subsubject = "bash";
my $type = "explain";
my $difficulty = "easy";

my $USAGE="\nUsage: $0 [-s subject] [-r subsubject] [-t type] [-d difficulty]\n


** This script creates a qa entry for a quiz library yaml file.

   \n";


my %args;
getopts('s:r:t:d:', \%args);

if (defined($args{s})) {
  $subject= $args{s};
}
if (defined($args{r})) {
  $subsubject= $args{r};
}
if (defined($args{t})) {
  $type= $args{t};
}
if (defined($args{d})) {
  $difficulty= $args{d};
}

my $i = 10000000 + int(rand(99999999));

printf("- id: %8d\n", $i);
printf("  subject: %s\n", $subject);
printf("  subsubject: %s\n", $subsubject);
printf("  type: %s\n", $type);
printf("  difficulty: %s\n", $difficulty);
printf("  prompt: |\n");
printf("      fill in question text here\n");
printf("  answer: |\n");
printf("      fill in answer text here\n");
