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
    print(item)
    multiplier = lb.count(item)
    print(multiplier)
    sum += item * multiplier

print(la)
print(lb)
print(sum)
