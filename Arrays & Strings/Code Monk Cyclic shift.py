
T =int(input())
for t_c in range(T):
    N,K = map(int,input().split()) # N- size of A, K- need to get maximum number i.e. B from A K times
    A = str(input()) 
    B = "" #B - will the maximun binary number formed after performing unknown shifts
    periodicity = -1
    for i in range (N):
        if (A > B):
                B = A
                displacement = i
        elif (B == A):
                periodicity = i - displacement
                break
        A = A[1:] + A[:1]

    if (periodicity == -1):
            print( displacement + (K-1)*N)
    else:
            print(displacement + (K-1)*periodicity)
