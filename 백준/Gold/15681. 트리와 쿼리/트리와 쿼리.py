import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 15681


def makeTree(currentNode, parentNode):
    for nextNode in graph[currentNode]:
        if nextNode != parentNode:
            parents[nextNode] = currentNode
            makeTree(nextNode, currentNode)
            children[currentNode] += children[nextNode]
            

N, R, Q = map(int, input().split())
parents = [i for i in range(N+1)]
children = [0] + [1 for _ in range(N)]
graph = [[] for _ in range(N+1)]
size = [0]*(N+1)
for _ in range(N-1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)
makeTree(R, R)
for _ in range(Q):
    U = int(input())
    print(children[U])
