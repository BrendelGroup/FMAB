# Python code to test the input/output pairs for submitted assignments

# We use the classic argparse library to parse our parameters
from argparse import ArgumentParser
# Make sure you have Biopython installed by following the instructions on README
from Bio import SeqIO

# calc_comp takes a sequence and calculate nucleotide frequencies

def calc_comp(sequence) :
    comp = dict()

    for nuc in sequence.seq :
        if nuc in comp :
            comp[nuc] += 1
        else : 
            comp[nuc] = 1

    for nuc in comp :
        comp[nuc] /= float(len(sequence))

    return comp


parser = ArgumentParser(description='Reads two fasta sequences and compares their compositions.')
parser.add_argument('-i', '--infile', help='input file in fasta format')
parser.add_argument('-o', '--outfile', help='output file in fasta format')
args=parser.parse_args()

input_sequence = SeqIO.read(args.infile, 'fasta')
output_sequence = SeqIO.read(args.outfile, 'fasta')

comp1 = calc_comp(input_sequence)
comp2 = calc_comp(output_sequence)

flag=True
for nuc in comp1 :
    diff = comp1[nuc]-comp2[nuc]
#    print '{}\t{:.2f}\t{:.2f}\t{:.2f}'.format(nuc, comp1[nuc], comp2[nuc], diff)
    flag = flag and abs(diff)<0.01

from sys import exit

if flag :
    print 'compositions same'
    exit(0)
else :
    print 'compositions different'
    exit(1)
