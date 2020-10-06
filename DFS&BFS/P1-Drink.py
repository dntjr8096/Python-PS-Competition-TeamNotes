'''
문제
- 얼음 틀의 모양이 주어졌을 때 생성되는 아이스크림 총 갯수를 구하여라

1. 아이스크림 틀 형태는 N X M 이다.
2. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시한다.

input Sample
4 5
00110
00011
11111
00000
result : 3
'''
n, m = map(int, input().split())

graph = []
for _ in range(n):
    data = []
    input_line = input()

    for i in range(m):
        data.append(int(input_line[i]))
    graph.append(data)

result = 0


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return

    if graph[x][y] == 0:
        graph[x][y] = 2
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

    return


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result += 1
            dfs(i, j)

print(result)
