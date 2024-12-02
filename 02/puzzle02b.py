from itertools import pairwise

with open("input-training") as f:
    nums = [lvl.split() for lvl in f.read().splitlines()]

print(nums)
sum = 0
for lvl in nums:
    failed = False
    decreasing = None
    increasing = None
    joker = True
    counter = 0

    while counter < len(lvl):
        print(lvl)
        x = lvl[counter]
        y = lvl[counter + 1]
        print(counter, x, y)
        diff = int(x) - int(y)
        if diff < 0 and decreasing is None:
            decreasing = True
        if diff > 0 and increasing is None:
            increasing = True
        if increasing is True and decreasing is True:
            failed = True
            print('failed inc_dec at', counter)
        if abs(diff) >= 1 and abs(diff) <= 3:
            pass
        else:
            failed = True
            print('failed limit at', counter)

        if failed and joker:
            joker = False
            del lvl[counter + 1]
            print('try again')
            counter = 0
            increasing = None
            decreasing = None
            failed = False
            continue
        if counter < len(lvl) - 2:
            counter += 1
            continue
        else:
            break

    if not failed:
        sum += 1
        print('--- added! ---')
    else:
        print('--- not added! ---')
print(sum)