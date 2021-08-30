
# Write your code here
T = int(input())

for t_c in range(T):
    N = int(input())
    A = sorted(list(map(int, input().split()))) # Firstly, I tried to simplify (A AND B) XOR (A OR B) and found that it's actually equal to A XOR B. Then since XOR gives 0 if both bits are the same, I thought that if the numbers are close to each other, then there's the chance that most of their bits are similar, hence giving more 0's in XOR, hence in resulting in a smaller output. So i went on this assumption, sorted the input list, XORed just the adjacent numbers and the returned the least of these numbers:
 
    #print(A)
    ans = []
    for i in range(N-1):
        ans.append((A[i] & A[i+1]) ^ (A[i] | A[i+1]))

    print(min(ans))
