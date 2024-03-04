n = int(input())

arr = [
    int(input())
    for _ in range(n)
]
arr = sorted(arr)

cur_cnt = 1
max_cnt = 1

cur_sum = arr[0]
max_sum = arr[0]

for i in range(1, n) :
    if arr[i] == arr[i - 1] + 1:
        cur_cnt += 1
        cur_sum += arr[i]
    else : 
        max_cnt = max(cur_cnt, max_cnt)
        max_sum = cur_sum
        cur_cnt = 1
        cur_sum = arr[i]
    
print(max_sum)