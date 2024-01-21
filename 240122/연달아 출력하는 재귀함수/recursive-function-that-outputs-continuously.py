# 방법 1 : 메모리 초과 - 리스트 사용보다 필요한 값을 직접 계산하거나 저장하는 방식으로 코드 변경
n = int(input())

result_list = [n]

while n != 1 :
    n = n // 3
    result_list.append(n)

result_list.reverse()

for i in result_list :
    print(i, end = ' ')


# n = int(input())

# while n != 1:
#     print(n, end=' ')
#     n = n // 3

# print(1, end=' ')