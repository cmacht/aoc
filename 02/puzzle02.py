from itertools import pairwise

with open("input") as f:
    nums = [lvl.split() for lvl in f.read().splitlines()]

sum = 0
for lvl in nums:
    failed = False
    decreasing = None
    increasing = None
    for x, y in pairwise(lvl):
        diff = int(x) - int(y)
        print(diff)
        if diff < 0 and decreasing is None:
            decreasing = True
        if diff > 0 and increasing is None:
            increasing = True
        if increasing is True and decreasing is True:
            failed = True
            print('failed')
        if abs(diff) >= 1 and abs(diff) <= 3:
            continue
        else:
            failed = True
            print('failed')
            break
    if not failed:
        sum += 1
print(sum)