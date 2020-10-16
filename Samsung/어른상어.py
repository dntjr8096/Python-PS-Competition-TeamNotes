'''
1. 변수명 실수 확인
2. x,y 입력 실수 확인
3. 시간 초 범위 확인
4. 이동 -> 시간 감소 -> 냄새 뿌리기 -> 퇴출 순으로 문제 요구사항대로 진행했는지 확인
'''

from collections import defaultdict

steps = ['dummy', [-1, 0], [1, 0], [0, -1], [0, 1]] #상하좌우

class Shark:
    def __init__(self, num):
        self.x = 0
        self.y = 0
        self.num = num
        self.direction = 0
        self.preference = defaultdict(list)
        self.out = False

    def setXY(self, x, y):
        self.x = x
        self.y = y

    def setDirection(self, direction):
        self.direction = direction

    def setPreference(self, d, data):
        assert len(data) == 4, 'Preference data length error'

        self.preference[d].append('dummy')
        for i in range(4):
            self.preference[d].append(data[i])

    def move(self):
        shark_steps = self.preference[self.direction]
        for d in range(1, 5):
            nx = self.x + steps[shark_steps[d]][0]
            ny = self.y + steps[shark_steps[d]][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if not smells[nx][ny]:
                self.x, self.y = nx, ny
                self.direction = shark_steps[d]
                break
        else:
            #재탐색 내 냄새 있는 곳 탐색
            for rd in range(1, 5):
                nx = self.x + steps[shark_steps[rd]][0]
                ny = self.y + steps[shark_steps[rd]][1]

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue

                if my_map[nx][ny] == self.num:
                    self.x, self.y = nx, ny
                    self.direction = shark_steps[rd]
                    break
            else:
                self.out = True

    def perfume(self):
        if self.out:
            return

        if not smells[self.x][self.y]:
            smells[self.x][self.y] = K
            my_map[self.x][self.y] = self.num
        elif smells[self.x][self.y] and my_map[self.x][self.y] == self.num:
            smells[self.x][self.y] = K
            my_map[self.x][self.y] = self.num
        else:
            self.out = True

N, M, K = map(int, input().split())

my_map = [list(map(int, input().split())) for _ in range(N)]  #상어 번호
smells = [[0 for _ in range(N)] for _ in range(N)]  #냄새 맵
sharks = ['dummy'] + [Shark(i) for i in range(1, M+1)]

#상어 위치 입력
for i in range(N):
    for j in range(N):
        if my_map[i][j]:
            sharks[my_map[i][j]].setXY(i, j)

#상어 방향 입력
directions = list(map(int, input().split()))
for i in range(1, M+1):
    sharks[i].setDirection(directions[i-1])

#상어 방향 우선순위 입력
for i in range(1, M+1):
    for j in range(1, 5):
        data = list(map(int, input().split()))
        sharks[i].setPreference(j, data)

# 상어 냄새뿌리기
for s in range(1, len(sharks)):
    sharks[s].perfume()

result = 0
for t in range(1001):
    #상어가 1마리만 남으면
    if len(sharks) == 2:
        print(t)
        exit(0)

    #상어 이동
    for s in range(1, len(sharks)):
        sharks[s].move()

    # 냄새 감소
    for i in range(N):
        for j in range(N):
            if smells[i][j]:
                smells[i][j] -= 1
                if smells[i][j] == 0:
                    my_map[i][j] = 0

    # 상어 냄새뿌리기
    for s in range(1, len(sharks)):
        sharks[s].perfume()

    # 상어 퇴출
    for s in range(len(sharks) - 1, 0, -1):
        if sharks[s].out:
            sharks.pop(s)

print(-1)