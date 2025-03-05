#!/usr/bin/perl
use strict;
use warnings;

# Check for correct number of arguments
if (@ARGV != 2) {
    die "Usage: $0 <token_file> <text_file>\n";
}

my ($token_file, $text_file) = @ARGV;

# Step 1: Read the token file into a hash
my %tokens;
open my $token_fh, '<', $token_file or die "Could not open '$token_file': $!";
while (my $line = <$token_fh>) {
    chomp $line;
    my ($key, $value) = split(/=/, $line, 2); # Split at the first '='
    $tokens{$key} = $value if defined $value; # Store key-value pair
}
close $token_fh;

# Step 2: Process the text file and replace keys with values
open my $text_fh, '<', $text_file or die "Could not open '$text_file': $!";
my @lines = <$text_fh>; # Read all lines
close $text_fh;

# Sort keys descending by length (longest first)
my @keys_sorted = sort { length($b) <=> length($a) } keys %tokens;

foreach my $line (@lines) {
    next if (index($line, '#') == 0);

    foreach my $key (@keys_sorted) {
        # Escape any regex special characters in keys for safety
        (my $escaped_key = $key) =~ s/([.*+?^\$\{\}\(\)|[\]\\])/\\$1/g;
        # Replace occurrences of complete words matching the key with its corresponding value
        $line =~ s/(^|,|\.|\s)$escaped_key($|,|\.|\s)/$1$tokens{$key}$2/g;
    }
}

# Step 3: Write modified lines back to the text file or a new file
open my $output_fh, '>', $text_file or die "Could not open output file: $!";
print $output_fh @lines; # Write modified lines to output file
close $output_fh;

print "Replacement complete. Modified file created as '$text_file'.\n";
