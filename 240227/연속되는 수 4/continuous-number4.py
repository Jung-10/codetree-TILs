n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

cnt = 0
cnt_max = 0
for i in range(n) :
    if arr[i-1] < arr[i] :
        cnt += 1
    else :
        cnt = 1
    cnt_max = max(cnt, cnt_max)

print(cnt_max)