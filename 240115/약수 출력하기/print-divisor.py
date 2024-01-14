n = int(input())
answer = []

# 방법 1 => 시간초과(2^31 - 1개를 전부 확인할 경우 시간 초과 발생)
# for i in range(1, n + 1) :
#     if n % i == 0 :
#         answer.append(i)

# for j in answer :
#     print(j, end = " ")

# 방법 2 => N개의 수를 전부 보지 않음.
for i in range(1, int(round(n**(1/2), 0)) + 1) :
    if n % i == 0 :
        answer.append(i)
        answer.append(n // i)

answer = sorted(answer)
answer = list(set(answer)) # set 타입으로 변경하면서 중복 제거

for j in answer :
    print(j, end = " ")