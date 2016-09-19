# We use the classic argparse library to parse our parameters
from argparse import ArgumentParser
# Make sure you have Biopython installed by following the instructions on README
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq


##### ALL MODIFICATIONS GO BELOW THIS LINE #####

from random import random

# calc_comp should take a sequence and calculate nucleotide frequencies
# it should return a dictionary

def calc_comp(sequence) :
    comp = dict()

    ##### Part 2 : Your composition calculating code goes here

    # We count each nucleotide in the sequence
    for nuc in sequence.seq :

        # An assertion is optional but a really good idea. 
        assert nuc in ['A','C','T','G'] , 'Weird nucleotide in sequence.'
        
        # If we have seen this nucleotide before, we increment the count
        if nuc in comp :
            comp[nuc] += 1
        # If not, then we should add it to the dictionary with count=1
        else : 
            comp[nuc] = 1

    # We divide each count by the length of sequence to get probabilities
    for nuc in comp :
        comp[nuc] /= float(len(sequence))

    # We return the dictionary with the probabilities

    return comp

# gen_sequence should take a nucleotide composition and an integer number
# it should return a random sequence with the given nucleotide composition and length

def gen_sequence(comp, length) :
    seq_string = ''

    ##### Part 3 : Your random sequence generating code goes here

    # Assertion is advised
    assert abs( sum(comp.values())-1 ) < 0.01 , 'Probabilities do not add up to 1.'
    
    # We generate a sequence of given length
    for i in range(length) :
        # Get a random number in [0,1)
        dice = random()
        limit=0
        # We divide [0,1) interval according to probabilities of each nucleotide
        for nuc in comp :
            limit += comp[nuc]
            # We add the letter that dice hits
            if dice<limit :
                seq_string += nuc
                limit = 0
                # Roll another dice for the next nucleotide
                break

    #####

    sequence = Seq(seq_string)
    return SeqRecord(sequence, id='Random Sequence', description=comp.__repr__())

##### ALL MODIFICATIONS GO ABOVE THIS LINE #####

### Part 0 : Argument Parsing
### We want out program to have easy-to-use parameters
### We are using the argparse library for this

parser = ArgumentParser(description='Reads a fasta sequence and generates random ones with the same compositon')
# input file
parser.add_argument('-i', '--infile', help='input file in fasta format')
# output file
parser.add_argument('-o', '--outfile', help='output file in fasta format')
# number of samples (default is 1)
parser.add_argument('-n', '--nrandom', type=int, default=1, help='number of random sequences to be generated')

args=parser.parse_args()

### Part 1 : Reading a FASTA file
### Biopython library makes this extremely easy using the SeqIO module

print 'Parsing the input sequence...'
input_sequence = SeqIO.read(args.infile, 'fasta')
# Note that this returns a SeqRecord object native to Biopython

# we can easily get the length of sequence
n_in_seq = len(input_sequence)

### Part 2 : Getting the nucleotide composition of the input sequence
print 'Calculating input sequence composition...'
input_comp = calc_comp(input_sequence)

### Part 3 : Generating the random sequences with the same composition
print 'Generating random sequences...'

# first define an empty list
random_sequences = list()

# then use a for loop to populate the list
for i in range(args.nrandom) :
    random_sequences.append( gen_sequence(input_comp, n_in_seq) )

# Here is 'the python way' of doing the same thing in a single line
# This uses 'list comprehension' which is a very versatile feature of python
# random_sequences = [ gen_sequence(input_comp, n_in_seq)) for i in range(args.nrandom) ]

### Part 4 : Writing random sequences to a FASTA file
print 'Writing sequences to file...'
SeqIO.write(random_sequences, args.outfile, 'fasta')
