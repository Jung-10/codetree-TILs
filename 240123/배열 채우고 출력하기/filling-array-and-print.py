char_list = input().split(' ')

print(''.join(char_list[::-1]))

# 전체 원소를 뒤집고 싶다면, start, end를 모두 비우고 step에 -1만 적으면 됨.
# join()을 사용하면 문자열을 합칠 수 있음.