import sys
input = sys.stdin.readline

def countIndex(N, arr):
    current_stage = 0  # 현재 몇번째 레벨에 있는지 확인
    upper_id = [0] * (N + 1)  # 상위 레벨들이 가진 index를 저장 예를들어 upper_id[1]은 1번 레벨의 인덱스
    graph = [0] * (N + 1)  # input 받은 순서대로 각 값이 가지는 하위 레벨 개수

    for i in range(1, N + 1):
        # 만약 레벨이 1계단 이상 상승한 경우 바로 return -1 (예를 들어 1 -> 5)
        if arr[i] - current_stage > 1:
            return -1

        # 레벨이 이전 레벨에 비해 1 올라간 경우
        elif arr[i] - current_stage == 1:
            # 상위 레벨의 인덱스에 위치를 저장
            upper_id[current_stage] = i - 1
            # 상위 레벨에 경로개수 추가
            graph[i - 1] += 1
            # 레벨 올려주기
            current_stage += 1

        # 레벨이 이전 레벨과 같은 경우
        elif arr[i] == current_stage:
            # 상위레벨의 인덱스에 경로개수 추가
            graph[upper_id[current_stage - 1]] += 1

        # 레벨이 1초과로 내려간 경우
        else:
            # 레벨을 현재 값으로 바꿔준다.
            current_stage = arr[i]
            # 상위레벨의 인덱스에 경로개수 추가
            graph[upper_id[current_stage - 1]] += 1

    return graph


N = int(sys.stdin.readline().rstrip())

arr = [0]
for i in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

new_arr = countIndex(N, arr)

if type(new_arr) == int:
    print(new_arr)
else:
    for i in range(1, len(new_arr)):
        print(new_arr[i])