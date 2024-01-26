arr_1 = [
    list(map(int, input().split()))
    for _ in range(3)
]

input()

arr_2 = [
    list(map(int, input().split()))
    for _ in range(3)
]

result_arr = [
    [0 for _ in range(3)]
    for _ in range(3)
]

for i in range(3) :
    for j in range(3) :
        result_arr[i][j] = arr_1[i][j] * arr_2[i][j]  

for row in result_arr :
    for elem in row :
        print(elem, end = " ")
    print()