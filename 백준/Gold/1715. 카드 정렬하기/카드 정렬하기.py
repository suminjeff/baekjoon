import sys
input = sys.stdin.readline
import heapq

N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))
visited = [0]*N
min_v = 1000*100000

cnt = 0
while len(cards) > 1:
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    new_card = card1+card2
    cnt += new_card
    heapq.heappush(cards, new_card)

print(cnt)