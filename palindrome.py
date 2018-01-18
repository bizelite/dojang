max_pal = 0
cur_pal = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        cur_pal = i * j
        if str(cur_pal) == str(cur_pal)[::-1] and cur_pal > max_pal:
            max_pal, cur_pal = cur_pal, max_pal
print(max_pal)
