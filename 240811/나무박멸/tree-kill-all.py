n, m, k, c = map(int, input().split())

answer = 0  # m 년 동안 총 박멸할 나무 그루 수
arr = []
killer_arr = [[0] * n for _ in range(n)]  # 제초제 위치와 남은 년수 기록하기, 벽의 위치 정보는 필요함

for i in range(n):
    arr.append(list(map(int, input().split())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 대각선 탐색
dx2 = [-1, 1, -1, 1]
dy2 = [-1, -1, 1, 1]

def growth():
    grow_pos = []  # 성장이 일어날 위치 기록

    for x in range(n):
        for y in range(n):
            if arr[x][y] > 0:  # 나무가 있으면 상하좌우 탐색하기
                # 인접한 네 개의 칸 중 나무가 있는 칸의 수 카운트
                cnt = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if (0 <= nx < n and 0 <= ny < n):
                        if arr[nx][ny] > 0:
                            cnt += 1
                if cnt > 0:
                    grow_pos.append((x, y, cnt))
    # update arr
    for x, y, amount in grow_pos:
        arr[x][y] += amount


def breeding():
    breeding_arr = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if arr[x][y] > 0:
                new_pos = []
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if (0 <= nx < n and 0 <= ny < n):
                        if arr[nx][ny] == 0 and killer_arr[nx][ny] == 0:
                            new_pos.append((nx, ny))
                if not new_pos:
                    continue 
                
                amount = (arr[x][y] // len(new_pos))
                for nx, ny in new_pos:
                    breeding_arr[nx][ny] += amount 
    # update arr
    for i in range(n):
        for j in range(n):
            arr[i][j] += breeding_arr[i][j]

def spread(x, y):
    killer_arr[x][y] = c+1
    if arr[x][y] == 0: # 빈칸의 경우 나무가 없으므로 번식할 수 없음
        return

    arr[x][y] = 0 # 나무 박멸
    for i in range(4):
        for j in range(1, k+1):
            nx, ny = x + dx2[i] * j, y + dy2[i] * j
            if not (0 <= nx < n and 0 <= ny < n):
                break
            if arr[nx][ny] == 0 or arr[nx][ny] == -1:
                killer_arr[nx][ny] = c + 1
                break
            arr[nx][ny] = 0 # 나무 박멸
            killer_arr[nx][ny] = c + 1

def spread_test(x, y):
    result = arr[x][y] # x, y 기준으로 제초제 뿌렸을 때 결과
    if arr[x][y] == 0: # 빈칸의 경우 Return 0
        return 0
    for i in range(4):
        for j in range(1, k+1):
            nx, ny = x + dx2[i] * j, y + dy2[i] * j
            if not (0 <= nx < n and 0 <= ny < n):
                break
            if arr[nx][ny] == 0 or arr[nx][ny] == -1:
                break
            result += arr[nx][ny]
    return result

def execute_spread():
    global answer
    max_kill, max_x, max_y = 0, 0, 0
    for x in range(n):
        for y in range(n):
            if arr[x][y] == -1: # 벽
                continue
            tmp = spread_test(x, y)
            if tmp > max_kill:
                max_kill, max_x, max_y = tmp, x, y # 갱신하기

    if not max_kill: # 0
        return False
    spread(max_x, max_y)
    answer += max_kill
    return True

# 제초제 1년 유효기간 반영 및 제초제 없애기
def remove_killer():
    for x in range(n):
        for y in range(n):
            killer_arr[x][y] = max(0, killer_arr[x][y] - 1)

def print_arr(a):
    for i in range(n):
        print(*a[i])
    print()

for year in range(m):
    growth()  # 나무 성장
    # print("GROWTH")
    # print_arr(arr)
    breeding()  # 나무 번식 소리
    # print("KILLER")
    # print_arr(killer_arr)
    # print("BREEDING")
    # print_arr(arr)
    result = execute_spread()
    if not result: # 더이상 제초제 뿌릴 수 없는 경우
        break
    # 새롭게 제초제를 뿌린 공간은 남은 년수를 remove_killer에서 빼면 안됨 !
    remove_killer()

print(answer)

"""
5 2 2 1
0 0 0 0 0
0 30 23 0 0
0 0 -1 0 0
0 0 17 46 77
0 0 0 12 0

330
"""