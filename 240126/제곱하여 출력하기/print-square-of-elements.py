n = int(input())
num_list = list(map(int, input().split(' ')))

result = [i ** 2 for i in num_list]

for i in result :
    print(i, end = ' ')