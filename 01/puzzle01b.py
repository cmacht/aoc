with open("input") as f:
    nums = f.read().splitlines()

la = []
lb = []
for num in nums:
    a, b = num.split()
    la.append(int(a))
    lb.append(int(b))

la.sort()
lb.sort()

sum = 0
for item in la:
    multiplier = lb.count(item)
    sum += item * multiplier

print(sum)
