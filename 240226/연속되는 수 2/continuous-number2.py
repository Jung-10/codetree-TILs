n = int(input())

arr = []

for _ in range(n) :
    arr.append(int(input()))

cnt = 0
max_cnt = 0
for i in range(1, n) :
    if arr[i] == arr[i-1] :
        cnt += 1
    else :
        max_cnt = max(cnt, max_cnt)
        cnt = 0
    
    max_cnt = max(cnt, max_cnt)

print(max_cnt + 1)