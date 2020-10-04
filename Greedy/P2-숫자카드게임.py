'''
문제
- 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장 뽑기
1. 숫자 카드들은 NXM 형태로 놓여있다.
2. 먼저, 뽑고자 하는 카드가 있는 행을 선택한다.
3. 선택된 행에 포함된 카드들 중 가장 낮은 카드를 선택한다.

input Sample
3 3
3 1 2
4 1 4
2 2 2
result : 2

2 4
7 3 1 8
3 3 3 4
result : 3
'''

n, m = map(int, input().split())
cards_list = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for cards in cards_list:
    min_card = min(cards)
    answer = max(answer, min_card)

print(answer)