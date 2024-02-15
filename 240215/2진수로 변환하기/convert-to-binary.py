n = int(input())

answer = []

while n != 1 :
    answer.append(n % 2)
    n = n // 2

answer.append(1)

for elem in answer[::-1] :
    print(elem, end='')