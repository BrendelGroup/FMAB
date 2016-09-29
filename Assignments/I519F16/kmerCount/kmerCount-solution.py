from Bio import SeqIO
from argparse import ArgumentParser

## Program to count kmers in a fasta file

# This function should count kmers and return the result in a dictionary.
# !! All possible kmers should be present in the dictionary,
# Even if they do not exist in the sequence.

def count_kmers(sequenceList, k=2) :
    kmer_count = dict()
    
    # Generate all possible kmers
    kmerList=['']
    alphabet = ['A','T','C','G']
    i=0
    while i<k :
        tmp = list()
        for mer in kmerList :
            for letter in alphabet :
                tmp.append(mer+letter)
        kmerList=tmp
        i+=1

    # Start each kmer with 1 pseudocount
    # Note that there are better ways to do this
    kmer_count = {kmer:1 for kmer in kmerList}
    
    # Count all the kmers in all the sequences
    for sequence in sequenceList : 
        for i in range (len(sequence)-k+1)  :
            kmer = sequence[i:i+k]
            assert kmer in kmer_count
            kmer_count[kmer] += 1

    return kmer_count

# This function should normalize kmer counts to provide conditional probabilities
# The last letter of the kmer is conditioned on the first k-1

def normalize_counts(kmer_count, k=2) :
    kmer_prob = dict()

    # Count numer of each (k-1)mer (prefix) occurs
    cond_counts = dict()
    for kmer in kmer_count :
        prefix = kmer[:-1]
        if prefix in cond_counts :
            cond_counts[prefix] += kmer_count[kmer]
        else :
            cond_counts[prefix] = kmer_count[kmer]


    # Normalize by prefix counts
    for kmer in kmer_count :
        prefix = kmer[:-1]
        kmer_prob[kmer] = float(kmer_count[kmer])/cond_counts[prefix]

    return kmer_prob

if __name__ == '__main__' :

    # Define program parameters
    parser = ArgumentParser(description='Reads a fasta sequence and counts k-mers')
    parser.add_argument('-i', '--infile', help='input file in fasta format')
    parser.add_argument('-k', type=int, default=2, help='k as in k-mer')
    args = parser.parse_args()

    # Read training sequences from fasta file
    sequences = [str(record.seq) for record in SeqIO.parse(args.infile, 'fasta') ]

    # Count all the kmers in these sequences
    counts = count_kmers(sequences,args.k)

    # Normalize counts to get conditional probabilities
    probs = normalize_counts(counts)

    # Print the resulting conditional probabilities
    for kmer in probs :
        print kmer, probs[kmer]

    # Note that we print everything to stdout rather than write to a file
    # User has the option to redirect to a file
