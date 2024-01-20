n = int(input())
num_list = [n]

while n != 1 : # n이 1이 될때까지 반복
    if n % 2 == 0 : # 짝수일 때
        n = n // 2
        num_list.append(n)

    elif n % 2 == 1 : # 홀수일 때
        n = n // 3
        num_list.append(n)

for i in num_list : # 모든 출력값 사이에 공백을 두고 출력
    print(i, end = ' ')