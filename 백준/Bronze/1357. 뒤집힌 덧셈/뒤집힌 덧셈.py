def rev(str_number):
    return int(str_number[::-1])

x, y = input().split()
print(rev(str(rev(x)+rev(y))))