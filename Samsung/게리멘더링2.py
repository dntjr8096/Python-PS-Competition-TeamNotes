N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

def divide(x, y, d1, d2):
    distinct = [0, 0, 0, 0, 0]

    for r in range(N):
        for c in range(N):

            if r < (x + d1) and c <= y and (r+c) < (x+y):
                distinct[0] += board[r][c]
            elif r <= (x + d2) and y < c and (c-r) > (y-x):
                distinct[1] += board[r][c]
            elif (x + d1) <= r and c < (y - d1 + d2) and (c-r) < (y-x-(2*d1)):
                distinct[2] += board[r][c]
            elif (x + d2) < r and (y - d1 + d2) <= c and (r+c) > (x+y+(2*d2)):
                distinct[3] += board[r][c]
            else:
                distinct[4] += board[r][c]

    return max(distinct) - min(distinct)

answer = float('inf')

for i in range(N):
    for j in range(N):
        x,y = i,j

        for d1 in range(1, N):
            for d2 in range(1, N):

                if (x + d1 + d2) >= N or (y + d2) >= N:
                    continue

                answer = min(answer, divide(x, y, d1, d2))

print(answer)