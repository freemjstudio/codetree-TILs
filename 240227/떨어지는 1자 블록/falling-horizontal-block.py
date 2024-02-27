n, m, k = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

delta = (1, 0) # 아래쪽으로 이동 

# block 삽입하기 
k = k-1 
block_pos = [] # block 을 이루는 좌표 값 

max_row = 0 # 가장 낮게 내려갈 수 있는 열의 위치 찾기 
for row in range(n-1):
    for col in range(k, k+m-1):
        if grid[row][col] == 1: 
            break 
    max_row = row  
max_row -= 1
for col in range(k, k+m):
    grid[max_row][col] = 1

# answer 
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()