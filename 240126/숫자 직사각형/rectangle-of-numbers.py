n, m = map(int, input().split())

# 2차원 배열 구현
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

cnt = 1

# n * m 크기의 배열에 숫자 채우기
for i in range(n) :
    for j in range(m) :
        arr[i][j] = cnt
        cnt += 1

for row in arr:
	for elem in row:
		print(elem, end=" ")
	print()