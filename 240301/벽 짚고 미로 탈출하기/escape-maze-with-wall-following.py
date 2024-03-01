n = int(input())
x, y = (map(int, input().split()))
grid = []
# 반시계 방향 순서 
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
answer = -1 
flag = False 
dir_idx = 0 # 현재 방향 기록 

for _ in range(n):
    grid.append(list(input()))
visited = [[False] * n for _ in range(n)]

def check_escape(i, j):
    if (i < 0 or i >= n) or (j < 0 or j >=n):
        return True # 탈출 
    return False 

cur_x, cur_y = x, y
def is_in_range(i, j):
    if (0 <= i < n) and (0 <= j < n):
        return True 
    else: 
        return False 

while True: 
    nx, ny = cur_x + dx[dir_idx], cur_y + dy[dir_idx]
    if check_escape(nx, ny):
        flag = True 
        break
    # 바라보고 있는 방향으로 이동하는 것이 가능하지 않은 경우
    if is_in_range(nx, ny) and grid[nx][ny] == '#':
        dir_idx += 1 # 반시계 방향으로 90만큼 바꾸기 
        continue 
        # 이동했다 가정했을 때 해당 방향을 기준으로 오른쪽에 짚을 벽이 있다
    if is_in_range(nx, ny): 
        right_dir = (dir_idx+3) % 4 
        rx, ry = nx + dx[right_dir], ny + dy[right_dir]
        if is_in_range(rx, ry) and grid[nx][ny] == '#': # 오른쪽에 벽있는지 확인 , visited ? 
            cur_x, cur_y = nx, ny # 한 칸 이동
            answer += 1
            continue
        elif is_in_range(rx, ry) and grid[nx][ny] != '#':
            # 현재 방향으로 한칸 이동 
            cur_x, cur_y = nx, ny 
            answer += 1
            # 시계방향으로 90도 
            dir_idx = (dir_idx + 3) % 4
            cur_x, cur_y = cur_x + dx[dir_idx], cur_y + dy[dir_idx]
            answer += 1
            continue
    if answer > n*n:
        flag = False 
        break 

if flag:
    print(answer)
else: # failed to escape 
    print(-1)