# Counting number of possible alignments

In this assignment, we will implement a little dynamical programming algorithm to count the number of possible [Needleman-Wunsh](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm#Computer_stereo_vision) type alignments for two sequences.

## Input

The input for our program will be simply integer numbers which represent the length of two sequences.
Unlike our previous codes, the order of these numbers are not important, so these are implemented as **positional arguments** in the [core code](alignmentCount.py).
For example, you should be able to run your program simply as `python2 alignmentCount.py 9 10` for n=9 and m=10.

## Assignment

You are expected to implement functions to calculate the number of possible alignments when
  * Double gaps are not allowed
  * Double gaps are allowed

In practice, you will simply write 2 nested for loops in each function.
The solution for the first case is discussed in the lecture notes, and we went over the solution for the second case in the lab session, despite it being simple enough for you to derive.

## Output

Your program will simply print a sentence summing up the results.
This also is handled by the core code.
You might want to study the final print line to check out the string formatting features of python which we have not used before.

## Tips

  * As discussed in the lab, we are using numpy. Initializing the zero matrices, and filling the first rows and columns with ones are implemented using numpy functions for demonstration purposes. You are advised to study these but for the rest of this assignment you can simply access numpy arrays like you do python lists. 

  * You are advised to sanity check your results since you will be using your code in the quiz. Make sure :
    * Your matrices are symmetrical
    * You are matching the numbers reported in the lecture notes
