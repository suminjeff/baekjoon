first, second, third = map(int, input().split())

if first == second == third:
    print(10000 + first * 1000)
elif first == second:
    print(1000 + first * 100)
elif first == third:
    print(1000 + first * 100)
elif third == second:
    print(1000 + third * 100)
else:
    print(100 * max(first, second, third))