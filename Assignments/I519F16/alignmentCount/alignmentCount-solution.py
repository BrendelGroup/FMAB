from argparse import ArgumentParser
# we are using numpy for our matrices
import numpy as np

# Function to calculate number of possible alignments
# If double gaps are allowed

def alignCount_allowDoublegap(n,m) :
    # initial matrix full of zeros
    mat = np.zeros([n+1,m+1],dtype=int) 
    
    # fill first row and column with ones
    mat[0,:] = np.ones(m+1)
    mat[:,0] = np.ones(n+1)

    # dynamical programming loop to fill the rest of it
    for i in range(1,n+1) :
        for j in range (1,m+1) :
            mat[i][j] += mat[i-1][j-1]
            mat[i][j] += mat[i-1][j]
            mat[i][j] += mat[i][j-1]

    # return the right bottom corner
    return mat[-1][-1]


# Function to calculate number of possible alignments
# If double gaps are not allowed

def alignCount_forbidDoublegap(n,m) :
    # initial matrix full of zeros
    mat = np.zeros([n+1,m+1],dtype=int) 
    
    # fill first row and column with ones
    mat[0,:] = np.ones(m+1)
    mat[:,0] = np.ones(n+1)
   
    # dynamical programming loop to fill the rest of it
    for i in range(1,n+1) :
        for j in range (1,m+1) :
            mat[i][j] += sum(mat[i-1,0:j])
            mat[i][j] += sum(mat[0:i,j-1])
            mat[i][j] -= mat[i-1][j-1]

    # return the right bottom corner
    return mat[-1][-1]

if __name__ == '__main__' :

    # Define program parameters
    parser = ArgumentParser(description='Reads a fasta sequence and counts k-mers')
    parser.add_argument('n', type=int, help='length of first sequence')
    parser.add_argument('m', type=int, help='length of second sequence')
    args = parser.parse_args()

    # Call the functions
    noDgaps = alignCount_forbidDoublegap(args.n, args.m)
    yesDgaps = alignCount_allowDoublegap(args.n, args.m)

    # Print the results
    print 'For sequences of length {} and {}, there are \n{} possible alignments if we do not allow double gaps \n{} alignments if we allow double gaps.'.format(args.n,args.m,noDgaps, yesDgaps)

