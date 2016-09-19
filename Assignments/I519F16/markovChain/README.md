# Markov chain random sequence generator

In this assignment, we will generate random sequences using a 1st order Markov chain generator.

##Input

The parameters of the Markov chain generator will be read from stdin.
For a 1st order Markov chain, we need a total of 16 conditional probabilities, each in a separate line.
A line such as `AT 0.21` implies P(T|A)=0.21; although it might look confusing at first, this notation is natural if you consider how we approximate these probabilities in the first place.

At this point it helps a lot if you have already done the [kmerCount](../kmerCount) assignment, because the output of that assignment can be directly piped to the input of this one.
Otherwise, it is highly recommended that you prepare some test parameters for piping into the input, rather than attempting to enter them manually.
If you still choose to enter parameters manually in stdin, you can terminate with Ctrl+d when you are done.

As usual, all input is handled by the [core code][markovChain.py] for your convenience.

## Assignment

### Initial probabilities

As discussed in the lab session, you need to use marginal probabilities to generate the first characters in a sequence.
You should fill in the function `generate_init_prob()` with appropriate code to derive marginal probabilities from conditional ones.
For example, you should combine P(A|A), P(A|T), P(A|C), P(A|G) to get P(A) etc.

### Markov chain generator

You should implement a Markov chain generator in the function `generate_markov()`.
Although this function takes an order parameter, it defaults to 1 and you are only expected to implement a 1st order Markov chain.
You are of course free to challenge yourself and generalize it.

## Output

The output will simply be printed to stdout.
This is also handled by the [core code][markovChain.py].

You are strongly encouraged to redirect your output to a file and practice analyzing it via simple command line tools such as cat, sed, grep, wc, etc.
