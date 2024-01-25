n = int(input())

arr = [n]

# 재귀함수
def factorial(n) :
    if n != 1 :
        n = n // 3
        arr.append(n)
        factorial(n)

result = factorial(n)

# 정수 n에서 시작하여 수를 왼쪽으로 이동하며 수를 하나씩 적어야하는데 오른쪽으로 이동해서 출력했으므로 뒤집어주기
reversed_list = list(reversed(arr)) 
print(*reversed_list)