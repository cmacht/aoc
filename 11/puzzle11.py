with open("input") as f:
    nums = [int(n) for n in f.read().split()]

print(nums)

for i in range(75):
    new = []
    for n in nums:
        ns = str(n)
        if n == 0:
            new.append(1)
        elif len(ns) % 2 == 0:
            l = ns[:len(ns) // 2]
            r = ns[len(ns) // 2:]
            new.extend([int(l), int(r)])
        else:
            new.append(n * 2024)
    nums = new[:]
    # print(f'blink {i}:', nums)
    print(i)

print(len(nums))
