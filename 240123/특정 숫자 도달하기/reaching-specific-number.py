# append : 리스트 맨 끝에 원소 추가
# pop : 리스트 맨 뒤에 있는 원소 지울 수 있음
# len : 리스트에 있는 원소의 개수 반환

num_list = list(map(int, input().split()))
result_list = []

for i in num_list :
    if i >= 250 :
        break

    elif i < 250 :
        result_list.append(i)

print(sum(result_list), round(sum(result_list) / len(result_list), 1))