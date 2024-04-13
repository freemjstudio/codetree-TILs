n, m, k, C = map(int, input().split())
answer = 0 
grid = []
herb = [[0] * n for _ in range(n)] # 제초제 위치 

for i in range(n):
    grid.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 대각선 이동 
tx = [-1, 1, -1, 1]
ty = [-1, 1, 1, -1]

# 성장 
def grow():
    for i in range(n):
        for j in range(n):
            if grid[i][j] <= 0:
                continue 
            tree_cnt = 0
            for t in range(4):
                nx, ny = i + dx[t], j + dy[t]
                if 0 <= nx < n and 0 <= ny < n:
                    if grid[nx][ny] > 0:
                        tree_cnt += 1
            grid[i][j] += tree_cnt

# 번식 - 번식 가능한 칸의 개수 만큼 번식됨 
def spread(): 
    global tree_pos
    temp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if grid[i][j] <= 0: 
                continue 
            # 번식 가능한 칸 
            cnt = 0 
            for t in range(4):
                nx, ny = i + dx[t], j + dy[t]
                if 0 <= nx < n and 0 <= ny < n: 
                    if herb[nx][ny]:
                        continue
                    if grid[nx][ny] == 0:
                        cnt += 1
            # 번식 진행 
            for t in range(4):
                nx, ny = i + dx[t], j + dy[t]
                if 0 <= nx < n and 0 <= ny < n:
                    if herb[nx][ny]:
                        continue
                    if grid[nx][ny] == 0:
                        temp[nx][ny] += grid[nx][ny] // cnt 

    for i in range(n):
        for j in range(n):
            grid[i][j] += temp[i][j]


# 제초제 위치 구하기 
def get_kill_pos():
    global answer 
    max_kill = 0 
    r, c = -1, -1 # max kill 값의 위치를 구하기 (제초제 뿌릴 위치)

    for i in range(n):
        for j in range(n): 
            if grid[i][j] <= 0: 
                continue 
            kill_count = grid[i][j]
            for t in range(4):
                nx, ny = i, j 
                for _ in range(k): # 대각선 방향 K 까지 영향줌 
                    nx += tx[t]
                    ny += ty[t]
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != -1: 
                        kill_count += grid[nx][ny]
                    else: # 범위 벗어나면 확산 중단  
                        break 
            if max_kill < kill_count:
                max_kill = kill_count
                r, c = i, j
    
    answer += max_kill

    # 제초제 뿌리기 
    if grid[r][c] > 0:
        grid[r][c] = 0 
        herb[r][c] = C 

        for t in range(4):
            nx, ny = r, c 
            for _ in range(k):
                nx, ny = nx + tx[t], ny + ty[t]
                if 0 <= nx < n and 0 <= ny < n:
                    if grid[nx][ny] < 0:
                        break # 벽인 경우 
                    if grid[nx][ny] == 0: # 나무 없는 경우 
                        herb[nx][ny] = C
                        break 
                    grid[nx][ny] = 0 
                    herb[nx][ny] = C 


def delete_herb():
    for i in range(n):
        for j in range(n):
            if herb[i][j] > 0:
                herb[i][j] -= 1

for _ in range(m):
    grow()
    spread()
    get_kill_pos()
    delete_herb() # 제초제 1년 감소 

print(answer)