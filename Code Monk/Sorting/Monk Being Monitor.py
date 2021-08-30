
# Write your code here
T = int(input())

for i in range(T):
    N = int(input())
    H = list(map(int, input().split()))
    #max_ = max(H)
    #min_ = min(H)
    #print(max_ - min_)
    H_d = {}
    for i in H:
        H_d[i] = H_d.get(i, 0) + 1
    #print(H_d)
    ans = max(H_d.values()) - min(H_d.values())
    if (ans == 0):
        print("-1")
    else:
        print(ans)



