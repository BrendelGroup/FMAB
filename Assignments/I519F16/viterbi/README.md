# Hidden Markov model

In this assignment we will implement the [Viterbi algorithm](https://en.wikipedia.org/wiki/Viterbi_algorithm) to find the most likely hidden state sequence in a [Hidden Markov Model](https://en.wikipedia.org/wiki/Hidden_Markov_model) which I will call **HMM** in this document.

## Input

The parameters to define a HMM can get complicated to parse due to different ways of representing them.
In this assignment, we therefore decided to **hard-code** the parameters in your program in a unambiguous, dictionary based representation.
You should examine the advantages and disadvantages of this solution; you do not have to prepare example input files, but you have to modify your code every time you want to change your parameters.
Think about cases in which this might be a feasible solution.

The only input your program will take will be the **observed sequence**.
Once you are done, you should be able to run it like `python hiddenMarkov.py HHHTTHTHTH`.

## Assignment

### Model

The parameters hard-coded into your [core code](hiddenMarkov.py) represent a coin toss, which can result in a head (H) or tail (T).
We have two coins, one is fair (F) and the other is biased (B) to yield T with higher probability.
Of course, we also have the transition probabilities between a fair and biased coin.

We observe a sequence of such coin tosses and we calculate the most likely sequence of used coins.

### Algorithm

The solution is obtained by the classical Viterbi algorithm.
The [wikipedia page](https://en.wikipedia.org/wiki/Viterbi_algorithm) has a very nice pseudocode which you can use for hints.
As usual, you will insert a few lines into the provided [core code](hiddenMarkov.py) to make it functional.
Even the traceback part is implemented for your convenience, so you only need to figure out how to fill the dynamical programming matrix.

My implementation in this case is only 4 additional lines to the core code, but yours may be a little longer.

## Output

The program will simply output the most likely hidden sequence.

## Notes

We are using python dictionaries to make our code more comprehensible to humans, whereas a computer scientist might prefer a pure matrix implementation.
In practice, there are extremely fast implementations of this algorithm which you would likely use rather than writing your own.
In such proof-of-concept or rapid prototyping applications, it is almost always preferable to have easier to understand code at the cost of some performance.
