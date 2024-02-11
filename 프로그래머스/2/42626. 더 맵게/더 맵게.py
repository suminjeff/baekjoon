from heapq import heappop, heappush, heapify
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while scoville:
        s1 = heappop(scoville)
        if s1 >= K:
            return answer
        s2 = heappop(scoville)
        heappush(scoville, s1+s2*2)
        answer += 1
        if len(scoville) < 2 and scoville[0] < K:
            return -1
    return answer