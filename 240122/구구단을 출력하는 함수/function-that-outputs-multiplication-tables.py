# 방법 1 : 런타임 에러
# 1. 받은 숫자 리스트에 넣어서 정렬
# 2. 3개 중 2번째 숫자와 같으면 출력하지않고 나머지는 출력

# x, y, z = map(int, input().split(' '))

# xyz_list = [x, y, z]
# xyz_list = sorted(xyz_list)

# for i in range(xyz_list[0], xyz_list[2] + 1) :
#     if i == xyz_list[1] :
#         continue
#     for j in range(1, 10) :
#         print('{0} * {1} = {2}'.format(i, j, i * j))

# 방법 2 :
# 함수 사용

def print_multiplication_table(exclude_value, start, end):
    for i in range(start, end + 1):
        if i == exclude_value:
            continue
        for j in range(1, 10):
            print('{0} * {1} = {2}'.format(i, j, i * j))

x, y, z = map(int, input().split(' '))
xyz_list = [x, y, z]
xyz_list.sort()

exclude_value = xyz_list[1]

print_multiplication_table(exclude_value, xyz_list[0], xyz_list[2])