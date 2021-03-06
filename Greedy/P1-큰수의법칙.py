'''
문제
1. 다양한 수로 이루어진 배열이 있다.
2. 이 때, 주어진 수들로 M번을 더하여 가장 큰수를 만들어라.
3. 단, 특정한 인덱스의 수를 연속해서 K번 더 할 수 없다.
Ex) arr =[2, 4, 5, 4, 6], K=3, M=5
6 + 6 + 6 + 6 + 6 <- X (틀린 답), 6을 5번 더했으므로 K(3)번을 초과해서 더했다.
6 + 6 + 6 + 5 + 6 <- O (맞는 답), K번 조건을 만족하며 M번 더했을 때 최대 값
'''


n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

count = m // (k+1)
answer = first*(m-count) + second*count

print(answer)
