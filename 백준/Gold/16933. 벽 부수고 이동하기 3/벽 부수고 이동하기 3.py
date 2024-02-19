from collections import deque
import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

if __name__=="__main__":

    N, M, K = map(int, input().split())

    board = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    Q=deque()         
    Q.append((0, 0, 0, 1))  # (행,열, 벽을 부순횟수, 낮이자 시작거리)

    while Q:
        x, y, z, ans = Q.popleft()     # x,y는 행,열 정보, z가 벽을 최대 부술수있는 횟수,ans는 거리(답),  ans는 거리(답)이자 밤/낮 정보, 
        if x==N-1 and y==M-1:
            print(ans)
            exit()

        daytime = ans % 2               # ans=1일때가 낮을 뜻한다, ans가 +1증가했다는 것은 낮에서 밤 또는 밤에서 낮으로 바뀐것을 의미한다
        for k in range(4) :
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<N and 0<=ny<M:                                   # 맵 범위안에서
                if board[nx][ny]==0 and visited[nx][ny][z]==0:        # 다음위치가 벽이 아니고 첫방문이면
                    visited[nx][ny][z]=ans
                    Q.append((nx,ny,z,ans+1))                         # ans가 상승했다-> 이동했다->날이 바꼈다. 즉, 몇밤을 세웠느냐가 곧 경로(거리)가 됨
                if board[nx][ny]==1 and z<K and visited[nx][ny][z+1]==0:     # 다음위치가 벽이고, 벽 부술 수 있고, 첫방문이면
                    if daytime :                                            # 낮이면
                        visited[nx][ny][z+1]=ans                            # 다음위치 벽 부순횟수 증가 위치에 현재거리(밤/낮)
                        Q.append((nx,ny,z+1,ans+1))                         # 다음은, 다음위치, 증가한 벽부순횟수,거리증가
                    else :                                                  # 밤이면 
                        Q.append((x,y,z,ans+1))                             # 이동은 안하지만, 머물러있어도 증가 

    print(-1)