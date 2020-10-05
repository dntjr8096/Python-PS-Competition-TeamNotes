'''
문제 . 시간 제한 1초, 메모리 제한 128MB
캐릭터가 방문한 칸 수를 출력하라.

1. N X M 형태의 맵이 존재한다.
2. 각각의 칸은 육지 또는 바다이다.
3. 캐릭터는 동서남북 중 한 곳을 바라보며 다음과 같이 이동한다.
    1) 현재 방향 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다.
    2) 바라본 방향에 갈 곳이 없다면 회전만 수행하고 1단계로 돌아간다. 아니면 이동한다.
    3) 만약 네 방향이 다 바다거나 가본 칸이라면 바라보는 방향을 유지한 채로 한 칸 뒤로가고 1단계로 돌아간다.
    4) 단, 이때 뒤쪽 방향이 바다 칸이라면 움직임을 멈춘다.
4. 0 - 북쪽, 1 - 동쪽, 2 - 남쪽, 3 - 서쪽
5. 맵: 0 - 육지, 1 - 바다

4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
result : 3
'''
class Character:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.count = 0
        self.movable = True
        self.steps = [(0, -1), (1, 0), (0, 1), (-1, 0)] #북,동,남,서

    def turnLeft(self):
        self.d = (self.d-1) % len(self.steps)

    def move(self):
        turnCount = 0
        while turnCount < 4:
            self.turnLeft()
            nx = self.x + self.steps[self.d][0]
            ny = self.y + self.steps[self.d][1]

            if 0 <= nx <= m and 0 <= ny <= n:
                if board[nx][ny] == 0:
                    self.x = nx
                    self.y = ny
                    board[nx][ny] = -1
                    self.count += 1
                    return
                else:
                    turnCount += 1

        nx = self.x - self.steps[self.d][0]
        ny = self.y - self.steps[self.d][1]
        #백스텝
        if nx < 0 or nx > m or ny < 0 or ny > n:
            self.movable = False
        else:
            if board[nx][ny] == -1:
                self.x = nx
                self.y = ny
            else:
                self.movable = False

n, m = map(int, input().split())
y, x, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

c = Character(x, y, d)
while c.movable:
    c.move()
print(c.count)

