from collections import deque 

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    visited = [[-1] * m for _ in range(n)]

    queue = deque([])
    queue.append((sx, sy))
    visited[sx][sy] += 1
    while queue:
        
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and visited[nx][ny] < 0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                
    
    return visited[-1][-1]


answer = bfs(0, 0)
print(answer)