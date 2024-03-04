def fibbo(n) :
    if memo[0] != -1 :
        return memo[n]
    
    if n <= 2 :
        memo[n] = 1
    else :
        memo[n] = fibbo(n - 1) + fibbo(n - 2)

    return memo[n]

n = int(input())
memo = [-1] * (n + 1)  # 메모이제이션을 위한 배열 초기화
result = fibbo(n)
print(result)