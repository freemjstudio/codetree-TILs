n, m, k = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# block 삽입하기 
k = k-1 

def check_block(row, start, end):
    for col in range(start, end):
        if grid[row][col] == 1: # not available 
            return False
    return True 

def get_row():
    for row in range(n-1):
        if not check_block(row + 1, k, k+m-1):
            return row 

    return n - 1 # 최댓값 

max_row = get_row()

# 최종 block 위치 표시하기 
for col in range(k, k+m):
    grid[max_row][col] = 1

# answer 
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()