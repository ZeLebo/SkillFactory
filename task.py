a = list(input())
b = set(a)
cnt = {}
for i in a:
    cnt[i] = 0
for i in a:
    if i in b:
        cnt[i] += 1
for i in cnt:
    print (i, "is", cnt.get(i), "times")
