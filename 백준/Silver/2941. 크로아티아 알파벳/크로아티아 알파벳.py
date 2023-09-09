alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
checker = ["c", "d", "l", "n", "s", "z"]
input_word = input()
N = len(input_word)
cnt = 0
i = 0
while i < N:
    temp = ""
    if input_word[i] in checker:
        if i+1 < N:
            temp += input_word[i] + input_word[i+1]
            if temp in alphabet:
                cnt += 1
                i += 2
            else:
                if i+2 < N:
                    temp += input_word[i+2]
                    if temp in alphabet:
                        cnt += 1
                        i += 3
                    else:
                        cnt += 1
                        i += 1
                else:
                    cnt += 1
                    i += 1
        else:
            cnt += 1
            i += 1
    else:
        cnt += 1
        i += 1

print(cnt)