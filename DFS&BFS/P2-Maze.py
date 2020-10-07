'''
문제
- 미로 탈출을 위해 최소로 움직여야 하는 칸을 구하라.

1. 미로 형태는 N X M 이다.
2. 괴물이 있는 부분은 0, 아닌 부분은 1로 표시한다.
3. 괴물을 피해서 탈출 해야한다.
4. 캐릭터는 (1,1)부터 시작한다.

input Sample
5 6
101010
111111
000001
111111
111111
result : 3
'''

from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
visited = [[0] * m for _ in range(n)]

queue = deque()
def bfs():
    queue.append((0, 0, 1))

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while len(queue) != 0:
        x, y, d = queue.popleft()
        visited[x][y] = d

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny, d+1))

    return visited[n-1][m-1]

print(bfs())