n = 5
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 첫 번째 행은 모두 1로 초기화
for j in range(n):
    arr[0][j] = 1

# 첫 번째 열은 모두 1로 초기화
# 나머지 칸들은 바로 위의 값과 바로 왼쪽의 값을 더 함
for i in range(1, 5) :
    for j in range(5) :
        if j == 0 :
            arr[i][0] = 1
        else :
            arr[i][j] = arr[i-1][j] + arr[i][j-1]

for elem in arr :
    print(*elem)