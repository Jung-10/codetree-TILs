n = int(input())
num_list = list(map(int, input().split(' ')))

result = [i * i for i in num_list]

print(*result)

# *은 unpacking 연산자(asterisk)
# 리스트나 튜플과 같은 iterable 객체의 요소를 풀어서 전달 가능