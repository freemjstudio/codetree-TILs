n = int(input())

data = []
for _ in range(n):
    x, y = map(int, input().split())
    data.append((x, y))
data.sort()

result = {}
for x, y in data: 
    if x not in result:
        result[x] = y

answer = 0 
for k, v in result.items():
    answer += v
print(answer)