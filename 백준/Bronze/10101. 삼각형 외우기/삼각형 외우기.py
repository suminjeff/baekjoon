total = 0
angles = set()
for _ in range(3):
    angle = int(input())
    angles.add(angle)
    total += angle
if total == 180:
    if len(angles) == 1:
        print("Equilateral")
    elif len(angles) == 2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
