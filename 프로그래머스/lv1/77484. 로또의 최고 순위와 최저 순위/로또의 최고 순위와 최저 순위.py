def solution(lottos, win_nums):
    answer = []
    my_dict = {6:1,
              5:2,
              4:3,
              3:4,
              2:5, 
              1:6, 
              0:6}
    cnt = 0
    zero_cnt = 0
    for i in range(6):
        if lottos[i] in win_nums:
            cnt += 1
        elif lottos[i] == 0:
            zero_cnt +=1
    answer.append(my_dict[cnt+zero_cnt])
    answer.append(my_dict[cnt])
    
    return answer