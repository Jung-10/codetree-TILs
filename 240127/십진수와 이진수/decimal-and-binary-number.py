# 이진수 입력받아서 십진수로 변환
n = int(input(), 2)

# 십진수에서 17배 후 다시 이진수로 변환
n_17 = n * 17
n_17 = bin(n_17)

# 이진수로 변환하면 앞에 '0b'가 붙으므로 이진수 부분만 추출
n_list = [i for i in n_17]
n_list = n_list[2:]

print(''.join(n_list))