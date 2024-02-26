n = int(input())

arr = []

for _ in range(n) :
    arr.append(int(input()))

cnt = 0
max_cnt = 0
for i in range(n) :
    if arr[i] != arr[i-1] or i == 0 :
        cnt += 1

print(cnt)