from argparse import ArgumentParser
from numpy import zeros, argmax, ones

# function to parse the paraeters from a file

def parse_parameters(parameterFilePath) :
    initial, transition, emission = dict(), dict(), dict() 

    ## Your code here

    return initial, transition, emission

# viterbi will return the most likely hiden state sequence. 

def viterbi(initial, transition, emission, observed) :
    hidden = ''

    ## Your code here

    return hidden


# forward-backward will return maximum posterior probability hidden state sequence
# AND the marginal posterior probability distribution 

def forwardBackward(initial, transition, emission, observed) :
    hidden = ''
    prob = zeros([len(initial), len(observed)])
    
    ## Your code here
    
    return hidden, prob

if __name__ == '__main__' :

    # Define program parameters
    parser = ArgumentParser(description='Generic Hidden Markov Model solver')
    parser.add_argument('-p', help='parameter file')
    parser.add_argument('-o', help='observed sequence')
    args = parser.parse_args()

    initial, transition, emission = parse_parameters(args.p)

    print viterbi (initial, transition, emission, args.o)
    mmpseq, prob = forwardBackward (initial, transition, emission, args.o)
    print mmpseq
    print prob.T
    
