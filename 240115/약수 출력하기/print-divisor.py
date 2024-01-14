n = int(input())
answer = []

# 방법 1 => 시간초과
# for i in range(1, n + 1) :
#     if n % i == 0 :
#         answer.append(i)

# for j in answer :
#     print(j, end = " ")

for i in range(1, int(round(n**(1/2), 0)) + 1) :
    if n % i == 0 :
        answer.append(i)
        answer.append(n // i)

answer = sorted(answer)

for j in answer :
    print(j, end = " ")