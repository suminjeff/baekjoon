N_list = []

for i in range(9):
    N = int(input())
    N_list.append(N)

print(max(N_list))
print(N_list.index(max(N_list)) + 1)