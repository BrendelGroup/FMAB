from Bio import SeqIO
from argparse import ArgumentParser

## Program to count kmers in a fasta file

# This function should count kmers and return the result in a dictionary.
# !! All possible kmers should be present in the dictionary,
# Even if they do not exist in the sequence. 

def count_kmers(sequenceList, k=2) :
    kmer_count = dict()
    
    # Note that you get a sequence list instead of a single sequence
    for sequence in sequenceList :
        ### Insert your code here 
        ### Goal : fill in kmer_count with counts for each possible kmer
        ### Note that your sequences are simple string objects this time so you do not need to use .seq

    return kmer_count

# This function should normalize kmer counts to provide conditional probabilities
# The last letter of the kmer is conditioned on the first k-1 

def normalize_counts(kmer_count, k=2) :
    kmer_prob = dict()

    ### Insert your code here
    ### Goal : normalize kmer_count to produce kmer_prob
    ### Remember to implement pseudocounts if you have not already

    return kmer_probs

if __name__ == '__main__' :

    # Define input parameters
    parser = ArgumentParser(description='Reads a fasta sequence and counts k-mers')
    parser.add_argument('-i', '--infile', help='input file in fasta format')
    parser.add_argument('-k', type=int, default=2, help='k as in k-mer')
    args = parser.parse_args()

    # Read the sequences on from the file
    sequences = [str(record.seq) for record in SeqIO.parse(args.infile, 'fasta') ]
    
    # Count all the kmers in these sequences
    counts = count_kmers(sequences,args.k)

    # Normalize counts to get probabilities
    probs = normalize_counts(counts)

    # Note that we print everything to stdout rather than write to a file
    for kmer in probs :
        print kmer, probs[kmer]

