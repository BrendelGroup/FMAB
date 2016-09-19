# Counting k-mers

In this assignment we will read a bunch of sequences from a multi-fasta file and count all the k-mers in it.
We will then normalize the counts to probability distributions and output these probabilities.

## Input

The input will be a multi-fasta file with a group of sequences.
In a machine learning context, this would be called a **training set**.
We are **training our statistical model** on these given sequences.

We are going through these sequences using Biopython's fasta parsing capabilities.
Note that the only difference from the [previous assignment](../RandomSeq) is that we have multiple sequences rather than one, but this is handled in the [core code](kmerCount.py) provided so you do not have to worry about it.

## Assignment

In the core python code, you are provided 2 positions to insert your code, these are in functions `count_kmers()` and `normalize_counts()`.

### Counting

You will count how many times each kmers occurs in the given sequences.

  * You need to include all possible kmers, including those that do not occur in the sequence in your output
  * At this point you may choose to add pseudocounts or not, to handle 0 counts later on
  * We will only test your program with k=2, but you are expected to write the function to work with any k

### Normalizing

You will normalize kmer counts to generate conditional probabilities for the 4 bases.
Each base will be conditioned on the preceding (k-1)mer, and probabilities should sum up to 1 accordingly.
For example,
  * for k=2, each base will be conditioned on the preceding base : e.g. P(A|C)
  * for k=3, each base will be conditioned on the preceding 2 bases : e.g. P(A|AT)  
  * for k=4, each base will be conditioned on the preceding 3 bases : e.g. P(A|ATC)

Again, we will only test your code for k=2 but your function should be able to handle any k and normalize accordingly.
 If you have not done so in the previous function, you may add pseudocounts here.

## Output

The output of your program will be printed to stdout.
For each line, we will print a kmer and the associated probability.
For example, a line that looks like `ACG  0.12` will imply P(G|AC)=0.12.
As a simple sanity check, your program should always print 4^k lines for a given k.

The formatting of the output is handled by the [core code](kmerCount.py), provided that you fill in the dictionaries appropriately.
We will then use this output as input for the [markov chain assignment](../markovChain), providing the parameters of our model.
