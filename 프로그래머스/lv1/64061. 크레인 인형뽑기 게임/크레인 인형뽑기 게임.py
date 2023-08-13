def solution(board, moves):
    basket = []
    N = len(board)
    for col in moves:
        for row in range(N):
            if board[row][col-1] != 0:
                basket.append(board[row][col-1])
                board[row][col-1] = 0
                break
    answer = 0
    i = len(basket) - 1
    while i > 0:
        if basket[i] == basket[i-1]:
            basket.pop(i)
            basket.pop(i-1)
            answer += 2
            i = len(basket) - 1
        else:
            i -= 1
    return answer