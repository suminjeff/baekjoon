import sys
input = sys.stdin.readline

# 5525

N = int(input())
M = int(input())
S = input()
ans = 0
for i in range(M):
    if S[i] == 'I':
        flag = True
        if i+2*N >= M:
            flag = False
        else:
            for j in range(i+1, i+1+2*N, 2):
                if j+1 < M:
                    if S[j] != 'O' or S[j+1] != 'I':
                        flag = False
                        break
        ans += int(flag)
print(ans)