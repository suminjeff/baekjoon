def solve(string):
    global answer
    if len(string) == len(current):
        if string == current:
            answer = 1
        return
    if len(string) == 0:
        return 
    if string[-1] == "A":
        solve(string[:-1])
    if string[0] == "B":
        solve(string[:0:-1])

current = input()
target = input()
answer = 0
solve(target)
print(answer)
