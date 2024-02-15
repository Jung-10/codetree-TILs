binary = list(map(int, list(input())))

num = 0
for i in range(len(binary)) :
    num = num * 2 + binary[i]

num = num * 17

answer = []
while True :
    if num < 2 :
        answer.append(num)
        break

    answer.append(num % 2)
    num = num // 2

for i in answer[::-1] :
    print(i, end = "")