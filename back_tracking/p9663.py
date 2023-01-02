import sys
count: int = 0

def is_valid(idx, temp):
    i = 0
    while i < idx:
        if temp[i] == temp[idx] or abs(temp[i] - temp[idx]) == idx - i:
            return False
        i +=1
    return True

def dfs(idx, temp):
    global count
    n = len(temp)
    if is_valid(idx, temp):
        if idx == n - 1:
            count +=1
        else :
            num = 0
            while num < n:
                temp[idx + 1] = num
                dfs(idx + 1, temp)
                num += 1

N = int(sys.stdin.readline().rstrip())
temp = [0] * N
dfs(-1, temp)
print(count)