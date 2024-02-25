#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

# Create an ArgumentParser object with a description
parser = ArgumentParser(description='Classify a sequence as DNA or RNA')

# Define command-line arguments
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif")

# Check if no arguments were provided, print help message and exit if so
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse the command-line arguments
args = parser.parse_args()

# Convert the sequence to uppercase for case-insensitive comparison
args.seq = args.seq.upper()

# Check if the sequence contains only valid DNA or RNA characters
if re.search('^[ACGTU]+$', args.seq):
    # Check if 'T' (thymine) is present in the sequence, indicating DNA
    if re.search('T', args.seq):
        print('The sequence is DNA')
    # Check if 'U' (uracil) is present in the sequence, indicating RNA
    elif re.search('U', args.seq):
        print('The sequence is RNA')
    # If neither 'T' nor 'U' is present, it could be either DNA or RNA
    else:
        print('The sequence can be DNA or RNA')
else:
    # If the sequence contains invalid characters, it's neither DNA nor RNA
    print('The given sequence is not DNA nor RNA')

# If a motif is provided, perform motif search in the sequence
if args.motif:
    # Convert the motif to uppercase for case-insensitive comparison
    args.motif = args.motif.upper()
    # Print message indicating motif search is enabled
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end='')
    # Perform motif search in the sequence
    if re.search(args.motif, args.seq):
        print("Motif FOUND")
    else:
        print("Motif NOT FOUND")

