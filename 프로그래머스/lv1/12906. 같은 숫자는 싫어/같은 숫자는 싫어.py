def solution(arr):
    answer = []
    top = -1
    for element in arr:
        if answer:
            if element == answer[top]:
                continue
            else:
                answer.append(element)
                top += 1
        else:
            answer.append(element)
            top += 1
    return answer