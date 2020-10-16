'''
1. bfs를 할 경우에는 visited를 사용해서 중복 원소 안들어가게 주의하기 또는 거리 배열의 초기화 값이랑 비교하기
2. 거리의 maximum 값을 잘 계산해보기
3. break 처리가 아닌 exit(0) 처리 하기
4. 변수명 고민하기
'''

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def makeDistance(px, py):
    q = deque()
    q.append([px-1, py-1, 0])
    distance = [[404 for _ in range(N)] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[px-1][py-1] = 1

    while len(q) > 0:
        x, y, c = q.popleft()
        distance[x][y] = c

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and my_map[nx][ny] != 1 and not visited[nx][ny]:
                q.append([nx, ny, c+1])
                visited[nx][ny] = 1

    return distance

def selectPassenger(ps, distance):
    minidx = -1
    mincost = 404
    for idx, el in enumerate(ps):
        sx, sy, dx, dy = el
        if mincost > distance[sx-1][sy-1]:
            minidx = idx
            mincost = distance[sx-1][sy-1]

    return minidx

N, M, P = map(int, input().split())
my_map = [list(map(int, input().split())) for _ in range(N)]
x, y = map(int, input().split())
passengers = []
for _ in range(M):
    passengers.append(list(map(int, input().split())))
passengers.sort(key=lambda el: (el[0], el[1]))

while len(passengers) > 0:
    if P <= 0:
        print(-1)
        exit(0)

    # 지금 택시 위치로부터 거리 계산하고 가장 가까운 승객 찾기
    distance = makeDistance(x, y)
    idx = selectPassenger(passengers, distance)
    srcx, srcy, dstx, dsty = passengers.pop(idx)

    #거리 연료 빼기
    if distance[srcx-1][srcy-1] == 404:
        print(-1)
        exit(0)
    P -= distance[srcx-1][srcy-1]
    if P <= 0:
        print(-1)
        exit(0)

    #승객 위치로부터 거리계산
    x, y = srcx, srcy
    distance = makeDistance(x, y)

    #목적지까지 데려다주고 연료 채우기
    if distance[dstx-1][dsty-1] == 404:
        print(-1)
        exit(0)
    disToDst = distance[dstx-1][dsty-1]
    P -= disToDst
    if P < 0:
        print(-1)
        exit(0)

    P += disToDst * 2
    x, y = dstx, dsty

print(P)