n = int(input())

offset = 100
arr = [
    [0 for _ in range(200 + 1)]
    for _ in range(200 + 1)
]

for _ in range(n) :
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + offset, y1 + offset, x2 + offset, y2 + offset

    for i in range(x1, x2) :
        for j in range(y1, y2) : 
            arr[i][j] = 1

area = 0
for i in range(0, 200 + 1) :
    for j in range(0, 200 + 1) :
        if arr[i][j] :
            area += 1

print(area)