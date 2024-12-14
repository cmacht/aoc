from functools import cache

with open("input") as f:
    nums = [int(n) for n in f.read().split()]

print(nums)

@cache
def calc(n):
    ns = str(n)
    if n == 0:
        return [1]
    elif len(ns) % 2 == 0:
        l = ns[:len(ns) // 2]
        r = ns[len(ns) // 2:]
        return [int(l), int(r)]
    else:
        return [n * 2024]


for i in range(75):
    new = []
    for n in nums:
        new.extend(calc(n))
    nums = new[:]
    # print(f'blink {i}:', nums)
    print(i)

print(len(nums))
