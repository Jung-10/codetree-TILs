a, b = map(int, input().split())
n = list(input())

num = 0
for i in range(len(n)) :
    num = num * a + int(n[i])

answer = []
while True :
    if num < b :
        answer.append(num)
        break
    
    answer.append(num % b)
    num = num // b

for i in answer[::-1] :
    print(i, end = '')