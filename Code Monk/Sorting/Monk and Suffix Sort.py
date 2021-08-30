
# Write your code here
S, k = map(str, input().split(' '))
k = int(k)
suffix = []
for i in range(len(S)):
    suffix.append(S[i:])

print(sorted(suffix)[k-1])

