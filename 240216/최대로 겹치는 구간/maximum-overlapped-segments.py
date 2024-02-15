n = int(input())

checked = [0] * (200 + 1)

for _ in range(n) :
    x1, x2 = map(int, input().split())

    for i in range(x1, x2) :
        checked[i] += 1

print(max(checked))