import sys


T = int(input())
for tc in range(T):
    N = int(input())
    ranks = sorted(list(map(int, input().split())) for _ in range(N))
    answer = 1
    highest_interview_rank = 0
    for i in range(1, N):
        if ranks[i][1] < ranks[highest_interview_rank][1]:
            highest_interview_rank = i
            answer += 1
    print(answer)