x = int(input())
y = int(input())

quadrant = None

if x > 0 and y > 0:
    quadrant = 1

elif x < 0 and y > 0:
    quadrant = 2

elif x > 0 and y < 0:
    quadrant = 4

elif x < 0 and y < 0:
    quadrant = 3

print(quadrant)