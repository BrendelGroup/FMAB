from argparse import ArgumentParser
from random import random
import sys

# Function to generate initial (marginal) probabilities from conditional probabilities
def generate_init_prob(cond_prob) :
    init_prob=dict()

    # Assuming simplest alphabet
    alphabet = ['A','T','C','G']
    init_prob = { letter:0 for letter in alphabet }

    # Sanity check
    prob_total = sum(cond_prob.values())    # Sum of conditionals
    k = len(cond_prob.keys()[0])            # Inferred k 
    a_size = len(alphabet)                  # alphabet size
    assert abs(prob_total-a_size**(k-1))<0.01 , 'Conditional probabilities do not add up to {}.'.format(a_size**(k-1)) 
    
    # Add conditionals to get marginals for the last char in kmer
    for kmer in cond_prob :
        last_char = kmer[-1]
        assert last_char in init_prob, 'kmer {} is looking weird.'.format(kmer)
        init_prob[last_char] += cond_prob[kmer]

    # Normalize 
    for nuc in init_prob :
        init_prob[nuc] /= prob_total
    
    return init_prob

def generate_markov(length, cond_prob, order=1) :

    sequence=''

    # Generate initial probabilities from conditional probabilities
    init_prob = generate_init_prob(cond_prob)

    ### Goal 1 : generate first order characters
    for i in range(order) :
        dice = random()
        limit = 0
        for nuc in init_prob :
            limit += init_prob[nuc]
            # We add the letter that dice hits
            if dice<limit :
                sequence += nuc
                break

    assert len(sequence) == order, 'First {} character(s) were not generated'.format(order)

    ### Goal 2 : generate rest of the sequence

    for i in range(length-order) :
        dice = random()
        limit = 0
        last=sequence[-1]
        
        for nuc in ['A','C','T','G'] :
            limit += cond_prob[last+nuc]
            # We add the letter that dice hits
            if dice<limit :
                sequence += nuc
                break

    assert len(sequence) == length, 'Sequence is wrong length'

    return sequence


if __name__ == '__main__' :

    # Define program parameters
    parser = ArgumentParser(description='Generates a random sequence using a markov chain')
    parser.add_argument('-o', '--order', type=int, default=1, help='order of markov chain')
    parser.add_argument('-l', '--length', type=int, default=10, help='length of sequences')
    parser.add_argument('-n', '--number', type=int, default=1, help='number of sequences')
    args = parser.parse_args()

    # Read model parameters from stdin
    cond_prob = dict()
    for line in sys.stdin :
        kmer, prob = line.strip().split()
        cond_prob[kmer] = float(prob)

    # Print n random sequences to stdout
    for i in range(args.number) :
        print '>'
        print generate_markov (args.length, cond_prob)
