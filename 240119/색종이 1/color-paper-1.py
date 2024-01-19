n = int(input()) # 정사각형 n장

result_list = [[0 for _ in range(500)] for _ in range(500)] # 전체 평면 - 이중리스트

for i in range(n) :
    x1, y1 = list(map(int, input().split())) # 각각 정사각형 x, y 좌표
    x2, y2 = x1 + 10, y1 + 10 # 가로, 세로의 크기가 각각 10인 정사각형
    for x in range(x1, x2) :
        for y in range(y1, y2) :
            result_list[x][y] += 1
    
# 0이 아닌 숫자의 개수를 세는 함수
def count_non_zero(count_list):
    return sum(1 for row in count_list for element in row if element != 0)

count = count_non_zero(result_list)
print(count)