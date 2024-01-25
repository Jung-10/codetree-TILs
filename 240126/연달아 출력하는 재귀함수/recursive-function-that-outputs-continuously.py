n = int(input())
result_list = [n]

while n != 1 :
    n = n // 3
    result_list.append(n)

reversed_list = list(reversed(result_list))

print(*reversed_list)