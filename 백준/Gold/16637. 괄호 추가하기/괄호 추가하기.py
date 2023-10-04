import sys
input = sys.stdin.readline

def calc(arr):
    stack = []
    i = 0
    while i < len(arr):
        if stack:
            op = arr[i]
            i += 1
            if op == "+":
                stack[-1] += arr[i]
            elif op == "-":
                stack[-1] -= arr[i]
            elif op == "*":
                stack[-1] *= arr[i]
            i += 1
        else:
            stack.append(arr[i])
            i += 1
    return stack[-1]


def prioritize(ops_idx):
    res = []
    i = 0
    while i < N:
        if type(arr[i]) == int:
            res.append(arr[i])
            i += 1
        else:
            op = input_arr[i]
            if i in ops_idx:
                if op == "+":
                    res.append(res.pop()+arr[i+1])
                elif op == "-":
                    res.append(res.pop()-arr[i+1])
                elif op == "*":
                    res.append(res.pop()*arr[i+1])
                i += 2
            else:
                res.append(arr[i])
                i += 1
    return calc(res)


N = int(input())
input_arr = list(input())
arr = []
for tkn in input_arr:
    if tkn.isnumeric():
        arr.append(int(tkn))
    else:
        arr.append(tkn)
max_v = calc(arr)

ops = [2*i+1 for i in range(N//2)]
for i in range(1, 1 << N//2):
    subset = []
    for j in range(N//2):
        if i & (1 << j):
            if subset:
                if abs(ops[j]-subset[-1]) != 2:
                    subset.append(ops[j])
            else:
                subset.append(ops[j])
    max_v = max(max_v, prioritize(subset))

print(max_v)