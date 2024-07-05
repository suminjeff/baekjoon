import sys
from math import sqrt


T = int(input())

microwave_time = [300, 60, 10]


total_click = [0, 0, 0]
time_left = T
index = 0
while True:
    if time_left <= 0:
        break

    if index > 2:
        print(-1)
        exit(0)
    click = time_left // microwave_time[index]
    total_click[index] += click
    time_left -= microwave_time[index] * click
    index += 1
print(*total_click)