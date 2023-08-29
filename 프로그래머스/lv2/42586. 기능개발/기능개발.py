def solution(progresses, speeds):
    N = len(progresses)
    answer = []
    front = -1
    rear = N - 1
    done = 0

    while done < N:
        cnt = 0
        if progresses[front + 1] >= 100:
            cnt += 1
            done += 1
            front += 1
            for i in range(front + 1, rear+1):
                if progresses[i] >= 100:
                    cnt += 1
                    done += 1
                    front += 1
                else:
                    break
        else:
            for i in range(N):
                if progresses[i] >= 100:
                    continue
                progresses[i] += speeds[i]
        if cnt:
            answer.append(cnt)

    return answer