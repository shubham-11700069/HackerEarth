# Write your code here

# Solution 1 - partial accepted code

N, X = map(int, input().split())
A = list(map(int, input().split()))
def t (N, A, X):
    for i in range(1, N+1):
        for j in range(N+1-i):
            ans = sum(A[j:j+i])
            if(ans > X):
                return(i-1)

ans = t(N,A,X)
if ans is None:
    print(N)
else:
    print(ans)

# ^^ till here ^^    
