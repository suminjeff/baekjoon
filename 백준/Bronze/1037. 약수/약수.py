import sys
input = sys.stdin.readline

N = int(input())
elements = list(map(int, input().split()))
elements.sort()
print(elements[-1] * elements[0])