def find_op(memory):
    op = []
    start = 0
    for i in range(len(memory)):
        if memory[i] == 1:
            op.append(i)
            start = i
            break

    for i in range(start+1, len(memory)):
        if memory[i] != memory[i-1]:
            op.append(i)
    return op


T = int(input())
for tc in range(1, T+1):
    memory = list(input())
    for m in range(len(memory)):
        memory[m] = int(memory[m])

    origin = [0] * len(memory)
    ans = find_op(memory)
    print(f"#{tc} {len(ans)}")