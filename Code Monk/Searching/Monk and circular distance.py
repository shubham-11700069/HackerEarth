

# Write your code here

from math import *
N = int(input())
x = []
y = []
hyp = []
for _ in range(N):
    x_i, y_i = map(int, input().split(' '))
    hyp_i = (sqrt( (x_i**2) + (y_i**2) ))
    x.append(x_i)
    y.append(y_i)
    hyp.append(hyp_i)

hyp.sort()
#print(hyp)
hyp_max = hyp[-1]
hyp_min = hyp[0]
q = int(input())
Q = []

for _ in range(q):
    r = int(input())

    lower = 0
    upper = N - 1
    while lower <= upper:
        mid = (lower+upper) // 2

        if hyp[mid] <= r:
            lower = mid + 1
        else:
            upper = mid - 1

    print(lower)
