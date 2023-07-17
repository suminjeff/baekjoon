num1 = int(input())
num2 = int(input())

result3 = num1 * (num2 % 10)
result4 = num1 * ((num2 % 100) // 10)
result5 = num1 * ((num2 % 1000) // 100)
result6 = result3 + (result4 * 10) + (result5 * 100)

print(result3)
print(result4)
print(result5)
print(result6)
