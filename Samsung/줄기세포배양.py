dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

T = int(input())

def wrapMap(_map, K):
    H = len(_map) + 2*(K-1)
    W = len(_map[0]) + 2*(K-1)

    new_map = [[0 for _ in range(W)] for _ in range(H)]

    for i in range(len(_map)):
        for j in range(len(_map[0])):
            new_map[K-1+i][K-1+j] = _map[i][j]

    return new_map

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    my_map = [list(map(int, input().split())) for _ in range(N)]
    active = ['dummy'] + [[] for _ in range(10)]

    for i in range(N):
        for j in range(M):
            y, x = i, j
            if my_map[i][j]:
                active[my_map[i][j]].append([K-1+i, K-1+j, my_map[i][j]]) #map을 상하좌우 K-1칸 씩 늘릴 예정

    my_map = wrapMap(my_map, K)

    for _ in range(K):
        for vitality in range(10, 0, -1):   #생명력 높은 순으로 번식
            cells = active[vitality]
            new = []
            old = []
            for i in range(len(cells)-1, -1, -1):
                cells[i][2] -= 1 #HP 1감소
                y, x, HP = cells[i]

                if HP == -1:    #번식 시작
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if not my_map[ny][nx]:
                            my_map[ny][nx] = vitality
                            new.append([ny, nx, vitality])

                if HP == -vitality:
                    old.append(i)

            #죽은 세포 제거
            for idx in old:
                cells.pop(idx)

            cells += new

    result = 0
    for i in range(1, 11):
        result += len(active[i])

    print(f'#{tc} {result}')


