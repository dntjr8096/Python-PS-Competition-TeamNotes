# 가장 기본적인 입력 받기

### 1줄 입력
```python
N, M = map(int, input().split())  #공백 구분하여 입력받기
```

### 한 줄 한 번에 입력 받기
```python
input_data = sys.stdin.readline().rstrip() # rstrip 필수!(엔터 제거)
```

### 여러줄 입력
```python
data = [list(map(int, input().split())) for _ in range(n)]
```

### 포맷팅 출력
```python
print("%d %s" % (100, 'exam'), end='')

val = 10
print(f'val = {val}')

print("val = {0}".format(10))
```