T = int(input()) #test cases


for t_c in range(T):
    N,K = map(int, input().split()) # N- number of elements in A, K- number of steps of rotation
    A = list(map(int, input().split())) # A main array where rotation is to be applied
    #for i in range(K):
    #    A = A[-1:] + A[:-1]
    new_k = K%N
    new_A = A[-(new_k):] + A[:-(new_k)]
    print (*new_A, sep = ' ')
    
