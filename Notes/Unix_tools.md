# Fundamental Unix toolbox

By now, we have an idea on the filesystem and we know how to navigate it.
Presumably we have some files containing both programs and data.
So how do we interact with them?

You will find that there are many simple programs installed on posix systems that are used to interact with files.
Consider these your basic tools, like screwdrivers and a hammer.
They are not fancy, by any means of the definition, but everyone must know how about their basic usage.
These are both essential for everyday usage of your posix system and also become extremely powerful tools in the right hands and circumstances.

Some of the fancier tools, like awk and sed, can do impressive things and you will learn them with time, by experience, but these simple ones you must know by heart.
Note that all of these canonical tools have very well written manpages, do not hesitate to refer to them
First line (italic) of each following section is the tools description from its manfile.

## echo

*echo - display a line of text*

`echo` is probably the simplest tool available, it displays a given string.
The canonical 'hello world' program for bash in fact consists of a single line.

 `echo 'Hello world!'`

Note the usage of quotes, which is usually good practice.
`echo` may seem useless by itself but it will be very useful when you write small bash scripts and you want it to display some information.
You may think of it like the 'print' command for bash.

It can also be used to display [environment variables](https://en.wikipedia.org/wiki/Environment_variable) on an interactive shell. Displaying your PATH, for example, can be very useful.

`echo $PATH`  

You can also **pipe** the output of echo to a file, which is very useful for creating simple files.

`echo 'file with a single line' > newfile`

## cat

*cat - concatenate files and print on the standard output*

`cat` will be useful in two scenarios :

You have a small file that you want to quickly see in the terminal :

`cat smallfile`

You have a bunch of files that you  want to join ([concatenate](https://en.wikipedia.org/wiki/Concatenation)) :

`cat file1 file2 file3 > newfile`

This is especially useful in combining fasta files together since the format allows simply appending files one after another.

`cat some_sequences.fasta other_sequences.fasta > combined.fasta`

##### Pro tip :

There is a version of `cat`, namely `zcat` that will work directly on compressed files, so you don't have to uncompress them before `cat`ing.

## head and tail

  * *head - output the first part of files*
  * *tail - output the last part of files*

`head` and `tail` are very useful when you have large files which you cannot display in a single screen.
For example, if you have a 300 MB FASTA file, and you just want to see the first line (description), you can do

`head -n 1 very_large.fasta`

which would save you the trouble of opening the whole thing.
Also note that both `head` and `tail` take a `-n` parameter which specifies the number of lines to be displayed. **Can you figure out how many lines they display if -n is not specified?**  

Or maybe you have a 4 gb file that is column formatted.
You are interested in the last few lines, but column headers are in the beginning of the file.

`head -n 1 very_large_file; tail -n 5 very_large_file`

will do in a pinch.
In bioinformatics projects, you will encounter a lot of files which you cannot conceivably load at once.
Sneaking peaks with `head`, `tail` and `grep` will be essential.

## grep

*grep, egrep, fgrep - print lines matching a pattern*

Once you are naturally using `head` and `tail` in your work, learning `grep` is the next logical step.
To take full advantage of grep, you will need to learn a little about [regular expressions](https://en.wikipedia.org/wiki/Regular_expression), but the basic usage is pretty straightforward.

Maybe you have a multi-fasta file, and you want to quickly list the sequences that are in it?
We all know description lines start with a >, so

`grep '>' many_sequences.fasta`

will only display lines containing the character > and will be extremely efficient for this job.

## less

*less - opposite of more*

So far, we have been printing all or parts of files in the terminal (stdout), but sometimes, even the segment of the file that we are interested in is too large.
`less` is a *pager* which will print a file to the terminal in an interactive fashion so that you can scroll, search, highlight etc.
Note that the manpage explanation is a wordplay on a primitive version of `less`, which was called `more`.
`less` is fairly fast for even GB size files, since it does not have to read the entire file to display.
Also note that *a pager is not an editor*, which means you can only display files with less and not modify them.

`less longfile`

#### Pro tip :

Less has vi-like key bindings so that you can :
  * hit **g** to go to the beginning of the document
  * hit **G** to go to the end of the document
  * hit **/**, followed by a pattern (and enter) to search that pattern in the file.
  * hit **h** to display the help documentation including these commands

## wc

*wc - print newline, word, and byte counts for each file*

If you want to get some stats on a file without actually 'looking' at it, you can use `wc` on it.
I most often use it with the parameter `-l` to get the number of lines in a file.
Looking back to out multi-fasta example, if I cannot be bothered to count the sequences, I can pipe the output of `grep` to `wc`, like so :

 `grep '>' many_sequences.fasta | wc -l`

 which will provide me the number of sequences in this FASTA file.

## wget

*Wget - The non-interactive network downloader.*

We use `wget` to download filer, for which we already have urls for.
The basic usage simply takes an url and downloads it to the *working directory*.

`wget ftp://ftp.plantbiology.msu.edu/pub/data/Eukaryotic_Projects/o_sativa/annotation_dbs/pseudomolecules/version_7.0/all.dir/all.chrs.con`

## touch

`touch` will 'touch' a file, which means :
  * if the file exists, its 'modification time' will be updated to current time
  * if the file does not exist, an empty file will be created

This can be surprisingly useful to create a bunch of empty files to initiate certain directory structure, or marking some files 'current' to avoid unnecessary updating by certain scripts.   

## awk and sed

  * *awk - pattern scanning and processing language*
  * *sed - stream editor for filtering and transforming text*

`awk` and `sed` are the two general purpose POSIX workhorses.
These are extremely powerful programs, which can accomplish pretty much any task you can imagine.
If you invest a little time in learning these two, they will amortize themselves many fold by saving you enormous amounts of time later on.

`awk` performs column-based operations on column formatted data (think hard-core MS excel).
While `awk` offers a complete programming language, most people only use very short programs called [one liners](http://www.pement.org/awk/awk1line.txt).
I recommend you learn just enough `awk` to understand such one liners and keep a handy collection of them for quick use.
In its basic usage, `awk` performs an action on each line that satisfies a pattern.

`sed` is a stream editor that is most commonly used for find/replace operations on large files.
To take full advantage of `sed`, like `grep`, you need to know a little about regular expressions.

Proper introduction of `awk` and `sed` are well beyond the scope of this class excellent tutorials are available online.
It is strongly advised that you familiarize yourself a little with both.

## bash scripting

Writing a bash script can be as easy as writing consecutive commands into a file rather than a command line.
If you want your work to be reproducible, such simple bash scripts can also be commented to serve as documentation, which is very convenient.

Bash, however, is a terrible general-purpose programming language.
It has a very inconvenient syntax that can give even the seasoned coder headaches.
You should, in general, try to avoid bash for anything more complicated than chaining a few programs together.

Write your programs in your programming language of choice, in such a way that they can be glued together with trivial bash scripts.
Do not expect bash to do anything 'intelligently'.

[This wiki](http://mywiki.wooledge.org/BashPitfalls) helped me a lot when troubleshooting my lousy bash programs.
