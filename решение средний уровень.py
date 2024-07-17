f = open("средний уровень.txt")
n, r = map(int, f.readline().split(" "))
arr = [int(i) for i in f]

count_max = 0
count_tk = 0
count_mx = 25
count = 0

for i in arr:
    if i == 2:
        if count_tk < count_mx:
            count_tk += 1
        count_max = max(count_max, count_tk)
    if i == 3:
        if count_tk > r: count += 1
        count_mx += 1
        if count_tk < count_mx:
            count_tk += 1
        count_max = max(count_max, count_tk)
    if i == 1:
        count_tk = 0
        count_mx = 25

print(count, count_max)