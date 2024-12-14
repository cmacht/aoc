from functools import cache

with open("input") as f:
    nums = [int(n) for n in f.read().split()]

print(nums)

# for n in nums:
#     for i in range(25):


def conquer(n, count=0):
    """ This is me, trying to figure out recursion
    """
    cur = calc(n)
    count += 1
    if count == 25:
        print(cur)
    if isinstance(cur, tuple):
        conquer(cur[0], count)
        conquer(cur[1], count)
    else:
        conquer(cur, count)


@cache
def calc(stone, steps):
    """ This is HyperNeutrinos Implementation, it doesn't work well without cache!
    """
    if steps == 0:
        return 1
    if stone == 0:
        return calc(1, steps - 1)
    ss = str(stone)
    if len(ss) % 2 == 0:
        l = ss[:len(ss) // 2]
        r = ss[len(ss) // 2:]
        return calc(int(l), steps - 1) + calc(int(r), steps - 1)
    return calc(stone * 2024, steps - 1)

print(sum(calc(n, 75) for n in nums))
