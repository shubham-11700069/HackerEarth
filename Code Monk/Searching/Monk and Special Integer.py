# Write your code here

# Solution 1 - partial accepted code Time limit issue

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


""" Solution 2 - O(nlogn)
def binary_helper(partial_sums, lower, upper, x, i):
    while lower <= upper:
        mid = (lower+upper) // 2
        mid_value = partial_sums[mid]

        if i != 0:
            mid_value = partial_sums[mid+i] - partial_sums[i-1]

        if mid_value <= x:
            lower = mid + 1
        else:
            upper = mid - 1

    return lower, upper


n, x = map(int, input().rstrip().split())
a = list(map(int, input().rstrip().split()))

partial_sums = [a[0]]
for i in range(1, n):
    partial_sums.append(partial_sums[i-1] + a[i])

lower = 0
upper = n - 1
for i in range(n):
    lower, upper = binary_helper(partial_sums, 0, upper, x, i)

    if upper == n - i - 1:
        print(upper+1)
        break
"""

# Solution 3 - O(logN)
n, x = map(int, input().rstrip().split())
a = list(map(int, input().rstrip().split()))
#
partial_sums = [a[0]]
for i in range(1, n):
    partial_sums.append(partial_sums[i-1] + a[i])
#
right = 0
min_length = float('inf')
for left in range(n):
    if left == 0:
        temp_sum = partial_sums[right]
    else:
        temp_sum = partial_sums[right] - partial_sums[left-1]
#
    while temp_sum <= x:
        right += 1
        if right == n:
            break
        if left == 0:
            temp_sum = partial_sums[right]
        else:
            temp_sum = partial_sums[right] - partial_sums[left - 1]
#
    if right-left < min_length:
        min_length = right-left
#
    if right == n:
        break
#
print(min_length)
