
T = int(input())
for t_c in range(T):
    N = int(input())
    M = [(list(map(int, input().split()))) for i in range(N)]
    #print(M)
    ans = 0
    for c_row in range(N):
        for c_col in range (N):
            for i_row in range(c_row, N):
                for i_col in range(c_col, N):
                    #print ("M[c_row][c_col] = ", c_row, c_col)
                    #print ("M[i_row][i_col] = ", i_row, i_col)
                    if M[c_row][c_col] > M[i_row][i_col]:
                        #print("h")
                        ans += 1
    print(ans)

