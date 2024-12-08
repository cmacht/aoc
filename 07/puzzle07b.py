from itertools import product

with open('input') as f:
    lines = [l.split(':') for l in f.read().splitlines()]

eqs = {}
for line in lines:
    eqs[int(line[0])] = [int(i) for i in line[1].split()]

ans = 0
for r, nums in eqs.items():

    combinations = product(('add', 'mul', 'concat'), repeat=len(nums)-1)
    print(r, nums)
    for c in combinations:
        t = nums[0]
        for i, o in enumerate(c):
            match o:
                case 'add': t += nums[i+1]
                case 'mul': t *= nums[i+1]
                case 'concat': t = int(str(t) + str(nums[i+1]))
        if t == r:
            ans += t
            break

print(ans)

