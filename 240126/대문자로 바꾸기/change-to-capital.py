arr = [
    list(input().split())
    for _ in range(5)
]


for row in arr:
    for char in row:
        # 알파벳 소문자를 대문자로 변환
        upper_char = char.upper()
        print(upper_char, end=" ")
    print()