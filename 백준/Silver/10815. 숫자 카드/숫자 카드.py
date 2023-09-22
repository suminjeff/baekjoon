import sys
input = sys.stdin.readline


def binary_search(array, t, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == t:
            return 1
        elif array[mid] > t:
            end = mid-1
        else:
            start = mid+1
    return 0


N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
checker = list(map(int, input().split()))
for i in range(M):
    checker[i] = binary_search(cards, checker[i], 0, N-1)
print(*checker)