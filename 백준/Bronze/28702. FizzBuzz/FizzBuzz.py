sequence = [int(x) if x.isnumeric() else x for x in [input() for _ in range(3)]]
idx = -1
for i in range(3):
    element = sequence[i]
    if isinstance(element, int):
        idx = element + (3-i)
        break

if idx % 3 == idx % 5 == 0:
    print('FizzBuzz')
elif idx % 3 == 0 and idx % 5 != 0:
    print('Fizz')
elif idx % 3 != 0 and idx % 5 == 0:
    print('Buzz')
else:
    print(idx)