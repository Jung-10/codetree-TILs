n = int(input())

result_list = [n]

while n != 1 :
    n = n // 3
    result_list.append(n)

result_list.reverse()

for i in result_list :
    print(i, end = ' ')