#! /usr/bin/perl -w
#
# xmkqa.pl
# Version of September 7, 2016.  Volker Brendel

use strict; 
use Getopt::Std;

my $subject = "Linux";
my $subsubject = "bash";
my $type = "explain";
my $difficulty = "easy";

my $USAGE="\nUsage: $0 [-h] [-s subject] [-r subsubject] [-t type] [-d difficulty]\n

** This script creates a qa entry for a quiz library yaml file.

   Example: $0 -s Linux -r bash -t provide -d moderate >> newqa
            vi newqa
     (then substitute \"fill in question text here\" and
      \"fill in answer text here\" in newqa and add the file to your library)
   \n";


my %args;
getopts('hs:r:t:d:', \%args);

if (defined($args{h})) {
  print $USAGE;
  exit 1;
}
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
