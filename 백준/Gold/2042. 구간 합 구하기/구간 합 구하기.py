import sys
input = sys.stdin.readline

# 2042


# 세그먼트 트리 생성
# node가 담당하는 구간 [start, end]
def init(node, start, end):
    # node가 leaf node인 경우 배열의 원소 값을 반환 -> tree[node] = a[start]
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        # 재귀 함수를 이용해 왼쪽 자식과 오른쪽 자식 트리를 만들고 합을 저장
        mid = (start+end)//2
        tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
        return tree[node]


# 구간 합 구하기
# node가 담당하는 구간 [start, end]
# 합을 구해야 하는 구간 [left, right]
def subSum(node, start, end, left, right):
    # 겹치지 않으면 탐색을 이어갈 필요가 없음
    if left > end or right < start:
        return 0

    # 구해야 하는 합의 범위에 start-end가 포함된다면 node의 자식들도 모두 포함 된 것
    if left <= start and end <= right:
        return tree[node]

    mid = (start+end)//2
    return subSum(node*2, start, mid, left, right) + subSum(node*2+1, mid+1, end, left, right)


def update(node, start, end, index, difference):
    if index < start or index > end:
        return
    tree[node] += difference

    if start != end:
        mid = (start+end)//2
        update(node*2, start, mid, index, difference)
        update(node*2+1, mid+1, end, index, difference)


# N: 숫자의 개수, M: 수의 변경이 일어나는 횟수, K: 구간의 합을 구하는 횟수
N, M, K = map(int, input().split())

# arr: N개의 수에 대한 배열
arr = [int(input()) for _ in range(N)]
tree = [0]*3000000

init(1, 0, N-1)
for _ in range(M+K):
    # a가 1일 때: b번째 수를 c로 바꿈
    # a가 2일 때: b번째 수부터 c번째 수까지의 합을 구해 출력
    a, b, c = map(int, input().split())
    if a == 1:
        b = b-1
        difference = c - arr[b]
        arr[b] = c
        update(1, 0, N-1, b, difference)
    elif a == 2:
        print(subSum(1, 0, N-1, b-1, c-1))