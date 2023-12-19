import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def bellman_ford(start):
    # 시작 노드 초기화
    distance = [inf] * (N+1)
    distance[start] = 0
    # 노드의 개수만큼 edge relaxation 반복
    # N-1번 탐색하고 마지막 한번은 negative cycle 존재 확인
    for i in range(N):
        # 매 반복마다 모든 간선을 확인하며 갱신
        for edge in edges:
            curNode, nextNode, edgeCost = edge
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[nextNode] > distance[curNode] + edgeCost:
                distance[nextNode] = distance[curNode] + edgeCost
                # N번째 반복에서 갱신되는 값이 있으면 negative cycle 존재
                if i == N-1:
                    return False
    return True


inf = int(1e9)
T = int(input())
for tc in range(1, T+1):
    N, M, W = map(int, input().split())
    edges = []
    for _ in range(M):
        s, e, t = map(int, input().split())
        edges.append([s, e, t])
        edges.append([e, s, t])
    for _ in range(W):
        s, e, t = map(int, input().split())
        edges.append([s, e, -t])

    res = bellman_ford(1)
    if res:
        print("NO")
    else:
        print("YES")

