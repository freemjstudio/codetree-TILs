n, m = map(int, input().split())
hash_map = {}
for idx in range(1, n+1):
    x = input()
    hash_map[x] = str(idx) 
    hash_map[str(idx)] = x

# # cnd 
for _ in range(m):
    temp = input()
    print(hash_map[temp])