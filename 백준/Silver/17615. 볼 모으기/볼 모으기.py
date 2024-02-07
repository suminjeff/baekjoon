N = int(input())
ball = input()
res = []
for red in [ball.rstrip("R"), ball.lstrip("R")]:
    res.append(red.count("R"))
for blue in [ball.rstrip("B"), ball.lstrip("B")]:
    res.append(blue.count("B"))
print(min(res))