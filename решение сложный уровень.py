arr = [int(i) for i in open("сложный уровень.txt")]
n = arr[0]
arr = arr[1:]

count_max = 0
count_tk = 0
count_mx = 20
shard = False
for i in arr:
    if i == 4:
        shard = True
        if count_mx <= 25: count_mx = 25 #если текущий максимум и так больше 25, то смысла его трогать нет
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
        count_tk = int(count_tk * 0.75)
        if shard: count_mx = 25
        else: count_mx = 20

print(count_tk, count_max)
