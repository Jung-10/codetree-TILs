n = int(input())

arr = [
    int(input()) 
    for _ in range(n)
]


cnt = 1
result = 1  # 최소한의 길이는 1이므로 result를 1로 초기화
for i in range(1, n): 
    if (arr[i] > 0 and arr[i-1] > 0) or (arr[i] < 0 and arr[i-1] < 0):
        cnt += 1
    else:
        cnt = 1
    
    result = max(cnt, result)

print(result)