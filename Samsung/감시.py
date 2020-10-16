'''
1. 백트래킹 코드 다시 짜보기
2. deepcopy가 아닌 변한 부분을 다시 되돌리는 식으로 고쳐보기
https://www.acmicpc.net/source/16503787 참조
'''

from copy import deepcopy
def rotateBy90(arr):
    arr = [[arr[i][j] for i in range(len(arr))] for j in range(len(arr[0]))]

# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def fill(_map, x, y, d):
    nx = x + dx[d]
    ny = y + dy[d]
    while True:
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            break
        elif _map[nx][ny] == 6:
            break

        _map[nx][ny] = -1
        nx += dx[d]
        ny += dy[d]

def dfs(_cctvs, _map):
    if len(_cctvs) == 0:
        temp = [_map[i][j] for i in range(N) for j in range(M) if not _map[i][j]]
        return len(temp)

    result = 64
    x, y, t = _cctvs.pop()
    if t == 1:
        for d in range(4):
            new_map = deepcopy(_map)
            new_cctvs = deepcopy(_cctvs)
            fill(new_map, x, y, d)
            result = min(dfs(new_cctvs, new_map), result)
    elif t == 2:
        for d in range(2):
            new_map = deepcopy(_map)
            new_cctvs = deepcopy(_cctvs)
            fill(new_map, x, y, d)
            fill(new_map, x, y, d+2)
            result = min(dfs(new_cctvs, new_map), result)
    elif t == 3:
        for d in range(4):
            new_map = deepcopy(_map)
            new_cctvs = deepcopy(_cctvs)
            fill(new_map, x, y, d)
            fill(new_map, x, y, (d + 1) % 4)
            result = min(dfs(new_cctvs, new_map), result)
    elif t == 4:
        for d in range(4):
            new_map = deepcopy(_map)
            new_cctvs = deepcopy(_cctvs)
            fill(new_map, x, y, d)
            fill(new_map, x, y, (d + 1) % 4)
            fill(new_map, x, y, (d + 2) % 4)
            result = min(dfs(new_cctvs, new_map), result)
    elif t == 5:
        new_map = deepcopy(_map)
        new_cctvs = deepcopy(_cctvs)
        for d in range(4):
            fill(new_map, x, y, d)
        result = min(dfs(new_cctvs, new_map), result)

    return result

N, M = map(int, input().split())
my_map = [list(map(int, input().split())) for _ in range(N)]

cctvs = []

for i in range(N):
    for j in range(M):
        if 1 <= my_map[i][j] <= 5:
            cctvs.append([i, j, my_map[i][j]])

print(dfs(cctvs, my_map))