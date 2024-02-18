n, m = map(int, input().split())
arr = []

for _ in range(n):
    data = list(map(int, input().split()))
    arr.append(data)

answer = 0

for i in range(n): # 가로 
    count = 1 
    for j in range(n-1):
        if arr[i][j] == arr[i][j+1]:
            count += 1
        else:
            count = 1
        
    if count >= m:
        answer += 1

for i in range(n):
    count = 1 
    for j in range(n-1):
        if arr[j][i] == arr[j+1][i]:
            count += 1
        else: 
            count = 1
    if count >= m:
        answer += 1
    

print(answer)