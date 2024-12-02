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
for a, b in zip(la, lb):
    diff = abs(b - a)
    sum += diff

print(sum)
