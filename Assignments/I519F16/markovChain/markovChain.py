from argparse import ArgumentParser
from random import random
import sys

# Function to generate initial (marginal) probabilities from conditional probabilities
def generate_init_prob(cond_prob) :
    initial=dict()

    ### Insert your code here
    ### Goal : get marginal probabilities for A,C,T,G
    ### e.g. P(A) from P(A|A), P(A|T), P(A|C), P(A|G)

    return initial

def generate_markov(length, cond_prob, order=1) :

    sequence=''

    # Generate initial probabilities from conditional probabilities
    init_prob = generate_init_prob(cond_prob)

    ### Insert your code here
    ### Goal 1 : generate first character

    assert len(sequence) == order, 'First character was not generated'

    ### Insert your code here
    ### Goal 2 : generate rest of the sequence

    assert len(sequence) == length, 'Sequence is wrong length'

    return sequence


if __name__ == '__main__' :

    # Define input parameters
    parser = ArgumentParser(description='Generates a random sequence using a markov chain')
    parser.add_argument('-o', '--order', type=int, default=1, help='order of markov chain')
    parser.add_argument('-l', '--length', type=int, default=10, help='length of sequences')
    parser.add_argument('-n', '--number', type=int, default=1, help='number of sequences')
    args = parser.parse_args()

    # Read the parameters from stdin
    cond_prob = dict()
    for line in sys.stdin :
        kmer, prob = line.strip().split()
        cond_prob[kmer] = float(prob)

    # Print n random sequences to stdout
    for i in range(args.n) :
        print generate_markov_1 (args.length, cond_prob)
