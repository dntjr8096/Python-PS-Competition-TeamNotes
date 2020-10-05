# 좌표 이동
* dx, dy 사용, steps 사용
```python
# dx, dy 사용 예시
n, m = 5, 5
board = [[0 for _ in range(n)] for _ in range(m)]

#steps = [(0,-1), (0,1), (1,0), (-1,0)]
dx = [0, 0, 1 ,-1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D'] # x,y 좌표는 문제에 따라 달라질 수 있음

x, y = 0, 0
for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
        continue    # 격자를 넘어갈 경우
    else:    
        x, y = nx, ny
        break
```

# 숫자 <-> 문자열 변환
```python
str_i = str(i)
int_i = int(str_i)
```

# 아스키 코드 변환
```python
ascii_a = int(ord('a'))
```