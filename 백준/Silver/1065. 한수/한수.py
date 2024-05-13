def is_hansu(num):
    # 한 자리 수나 두 자리 수는 모두 등차수열이므로 항상 한수
    if num < 100:
        return True
    else:
        num_str = str(num)
        # 각 자리 숫자들의 차이가 일정한지 확인
        diff = int(num_str[1]) - int(num_str[0])
        for i in range(2, len(num_str)):
            if int(num_str[i]) - int(num_str[i-1]) != diff:
                return False
        return True

N = int(input())
count = 0

# 1부터 N까지의 수 중에서 한수의 개수 세기
for i in range(1, N+1):
    if is_hansu(i):
        count += 1

print(count)
