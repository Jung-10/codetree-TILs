n = int(input())

answer = []

while True :
    if n < 2 :
        answer.append(n)
        break
    
    answer.append(n % 2)
    n = n // 2

for elem in answer[::-1] :
    print(elem, end='')