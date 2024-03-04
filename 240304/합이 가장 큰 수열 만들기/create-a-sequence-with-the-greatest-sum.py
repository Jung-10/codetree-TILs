n = int(input())

arr = [
    int(input())
    for _ in range(n)
]
arr = sorted(arr)

cur_cnt = 1
max_cnt = 0

cur_sum = 0
max_sum = 0

for i in range(n - 1) :
    if arr[i] + 1 == arr[i + 1] :
        cur_cnt += 1
        cur_sum += arr[i]
    else : 
        cur_sum += arr[i]
        max_cnt = max(cur_cnt, max_cnt)
        max_sum = cur_sum
        
print(max_sum)