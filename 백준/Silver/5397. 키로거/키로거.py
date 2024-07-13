import sys

# 5397


T = int(input())
for tc in range(T):
    L = input()
    left = []
    right = []

    for l in L:
        if l == '<':
            if left:
                right.append(left.pop())
        elif l == '>':
            if right:
                left.append(right.pop())
        elif l == '-':
            if left:
                left.pop()
        else:
            left.append(l)
    left.extend(reversed(right))
    print(''.join(left))