phone = [""]*8
phone[0] += "ABC"
phone[1] += "DEF"
phone[2] += "GHI"
phone[3] += "JKL"
phone[4] += "MNO"
phone[5] += "PQRS"
phone[6] += "TUV"
phone[7] += "WXYZ"

word = input()
ans = 0

for i in range(len(word)):
    for j in range(len(phone)):
        if word[i] in phone[j]:
            ans += (phone.index(phone[j]) + 3)

print(ans)
