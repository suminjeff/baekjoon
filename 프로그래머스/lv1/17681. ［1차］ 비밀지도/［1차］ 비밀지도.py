def solution(n, arr1, arr2):
    answer = []
    map1 = []
    for i in arr1:
        string = str(bin(i))[2:].zfill(n)
        map1.append(string)

    map2 = []
    for i in arr2:
        string = str(bin(i))[2:].zfill(n)
        map2.append(string)

    for row in range(n):
        string = ""
        for col in range(n):
            if map1[row][col] == '1' or map2[row][col] == '1':
                string += '#'
            else:
                string  += ' '
        answer.append(string)

    return answer