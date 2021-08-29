'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def ans(n):
    if (n in cache):
        return (cache[n])

    if (n == 0):
        cache[n] = 1
        return (cache[n])
    if (n == 1):
        cache[n] = 10
        return (cache[n])

    temp1 = ans(n/2)
    temp2 = ans(n/2-1)

    if (n & 1) == 0:
        cache[n] = (temp1*temp1 - temp2*temp2) % mod
    else:
        temp3 = ans(n/2 + 1)
        cache[n] = (temp1 * (temp3 - temp2)) % mod

    return (cache[n])

T = int(input())
for t_c in range(T):
    N = int(input())
    """if (N == 1):
        print(10)
        break
    max_N = pow(10, N)-1
    #min_N = pow(10, (N-1))
    #print(max_N)
    #print(min_N)
    ans = list(map(str, range(max_N+1)))
    #print(ans)
    if '13' in str(ans):
        matching = [s for s in ans[10:] if "13" in s]
    print(len(ans)-len(matching))"""

    
    cache = {}
    mod = 1000000009
    print(ans(N))

