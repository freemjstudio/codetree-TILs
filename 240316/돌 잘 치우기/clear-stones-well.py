from itertools import combinations
from collections import deque 
import sys 
input = sys.stdin.readline
n, k, m = map(int, input().split())

arr = []
rocks = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            rocks.append((i, j))
    arr.append(line)

start_pos = []
for _ in range(k):
    r, c = map(int, input().split())
    start_pos.append((r, c))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy, comb):
    queue = deque([(sx, sy)])
    visited = [[0] * n for _ in range(n)]
    
    count = 0 # enqueue 할 떄 count 
    while queue: 
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if arr[nx][ny] == 0 or (nx, ny) in comb:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    count += 1

    return count 

answer = 0 # max
if m > 0:
    remove_rock_comb = list(combinations(rocks, m))
    for comb in remove_rock_comb:
        for sx, sy in start_pos:
            answer = max(bfs(sx, sy, list(comb)), answer)
else: 
    for sx, sy in start_pos:
        answer = max(bfs(sx, sy, []), answer)

print(answer)