n = int(input())

num_sum = 0
result_list = [1, 1]

for i in range(2, n) :
    num_sum = result_list[i - 1] + result_list[i - 2]
    result_list.append(num_sum)

print(result_list[n-1])