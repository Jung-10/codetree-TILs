dirs = list(input())

x, y = 0, 0
cur_dir = 3

# 동, 남, 서, 북
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for c_dir in dirs :
    if c_dir == 'L' :
        cur_dir = (cur_dir - 1 + 4) % 4

    elif c_dir == 'R' :
        cur_dir = (cur_dir + 1 ) % 4
    
    elif c_dir == 'F' :
        x, y = x + dx[cur_dir], y + dy[cur_dir]

print(x, y)