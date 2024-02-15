n, b = map(int, input().split())
answer = []

while True :
    if n < 2 and n != 0:
        answer.append(n)
        break

    answer.append(n % b)
    n = n // b

for i in answer[::-1] :
    print(i, end = '')