T = 4
for tc in range(1, T+1):
    ans = 0
    ax, ay, ap, aq, bx, by, bp, bq = map(int, input().split())
    if ax > bp or bx > ap or ay > bq or by > aq:
        ans = "d"
    else:
        if (ax == bp and aq == by) or (ax == bp and ay == bq) or (bx == ap and bq == ay) or (bx == ap and by == aq):
            ans = "c"
        else:
            if ax == bp or bx == ap or ay == bq or by == aq:
                ans = "b"
            else:
                ans = "a"
    print(ans)