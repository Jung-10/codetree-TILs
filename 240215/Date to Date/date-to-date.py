m1, d1, m2, d2 = map(int, input().split())

def num_of_days(m, d) :
    #          1.  2.  3.  4.  5.  6.  7.  8.  9.  10. 11. 12.  
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30 ,31, 30, 31]

    total_days = 0

    # 1월부터 (m-1)월 까지는 다 채워져 있음.
    for i in range(1, m) :
        total_days += days[i]

    # m월은 d일만큼
    total_days += d

    return total_days


total_days = num_of_days(m2, d2) - num_of_days(m1, d1) + 1

print(total_days)