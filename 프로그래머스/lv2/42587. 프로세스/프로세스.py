def solution(priorities, location):
    for i, p in enumerate(priorities):
        priorities[i] = [p, i]
    done = []
    while priorities:
        max_p = max(priorities)
        cur = priorities.pop(0)
        if cur[0] != max_p[0]:
            priorities.append(cur)
        else:
            done.append(cur)

    for i in range(len(done)):
        if done[i][1] == location:
            return i+1