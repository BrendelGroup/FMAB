# Estimate waiting time for a pattern

In this assignment you will write a program that will generate a random sequence until it generates a given pattern, and reports how many steps it took to get there.

## Input

The provided [core program](waitingTime.py) takes 3 parameters :

  * -p : Pattern for which we are calculating the waiting time
  * -n : Number of experiments (samples, random sequences) we will do
  * -A,-C,-T,-G : Optional composition parameters. If none are provided, uniform composition is assumed by default. Note that you need to provide either all or none of them. *(Why?)* There is an assertion to make sure this was done properly. *(Where?)*


## Assignment

You will fill in the gap in the **waiting_time()** function.
It should generate a random sequence until the given pattern comes up, then stop and report the length of the sequence generated.

Note that the main loop of this assignment is essentially the same as the [first assignment](../randomSeq).
My implementation is 8 lines and 7 of these are shared between the two.
Instead of a **for loop**, this time you should use a **while loop**.

## Output

The provided [core program](waitingTime.py) prints 3 numbers :

  * n : number of experiments
  * mean : mean of waiting times observed in experiments
  * err : [Standard error](https://en.wikipedia.org/wiki/Standard_error) of the mean

## Final report

You are expected to plot the output for different n, using error bars for showing the standard error.
Use [matplotlib](http://matplotlib.org/) or any other plotting program of your choice.
Use exponentially increasing n such as n=,4,8,16,3,64,128,256,512,1024,2048 and observe how the standard error changes.
Answer the questions :

  * What is a reasonable n for pattern size 2?
  * What is a reasonable n for pattern size 5?
  * What is a reasonable n for pattern size 10?
  * What is a reasonable n for pattern size 100?
  * What does it mean to have a reasonable n?
  * Are your numbers consistent with those calculated in the lecture notes?
