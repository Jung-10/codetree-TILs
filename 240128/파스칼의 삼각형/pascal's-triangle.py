n = int(input())

arr = [
    [0 for j in range(i+1)]
    for i in range(n)
]

arr[0][0] = 1
arr[1][0] = 1
arr[1][1] = 1

# 첫 번째 열은 모두 1로 초기화, 마지막 열 모두 1로 초기화
for i in range(n):
    arr[i][0] = 1
    arr[i][i] = 1

for i in range(n) :
    for j in range(1, i) :
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for elem in arr :
    print(*elem)