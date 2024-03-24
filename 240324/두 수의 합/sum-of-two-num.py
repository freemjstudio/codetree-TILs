from collections import defaultdict 
n, k = map(int, input().split())
arr = list(map(int, input().split()))

numbers = defaultdict(list)
for idx, elem in enumerate(arr):
    numbers[elem].append(idx) # 위치 

answer = 0 

for key, value in numbers.items():
    tmp = (k - key)
    if tmp in numbers:
        answer += (len(value) * len(numbers[tmp]))

print(answer//2)