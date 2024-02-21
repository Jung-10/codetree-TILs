n = int(input())

offset = 100

# N장의 정사각형의 좌측하단 꼭지점들의 input값
input_arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# 원래 [-100, 100] * [-100, 100] 격자 내의 칸들인데
# 양수부분으로 계산하기 위해서 [0, 200] * [0, 200]
color_arr = [
    [0 for _ in range(200 + 1)]
    for _ in range(200 + 1)
]

# 직사각형을 칠해줌.
# 격자 단위로 진행하는 문제이므로 x2, y2에 등호가 들어가지 않음에 유의

for x1, y1 in input_arr :
    
    x1, y1 = x1 + offset, y1 + offset

    # 길이가 8인 정사각형
    x2, y2 = x1 + 8, y1 + 8

    for x in range(x1, x2) :
        for y in range(y1, y2) :
            color_arr[x][y] = 1
    
# 색종이의 총 넓이
area = 0

for x in range(0, 200 + 1) :
    for y in range(0, 200 + 1) :
        if color_arr[x][y] :
            area += 1

print(area)