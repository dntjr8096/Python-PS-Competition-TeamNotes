### 처음 풀이
'''
T = int(input())

def hex2dec(hex):
    dec = 0
    for i in range(len(hex)):
        dec += int(hex[len(hex) - (i + 1)], 16) * (16 ** i)
    return dec

for t in range(T):
    N, K = map(int, input().split())
    R = N // 4

    numbers = input()
    combs = set()
    for i in range(R):
        for j in range(0, N, R):
            _hex = ''
            for k in range(i + j, i + j + R):
                _hex += numbers[k % N]
            combs.add(hex2dec(_hex))

    answer = sorted(combs, reverse=True)[K - 1]
    print(f'#{t + 1} {answer}')
'''
### 리팩토링
T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    R = N // 4
    numbers = input()

    combs = set()
    for _ in range(R):
        for i in range(0, N, R):
            combs.add(int(numbers[i:i+R], 16))
        numbers = numbers[1:] + numbers[0]

    answer = sorted(combs, reverse=True)[K-1]
    print(f'#{t+1} {answer}')
