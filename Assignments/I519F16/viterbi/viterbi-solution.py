from sys import argv
from numpy import zeros, argmax

# viterbi will return the most likely hiden state sequence. 

def viterbi(initial, transition, emission, observed) :
    
    # infer hidden states
    states = initial.keys()

    # initialize matrices
    score = zeros([len(states), len(observed)])
    trace = zeros([len(states), len(observed)], dtype=int)
    
    # forward pass
    for i, obs in enumerate (observed) :
        for j, st in enumerate (states) :
            if i == 0 :
                # first column
                score[j,i] = initial[st]*emission[st][obs]
                trace[j,i] = 0
            else :
                # rest of the columns
                score[j,i] = max ([score[k,i-1]*transition[pst][st]*emission[st][obs] for k,pst in enumerate(states)])
                trace[j,i] = argmax ([score[k,i-1]*transition[pst][st] for k,pst in enumerate(states)] )
    
    # trace back
    z = argmax(score[:,-1])
    hidden = states[z]

    for i in range(1,len(observed))[::-1] :
        z = trace[z,i]
        hidden += states[z]

    # return REVERSED traceback sequence
    return hidden[::-1]

if __name__ == '__main__' :

    # initial probabilities of (F)air and (B)iased coins
    initial = {'F':0.5, 'B':0.5}

    # transition probabilities btw (F)air and (B)iased coins
    transition = {'F':{'F':0.8, 'B':0.2}, 'B':{'F':0.2, 'B':0.8} }

    # emmision probabilites from (F)air and (B)iased coins
    emission = {'F':{'H':0.5, 'T':0.5}, 'B':{'H':0.2, 'T':0.8} }

    # observed sequence is the only input to the program
    sequence = argv[1]

    print viterbi (initial, transition, emission, sequence)
    

