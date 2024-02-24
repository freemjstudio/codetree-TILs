n, m = map(int, input().split())
array = []
# n * n 영역 
for _ in range(n): 
    array.append(list(map(int, input().split())))

# 마름모 넓이에 속한 block (1*1) 개수 반환 
def get_block(s): 
    return s *s + (s+1) * (s+1)
answer = 0

dxs = [1, 1, -1, -1]
dys = [-1, 1, 1, -1]

def is_in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True 
    return False 

# 채굴 가능한 금 확인 
def get_gold(x, y, k):
    gold = 0 
    # 시작점 칸 확인 
    gold += array[x][y] 
    # 중심점을 기준으로 cur_k 만큼 떨어져 있음 
    for cur_k in range(1, k+1): 
        cur_x, cur_y = x - cur_k, y
        for dx, dy in zip(dxs, dys): # 이동 방향 
            for step in range(cur_k): # 이동 반복 횟수 
                if is_in_range(cur_x, cur_y):
                    gold += array[cur_x][cur_y]
                # 좌표 갱신하기 
                cur_x, cur_y = cur_x + dx, cur_y + dy

    return gold 



# 격자 탐색하기 
for i in range(n):
    for j in range(n):
        for k in range(2*n):
            gold = get_gold(i, j, k)
            if gold*m >= get_block(k):
                answer = max(gold, answer)
    
print(answer)