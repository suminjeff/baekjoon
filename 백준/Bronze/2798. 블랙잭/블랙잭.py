N, M = map(int, input().split())
cards = list(map(int, input().split()))

min_diff = float("inf")
ans = 0

for card1 in cards:
    for card2 in cards:
        if card2 == card1:
            continue
        else:
            for card3 in cards:
                if card3 == card1:
                    continue
                else:
                    if card3 == card2:
                        continue
                    else:
                        res = card1 + card2 + card3
                        if res <= M and M-res < min_diff:
                            min_diff = M-res
                            ans = res
print(ans)