'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
"""
def number_of_strings(n):
        result = 0
        result1 = 99
        result2 = 10
        if n == 1:
            return result2
        if n == 2:
            return result1
        for i in range(3, n+1):
            result = 10*result1 - result2
            result2 = result1
            result1 = result
        return result

    print(number_of_strings(N))
    
This is O(n) solution which cause time limit exceeded issue 
"""
# Write your code here
""" this is O(log[n]) solution but currently it is crashing and hackerearth is not accepting it, because the function is causing RecursionError : maximum recursion depth exceeded in comparison
"""
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

cache = {}
mod = 1000000009
T = int(input())
for t_c in range(T):
    N = int(input())
    print(ans(N))

