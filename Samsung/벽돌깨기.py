'''
1. 순환 참조 방지 (visited 이용)
2. 시뮬레이션하면서 부딪힐 수 있는 부분만 뽑기 (itertools product 사용 X)
'''
from collections import deque
from copy import deepcopy

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def countBlock(board):
    tmp = [board[i][j] for i in range(len(board)) for j in range(len(board[i])) if board[i][j] != 0]
    return len(tmp)

def dfs(board, count, N):
    block_count = countBlock(board)
    if count >= N or block_count == 0:
        return block_count

    start_idx = [i for i in range(len(board)) if len(board[i]) != 0]

    answer = float('inf')
    for idx in start_idx:
        result = dfs(bomb(idx, len(board[idx])-1, deepcopy(board)), count+1, N)
        answer = min(answer, result)

    return answer

def bomb(_x, _y, _board):
    visited = [[0 for _ in range(len(_board[i]))] for i in range(len(_board))]

    queue = deque()
    if _y < 0:
        return _board

    queue.append((_x, _y))
    visited[_x][_y] = 1

    while len(queue) != 0:
        x, y = queue.popleft()
        if _board[x][y] == 0:
            continue
        n = _board[x][y]
        _board[x][y] = 0

        for k in range(1, n):
            for i in range(4):
                nx = x + k*dx[i]
                ny = y + k*dy[i]

                if 0 <= nx < len(_board) and 0 <= ny < len(_board[nx]) and _board[nx][ny] and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

    for i in range(len(_board)):
        _board[i] = [_board[i][j] for j in range(len(_board[i])) if _board[i][j] != 0]

    return _board

for t in range(T):
    N, W, H = map(int, input().split())

    _board = []
    for _ in range(H):
         _board.append(list(map(int, input().split())))

    #board 행렬 뒤집기
    new_board = [[_board[i][j] for i in reversed(range(H)) if _board[i][j] != 0] for j in range(W)]
    answer = dfs(new_board, 0, N)

    print(f'#{t+1} {answer}')