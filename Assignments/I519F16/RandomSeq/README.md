# Generate a random sequence

In this assignment, you will :

1. Read a given sequence in [FASTA format](https://en.wikipedia.org/wiki/FASTA_format)
2. Determine its composition (nucleotide frequencies)
3. Generate random sequences with the same composition
4. Write the resulting random sequences to a file in FASTA format

You are provided a core program written in python.
If you choose to use that and complete the assignment in python, the 1st and 4th steps are coded in for you, so all you need to do is to fill in the lines for 3nd and 3rd steps.
In any case, you will be graded on the input/output of your program; if it can read the input fasta and generate an output fasta with the specified sequences, you get full grades regardless of the actual program.

## Prerequisites

**Python 2.7** is already installed in your VMs, along with the iPython interactive shell.

We are going to use some features from the **[Biopython](https://github.com/biopython/biopython.github.io/)** library.
This is a common library that has many useful data structures and functions for bioinformatics and it is already packaged for Ubuntu (therefore mint).
You can install it to your VM simply by typing :

`sudo apt-get install python-biopython python-biopython-doc`

**Remember, NEVER COPY-PASTE A SUDO COMMAND!!!**
This is a very simple command; while acting as the superuser using `sudo`, it tells you package manager, `apt-get` to download and `install` a package, namely `python-biopython`.
The second package, `python-biopython-doc` includes the documentation and is optional.
You should be able to handle such simple commands without mindless copy-pasting.
Because Linux is based on Ubuntu, which in turn has an enormous package repository, you can install many programs in this fashion. 
There is even a graphical interface, called **synaptic** that enables you to search and install such packages.

You will also need a text editor to modify the code.
Any text editor will do but some are more convenient than others.
You can :
  - Use xed, the default text editor that comes with your distribution
  - [Learn vim](http://vim.wikia.com/wiki/Tutorial) or emacs and learn how to work like a pro in a non-graphical environment
  - Download and install [Atom](https://atom.io/), a very popular graphical text editor
  - Install an integrated development environment (IDE) such as [Spyder](https://github.com/spyder-ide/spyder)

## Instructions (if you are using the core code and Python)

Open the file main.py and read it.
Go through and try the understand the structure of the program, it demonstrates good programming practices that you should familiarize yourself with.
This program handles parts 1 and 4, that is it reads and writes FASTA files using Biopython.
There are only two functions, **calc_comp** and **gen_sequence**, into which you should add your own code, there are no other modifications required to complete this assignment.
This is so that you can see how a well written program should behave and focus on the core calculations to finish the assignment.

You can run the core program with the help parameter using `python main.py -h` to get a short summary of parameters.


## Instructions (if you are using another programming language)

Comment your code well and add a README file to describe how to run it.
Your program will take 3 inputs :
1. Input file name
2. Output file name
3. Number of samples to be produced

Your program **must read and output standard FASTA files**.
As long as your output for a given input satisfies the conditions for any valid input, you will get the points.

Note that we are providing this option for the sake of openness.
We believe such openness to be good practice but it also requires strict specifications.
If you stray from the specifications, that is if your output is not readable by the Biopython's FASTA reader, **you will get no partial points**.
