T = int(input())

for tc in range(T):
    R, S = map(str, input().split())
    for r in range(len(S)):
        print(S[r]*int(R), end="")
    print()