#!/usr/bin/env python

import sys
from argparse import ArgumentParser

parser = ArgumentParser(description='Calculate the percentage of each nucleotide in a DNA or RNA sequence')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input DNA or RNA sequence")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()

if all(base in 'ACGTU' for base in args.seq):
    length = len(args.seq)
    a_percentage = (args.seq.count('A') / length) * 100
    c_percentage = (args.seq.count('C') / length) * 100
    g_percentage = (args.seq.count('G') / length) * 100
    t_percentage = (args.seq.count('T') / length) * 100
    u_percentage = (args.seq.count('U') / length) * 100

    print(f"A: {a_percentage:.2f}%")
    print(f"C: {c_percentage:.2f}%")
    print(f"G: {g_percentage:.2f}%")

    if 'T' in args.seq:
        print(f"T: {t_percentage:.2f}% \n(DNA sequence)")
    elif 'U' in args.seq:
        print(f"U: {u_percentage:.2f}% \n(RNA sequence)")
else:
    print('The sequence is not DNA nor RNA')

