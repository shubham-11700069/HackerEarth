#solution 1 ===================>
# Write your code here
N = int(input())
arr = list(map(int, input().split()))
max_arr = max(arr)
#print(max_arr)
mul = 1
r = 100000

while max_arr:
    #print(mul, r)
    arr.sort(key = lambda x: (x/mul)%r)
    #print(arr)
    print(' '.join(map(str, arr)))
    mul = mul * r
    #print(mul)
    max_arr = max_arr // r
    #print(max_arr)


#Solution 2 =====================>

N = int(input())
A = list(map(int, input().split()))
def get(x, k):
    x //= 10**(5*k)
    return x % (10 ** 5)
 
for k in range(10):
    A.sort(key=lambda x: get(x, k))
    if all(get(x, k) == 0 for x in A):
        break
    print (" ".join(map(str, A)))
