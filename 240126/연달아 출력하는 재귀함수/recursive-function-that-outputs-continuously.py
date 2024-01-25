def function(n):
    if n < 3:
        return [n]
    
    next_number = n // 3
    result = function(next_number)
    result.append(n)
    
    return result

# 입력
n = int(input())

# 결과 출력
result = function(n)
print(" ".join(map(str, result)))