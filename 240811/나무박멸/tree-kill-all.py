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
                    if (0 <= nx < n and 0 <= ny < n) and arr[nx][ny] > 0:
                        cnt += 1
                if cnt > 0:
                    grow_pos.append((x, y, cnt))
    # update arr
    for x, y, amount in grow_pos:
        arr[x][y] += amount


def breeding():
    breeding_pos = []  # 번식이 일어날 위치 기록
    for x in range(n):
        for y in range(n):
            if arr[x][y] > 0:
                new_pos = []
                cnt = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if (0 <= nx < n and 0 <= ny < n):
                        if arr[nx][ny] == 0:
                            cnt += 1
                            new_pos.append((nx, ny))
                if cnt > 0:
                    for nx, ny in new_pos:
                        breeding_pos.append((nx, ny, (arr[x][y] // cnt)))

    # update arr
    for x, y, amount in breeding_pos:
        arr[x][y] += amount


# 가장 많이 박멸할 수 있는 칸 찾기
def find_most_kill_pos():
    max_kill = 0  #
    max_x, max_y = -1, -1  # 가장 많이 박멸할 수 있는 칸
    # 같다면 행이 작은 순서대로, 열이 작은 순서대로
    # 나무가 있는 칸이어야 함
    for x in range(n):
        for y in range(n):
            if arr[x][y] > 0:  # 나무가 있는 칸
                temp_kill_cnt = arr[x][y]
                # 방향은 4가지 대각선
                for i in range(4):
                    nx, ny = x, y
                    for j in range(k):  # k 만큼 이동 가능
                        nx, ny = nx + dx2[i], ny + dy2[i]
                        if (0 <= nx < n and 0 <= ny < n):
                            if arr[nx][ny] > 0:  # 나무가 있는 칸
                                temp_kill_cnt += arr[nx][ny]
                            if arr[nx][ny] == -1:
                                break
                    # print("temp kill cnt", temp_kill_cnt)
                if max_kill < temp_kill_cnt:
                    max_kill = temp_kill_cnt
                    max_x, max_y = x, y
                elif max_kill == temp_kill_cnt:
                    if max_x > x:
                        max_x, max_y = x, y
                    elif max_x == x and max_y > y:
                        max_x, max_y = x, y
    return max_x, max_y


# 나무 박멸하기
def kill_tree(x, y):
    new_killer_pos = []  # 해당 년도에 새롭게 제초제를 뿌린 위치

    # x, y = find_most_kill_pos()
    kill_cnt = arr[x][y]
    killer_arr[x][y] = c
    arr[x][y] = -2
    new_killer_pos.append((x, y))
    # 박멸 실행하기
    for i in range(4):
        nx, ny = x, y
        for j in range(k):
            nx, ny = nx + dx2[i], ny + dy2[i]
            if (0 <= nx < n and 0 <= ny < n):
                if arr[nx][ny] == -1:  # 벽을 만나는 경우
                    break
                    # 박멸한 나무 수 기록하기
                if arr[nx][ny] > 0:
                    kill_cnt += arr[nx][ny]
                    # 제초제 뿌렸음을 표시하기
                    arr[nx][ny] = -2
                    killer_arr[nx][ny] = c
                    # 제초제 유효 기간
                    new_killer_pos.append((nx, ny))
                if arr[nx][ny] == -2:
                    killer_arr[nx][ny] = c
                    new_killer_pos.append((nx, ny))

    return kill_cnt, new_killer_pos


# 제초제 1년 유효기간 반영 및 제초제 없애기
def remove_killer(new_killer_pos):
    for x in range(n):
        for y in range(n):
            if killer_arr[x][y] > 0 and (x, y) not in new_killer_pos:
                killer_arr[x][y] -= 1
                if killer_arr[x][y] == 0 and arr[x][y] == -2:
                    arr[x][y] = 0  # 제초제 효과 없어짐


def print_arr(a):
    for i in range(n):
        print(*a[i])
    print()


for year in range(m):
    growth()  # 나무 성장
    # print("GROWTH")
    # print_arr(arr)
    breeding()  # 나무 번식 소리
    # print("BREEDING")
    # print_arr(arr)
    x, y = find_most_kill_pos()
    if x >= 0 and y >= 0:
        tree, new_killer_pos = kill_tree(x, y)  # 박멸한 나무 수
        answer += tree
    else:
        break 
    # 새롭게 제초제를 뿌린 공간은 남은 년수를 remove_killer에서 빼면 안됨 !

    remove_killer(new_killer_pos)

print(answer)