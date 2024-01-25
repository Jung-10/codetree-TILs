arr = [
    list(map(int, input().split()))
    for _ in range(2)
]

# 가로 평균
for i in arr :
    print(f"{sum(i) / len(i):.1f}", end = ' ')
print()

# 세로 평균
for j in range(4) :
    sum_val = 0
    for i in range(2) :
        sum_val += arr[i][j]
    print(f"{sum_val / 2:.1f}", end = ' ')
print()

# 전체 평균
sum_val = 0
for i in range(2) :
    for j in range(4) :
        sum_val += arr[i][j]
print(f"{sum_val / 8:.1f}")