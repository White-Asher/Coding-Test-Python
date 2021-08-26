# ==============================================================================================================
# <문제> 모험가 길드

# 한 마을에 모험가가 N명 있습니다. 모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 츨정했는데,
# '공포도'가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다.

# 모험가 길드장인 철수는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명이상으로
# 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했습니다.

# 철수는 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금합니다. N명의 모험가에 대한 정보가 주어졌을 때, 
# 여행을 떠날 수 있는 그룹 수의 최대값을 구하는 프로그램을 작성하세요.
# 난이도 1, 풀이시간 30분, 시간제한 1초,

# 입력조건 
# 첫째 줄에 모험가의 수 N이 주어집니다.(1<=N<=100000)
# 둘째 줄에 각 모험가의 공포도의 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.

# 출력조건
# 여행을 떠날 수 있는 그룹 수의 최대값을 출력합니다.

# 입력예시
# 5
# 2 3 1 2 2

# 출력예시
# 2
# ==============================================================================================================

n = int(input())
data = list(map(int,input().split()))
result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모함가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화
        
print(result) # 총 그룹의 수 출력