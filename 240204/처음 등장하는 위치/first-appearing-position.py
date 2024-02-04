from sortedcontainers import SortedDict

n = int(input())
data = list(map(int, input().split()))
s = SortedDict() 

# 오름차순 정렬
for i in range(n):
    if data[i] not in s: 
        s[data[i]] = (i+1) 

for k, v in s.items():
    print(k, v)