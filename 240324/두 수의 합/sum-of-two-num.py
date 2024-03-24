n, k = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0 
numbers = {}
for idx, elem in enumerate(arr):
    numbers[elem] = idx # 위치 

for i in range(len(arr)): 
    tmp = (k - arr[i])
    if tmp in numbers:
        if i != numbers[tmp]:
            answer += 1

print(answer//2)