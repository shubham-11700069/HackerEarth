
# Write your code here

N = int(input())
arr = []
for i in range(N):
    arr.append(str(input()))

#print(arr)
 
for i in range(N):
    ans = 0
    for j in range(i):
        if (arr[i] > arr[j]):
            ans += 1
    print(ans)
