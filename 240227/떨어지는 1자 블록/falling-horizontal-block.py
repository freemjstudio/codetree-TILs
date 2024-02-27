n, m, k = map(int, input().split())
# block -> 1, empty -> 0 

grid = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

delta = (1, 0) # 아래쪽으로 이동 

# 1. block 삽입하기 
k = k-1 
block_pos = [] # block 을 이루는 좌표 값 
for i in range(m):
    grid[k][i] = 1 # new block 
    block_pos.append((k, i))

# 2. block 객체 이동시키기 
while True:
    # check 
    flag = True 
    new_block_pos = []
    for x, y in block_pos:
        nx, ny = x+1, y 
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0: 
            new_block_pos.append((nx, ny))
        else: 
            flag = False 
    if not flag:
        break 
    # remove prev position 
    for x, y in block_pos:
        grid[x][y] = 0
    # move to new position 
    for x, y in new_block_pos:
        grid[x][y] = 1
    # update
    block_pos = new_block_pos

# 3. answer 
for i in range(n):
    print(*grid[i])