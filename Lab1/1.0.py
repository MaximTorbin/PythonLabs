n = 3
s = [int(input()) for i in range(n)]
min_num = s[0]
max_num = s[0]

for num in s:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

print("Минимальное число:", min_num)
print("Максимальное число:", max_num)
