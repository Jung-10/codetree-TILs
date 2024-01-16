def solution(n) :
    sum = 0 
    for i in range(10, n + 1) :
        sum += i
    return sum

n = int(input())
print(solution(n))