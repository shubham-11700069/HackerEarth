n,m,g = map(int, input().split())
T = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = 0
gap = []
for i in range (n-1):
    gap.append(T[i+1] - T[i])
d = max(gap)
for i in range(m):
    if (d >= A[i]:
        ans += 1
print(ans)
