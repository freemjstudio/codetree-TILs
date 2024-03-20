import functools 

n, m = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0 

def find_max_xor(idx, cnt, cur_val):
    global answer 
    
    if cnt == m:
        answer = max(answer, cur_val)
        return 
    if idx == n:
        return 
    # index에 있는 숫자를 선택하지 않은 경우 
    find_max_xor(idx+1, cnt, cur_val)

    # index에 있는 숫자를 선택한 경우 
    find_max_xor(idx+1, cnt+1, cur_val ^ arr[idx])

find_max_xor(0, 0, 0)
print(answer)