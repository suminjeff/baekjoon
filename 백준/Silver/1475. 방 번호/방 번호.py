def solve(n):
    numbers = [0 for _ in range(10)]
    while n > 0:
        i = n % 10
        n //= 10
        if (i == 6) or (i == 9):
            six, nine = numbers[6], numbers[9]
            if six > nine:
                numbers[9] += 1
            else:
                numbers[6] += 1
        else:
            numbers[i] += 1
    return max(numbers)

if __name__ == '__main__':
    N = int(input())
    answer = solve(N)
    print(answer)