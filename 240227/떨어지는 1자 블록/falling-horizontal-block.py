n, m, k = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))


# block 삽입하기 
k = k-1 
block_pos = [] # block 을 이루는 좌표 값 

max_row = 0 # 가장 낮게 내려갈 수 있는 열의 위치 찾기 
for row in range(n):
    for col in range(k, k+m):
        if grid[row][col] == 1: 
            max_row = row -1 
            break 
max_row -= 1
# 최종 block 위치 표시하기 
for col in range(k, k+m):
    grid[max_row][col] = 1

# answer 
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()