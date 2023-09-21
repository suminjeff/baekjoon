N = int(input())

num = 666
nums = [num]
cnt = 1

while cnt <= N:
    if '666' in str(num):
        nums.append(num)
        cnt += 1
    num += 1
print(nums[-1])