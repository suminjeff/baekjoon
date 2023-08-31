def dfs(start, division):
    if len(division) == 0:
        return True
    else:
        visited[start] = 1
        for i in graph[start]:
            if visited[i] == 0 and i in division:
                dfs(i, division)
        for i in division:
            if visited[i] != 1:
                return False
        return True


def divide_city(city_n):
    div_list = []
    for i in range(1 << city_n - 1):
        div1 = []
        div2 = []
        for j in range(N):
            if i & (1 << j):
                div1.append(j)
            else:
                div2.append(j)
        if 0 < len(div1):
            div_list.append([div1, div2])
    return div_list


def calc_pop_diff(division):
    div1, div2 = division[0], division[1]
    pop1, pop2 = 0, 0
    for i in div1:
        pop1 += population[i]
    for j in div2:
        pop2 += population[j]
    return abs(pop1 - pop2)


N = int(input())
cities = [n for n in range(N)]
population = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    length = graph[i].pop(0)
    for j in range(length):
        graph[i][j] -= 1
division = divide_city(N)

ans = float("inf")
for div in division:
    isValid = True
    for i in range(2):
        visited = [0] * N
        if dfs(div[i][0], div[i]) == False:
            isValid = False
    if isValid:
        pop_diff = calc_pop_diff(div)
        ans = min(ans, pop_diff)

if ans == float("inf"):
    ans = -1
print(ans)