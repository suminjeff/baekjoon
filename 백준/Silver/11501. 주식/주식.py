import sys


def calculate_max_price(n, prices):
    max_price = 0
    stack = []
    for i in range(n-1, -1, -1):
        price = prices[i]
        if not stack:
            stack.append(price)
        else:
            last_price = stack[-1]
            if price > last_price:
                stack.append(price)
            else:
                max_price += last_price - price
    return max_price


if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        N = int(input())
        PRICES = list(map(int, input().split()))
        ANSWER = calculate_max_price(N, PRICES)
        print(ANSWER)
