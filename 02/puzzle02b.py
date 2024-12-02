from itertools import pairwise

with open("input") as f:
    # deltas = [[int(b) - int(a) for a, b in pairwise(levels.split())] for levels in f.read().splitlines()]
    levels_list = [[int(i) for i in l.split()] for l in f.read().splitlines()]

print(levels_list)
ans = 0

def is_safe(levels):
    print(levels)
    reversion_ok = (levels==sorted(levels) or levels==sorted(levels, reverse=True))
    limit_ok = True
    deltas = [y - x for x, y in pairwise(levels)]
    if not all(0 < abs(x) <= 3 for x in deltas):
        limit_ok = False
    return reversion_ok and limit_ok

for levels in levels_list:
    if any(is_safe(levels[:idx] + levels[idx+1:]) for idx in range(len(levels))):
        ans += 1

print('ans:', ans)
