arr = [int(i) for i in open("легкий уровень.txt")]
n = arr[0]
arr = arr[1:]

count_max = 0
count_tk = 0
count_mx = 25

for i in arr:
    if i == 2:
        if count_tk < count_mx:
            count_tk += 1
        count_max = max(count_max, count_tk)
    if i == 3:
        count_mx += 1
        if count_tk < count_mx:
            count_tk += 1
        count_max = max(count_max, count_tk)
    if i == 1:
        count_tk = 0
        count_mx = 25

print(count_tk, count_max)



