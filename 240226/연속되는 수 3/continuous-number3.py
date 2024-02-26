n = int(input())

arr = [
	int(input())
	for _ in range(n)
]

cnt = 0
result = 0
for i in range(n) :
    if (arr[i] > 0 and arr[i-1] > 0) or (arr[i] < 0 and arr[i-1] < 0) :
        cnt += 1
    else :
        cnt = 0
    
    result = max(cnt, result)

print(result + 1)