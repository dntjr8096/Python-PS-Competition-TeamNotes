'''
문제 . 시간 제한 1초, 메모리 제한 128MB
나이트가 이동할 수 있는 경우의 수를 출력하라.

1. 8 X 8 체스판 형태의 정원이 존재한다.
2. 나이트는 체스판 특정 1칸에 서있으며 L자 형태로만 움직일 수 있다.
    1) 수평 2칸 이동, 수직 1칸 이동
    2) 수직 2칸 이동, 수평 1칸 이동
3. 행 위치는 1~8료 표시, 열 위치는 a~h로 표시
'''
N = 8

position = input()
row = int(position[1])
col = int(ord(position[0])) - int(ord('a')) + 1

steps = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (-1, 2), (1, -2), (-1, -2)]

result = 0
for x, y in steps:
    nx = row + x
    ny = col + y
    if nx < 1 or nx > N or ny < 1or ny > N:
        continue
    result += 1
print(result)

