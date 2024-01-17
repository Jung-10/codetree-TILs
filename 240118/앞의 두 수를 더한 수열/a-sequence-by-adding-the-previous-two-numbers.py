n = int(input())

num_list = [0, 1]
result = 0

for i in range(n - 1) :
    result = num_list[i] + num_list[i+1]
    num_list.append(result)

print(num_list[n])