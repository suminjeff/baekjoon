def is_consistent(phone_numbers):
    phone_numbers.sort()

    for i in range(len(phone_numbers) - 1):
        if phone_numbers[i+1].startswith(phone_numbers[i]):
            return "NO"
    return "YES"


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    data = [input() for _ in range(n)]
    ans = is_consistent(data)
    print(ans)