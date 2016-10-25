# Forward-backward argorithm

In this assignment, you will implement the [forward-backward algorithm](https://en.wikipedia.org/wiki/Forward%E2%80%93backward_algorithm) from scratch.
This does not require any novel knowledge of programming on top of what you have seen in the previous assignments, so you will not get a core code. 

## The algorithm

Forward-backward algorithm is very similiar to the viterbi algorithm and is discussed in the lecture notes. 
The difference is, when provided an observed sequence, forward-backward yields **posterior marginal probabilities** of all hidden states for each position, while viterbi only yields the **most likely hidden state**.
When you complete this assignment, you should realize these are not necessarily the same. 

## The input

Unlike the Viterbi assignment, you will need to parse your parameters from the input for this assignment. 
The input will be formatted as follows :

  * 2 integers n and m signifying number of states and alphabet size
  * n lines of initial probabilities
  * n x n lines of transition probabilities
  * n x m lines of emission probabilities

Which will look like this : 

nstates nalphabet
state1	prob
...
...	prob
...
staten	prob
state1 state2 prob
...
statei statej prob
...
state
state1 char1 prob
...
statei charj prob
...
staten charm prob

Your code should check for sanity of parameters and should refuse to run for broken parameters. 
An example sane [input file](sample_parameters.dat), representing the fair/biased coin example from the viterbi assignment is provided. 
Your code should take the parameter file as the -p parameter and should not run without it. 

## The program

Implement the viterbi and forward-backward algorithms as **seperate functions**. 
Comment your code very very well. 
There will be no partial credits in this assignment. 
You will be given a very small grace period to fix minor mistakes but it will be impossible for you to convince me your mistakes are minor unless your code has **excellent** comments. 

