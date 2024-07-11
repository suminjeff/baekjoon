import sys
from collections import deque


# 23288


delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 동 남 서 북

class Dice:

	position, direction = [0, 0], 0
	top, bottom, north, south, east, west = 1, 6, 2, 5, 3, 4

	def roll(self, direction):
		top, bottom, north, south, east, west = self.top, self.bottom, self.north, self.south, self.east, self.west
		if direction == 0:  # 동쪽
			self.bottom = east
			self.east = top
			self.top = west
			self.west = bottom
		elif direction == 1:  # 남쪽
			self.bottom = south
			self.south = top
			self.top = north
			self.north = bottom
		elif direction == 2:  # 서쪽
			self.bottom = west
			self.west = top
			self.top = east
			self.east = bottom
		elif direction == 3:  # 북쪽
			self.bottom = north
			self.north = top
			self.top = south
			self.south = bottom

	def get_next_direction(self, direction, grid_value):
		dice_value = self.bottom  # dice_value: A, grid_value: B
		if dice_value > grid_value:	    # 90도 시계 방향 회전
			next_direction = (direction + 1) % 4
		elif dice_value < grid_value:   # 90도 시계 방향 회전
			next_direction = (direction + 3) % 4
		else:							# 이동 방향에 변화 없음
			next_direction = direction
		return next_direction


def bfs(n, m, r, c, v, grid):
	result = 1
	visited = [[0]*m for _ in range(n)]
	visited[r][c] = 1
	que = deque([[r, c]])
	while que:
		r, c = que.popleft()
		for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
			if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and grid[nr][nc] == v:
				result += 1
				visited[nr][nc] += 1
				que.append([nr, nc])

	return result

def solve(n, m, k, grid):
	answer = 0
	dice = Dice()
	for _ in range(k):
		r, c = dice.position
		direction = dice.direction
		dr, dc = delta[direction]
		nr, nc = r + dr, c + dc
		if nr < 0 or nr >= n or nc < 0 or nc >= m:  # 반대 방향
			direction = (2-direction) if direction in [0, 2] else (4-direction)
			dr, dc = delta[direction]
			nr, nc = r + dr, c + dc

		v = grid[nr][nc]
		c = bfs(n, m, nr, nc, v, grid)
		answer += v*c

		dice.roll(direction)
		next_direction = dice.get_next_direction(direction, v)
		dice.position, dice.direction = [nr, nc], next_direction

	return answer


if __name__ == '__main__':
	N, M, K = map(int, input().split())
	GRID = [list(map(int, input().split())) for _ in range(N)]
	ANSWER = solve(N, M, K, GRID)
	print(ANSWER)