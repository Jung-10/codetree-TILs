offset = 1000

# a : 첫 번째 직사각형, b : 두 번째 직사각형
ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())

# 문제에서 주어지는 좌표가 음수 값을 갖기 때문에 주어지는 좌표에 대해 전부 offset을 더한 후 진행
ax1, ay1, ax2, ay2 = ax1 + offset, ay1 + offset, ax2 + offset, ay2 + offset
bx1, by1, bx2, by2 = bx1 + offset, by1 + offset, bx2 + offset, by2 + offset

# 칠해지는 부분 체크하기 위한 배열
color_arr = [
    [0 for _ in range(2000 + 1)]
    for _ in range(2000 + 1)
]

# 첫 번째 직사각형 색칠 
for x in range(ax1, ax2) :
    for y in range(ay1, ay2) :
        color_arr[x][y] = 1

# 두 번째 직사각형 색칠 (첫 번째 직사각형과 겹치는 부분이면 두고 아니면 0으로 바꿔줌)
for x in range(bx1, bx2) :
    for y in range(by1, by2) :
        if color_arr[x][y] == 1 :
            color_arr[x][y] = 1
        elif color_arr[x][y] != 1 :
            color_arr[x][y] = 0

# 남은 부분을 덮기 위한 사각형의 최소 넓이
area = 0
for x in range(2000 + 1) :
    for y in range(2000 + 1) :
        if color_arr[x][y] == 1 :
            area += 1

print(area)