n, k = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0 

for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j:
            continue
        if arr[i] + arr[j] == k:
            answer += 1

print(answer//2)