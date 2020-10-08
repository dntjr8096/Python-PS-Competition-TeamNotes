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

# 진수 변환
```python
42 == 0b101010 # 2진수
42 == 0o52 # 8진수
42 == 0x2a # 16진수

bin(42) == '0b101010' #2진수 문자열 변환
oct(42) == '0o52' #8진수 문자열 변환
hex(42) == '0x2a' #16진수 문자열 변환

int('0b101010', 2) #2진수 -> 10진수 변환
int('0o52', 8) #8진수 -> 10진수 변환

#접두어 제거 변환
format(42, 'b') == '101010'
format(42, 'o') == '52'
format(42, 'x') == '2a'
format(42, 'X') == '2A'

#접두어 포함 변환
format(42, '#b') == '0b101010'

#문자열 포맷터 변환
"int: {0:d}, bin: {0:b}, oct: {0:o}, hex: {0:x}".format(42)
>>> 'int: 42, oct: 52, bin: 101010, hex: 2a'

#함수(!6진법까지)
def toN(n, num=2):
    res=[]
    res2=''
    while n>0:
       n, tmp = divmod(n, num)
       res.append((str(tmp) if tmp <10 else 'ABCDEF'[tmp-10]))

    for i in range(len(res)):
        res2 += res.pop()

    return res2
```

# 순환 참조
```python
num = '123456'

# 3개 씩 잘라보기 (ex. '123', '456', '234', '561'...)
k = 3
for i in range(2):
    for j in range(0, len(num), 3):
        print(str[j:j+k+1])
    num = num[1:] + num[0]
```

# 맵 뒤집기
```python
#board 가로길이 W, 세로길이 H
new_board = [[board[i][j] for i in reversed(range(H))] for j in range(W)]
```
