# Rc4 Python Implementation
# Authors:
# Dustin Ray
# Tianyi Li
# TCSS 581 - Spring 2020


# Key Scheduling Alg accepts a keyseed as input
# and expands it to keystream. 
def KSA(key):

    keylength = len(key)

    # define S
    S = []

    # initialize S
    for i in range(0, 255):
        S[i] = i
    
    # define j
    j = 0

    # scheduling loop
    for i in range(0, 255):
        j = (j + S[i] + key[i % keylength]) % 256
        
        # swap values
        S[i], S[j] = S[j], S[i]

    return S

# function accepts S from above and generates a 
# pseudorandom number output to be used for encryption
def PRNGA(S):

    #define i and j    
    i = 0
    j = 0

    # this is broken, we need a way to loop 
    # infinitely here.
    idx = 0
    while idx <= len(S):
        
        # advance bit i + 1
        i = (i + 1) % 256

        # advance bit j + S[i]
        j = (j + S[i]) % 256
        
        # swap just like above
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        
        # since a stream is being generated, 
        # use yield instead of return
        yield K



    # driver of this implmentation
    # of RC4. Accepts key as input and calls other functions. 
    def mainAlg(key):

        #expand key using KSA defined above
        S = KSA(key)

        # generate pseudorandom output using function
        # defined above. 
        PRGA = PRNGA(S)

        return PRGA


