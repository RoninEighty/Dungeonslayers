#!/bin/sh

# Exit on error
set -e

# tokens.txt should contain the tokens and their replacements in the format token=value. 
# perl reads these pairs and performs the replacements in FILE, outputting the result to FILE.tmp

TOKEN_FILE=$1
REPLACE_FILE=$2

perl -pe '
  use utf8;
  BEGIN {
    open my $fh, "<", "'${TOKEN_FILE}'" or die "Cannot open '${TOKEN_FILE}': $!";
    while (<$fh>) {
      chomp;
      my ($old, $new) = split /=/;
      print $old;
      $replacements{"\Q${old}\E"} = $new;
    }
    close $fh;
  }
  s/(\w+)/$replacements{$1} || $1/e;
' ${REPLACE_FILE} > ${REPLACE_FILE}.tmp