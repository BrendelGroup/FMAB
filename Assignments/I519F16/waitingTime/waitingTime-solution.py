from argparse import ArgumentParser
from random import random

# waiting_time takes a composition and a pattern
# it generates a random sequence with (approximately) the given composition
# until the given pattern is generated
# returns the number of steps it took to generate this pattern

def waiting_time(composition, pattern) :
    # Sanity check on composition
    assert abs( sum(composition.values())-1 ) < 0.01 , 'Probabilities do not add up to 1.'

    # Sanity check on pattern
    for letter in pattern :
        assert letter in composition, 'Pattern involves letters not specified in composition'

    pattern_size = len(pattern)
    sequence =''

    # Main loop
    while len(sequence) < pattern_size or sequence[-pattern_size:] != pattern :

        dice = random()
        limit=0
        for nuc in composition :
            limit += composition[nuc]
            if dice<limit :
                sequence += nuc
                break

    # Return length of the generated sequence
    return len(sequence)

### Defining program parameters
parser = ArgumentParser(description='Estimates the waiting time (in steps) until generation of given pattern and composition')
parser.add_argument('-p', '--pattern', help='waiting time until generating this pattern')
parser.add_argument('-n', type=int, default=1, help='number of random sequences to be generated')
# composition parameters
parser.add_argument('-A', type=float, default=0.25, help='probability of A')
parser.add_argument('-T', type=float, default=0.25, help='probability of T')
parser.add_argument('-C', type=float, default=0.25, help='probability of C')
parser.add_argument('-G', type=float, default=0.25, help='probability of G')
# parsing parameters
args=parser.parse_args()

# Composition is uniform by default, but can be changed using parameters
composition = dict()
composition['A']=args.A
composition['T']=args.T
composition['C']=args.C
composition['G']=args.G

# Sample waiting times
waiting_times = [ waiting_time(composition, args.pattern) for i in range(args.n)]

# Check out the new numpy functions we are using!
from numpy import mean, std, sqrt

# Print the mean waiting time and STANDARD ERROR of waiting time
print args.n, mean(waiting_times), std(waiting_times)/sqrt(args.n)
