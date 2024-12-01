with open("input") as input:
    lines = input.readlines()
    lines = [line.strip() for line in lines]

width = len(lines)
heigth = len(lines[0])
nums = []
gears = []
sum = 0

for posy, line in enumerate(lines):
    ctdigit = False
    for posx, char in enumerate(line):
        if char.isdigit():
            if ctdigit:
                d = nums.pop()
                d[0] += char
                d[1].append((posy, posx))
                nums.append(d)
                continue
            nums.append([char, [(posy, posx)]])
            ctdigit = True
        elif char == '*':
            gears.append((posy, posx))
            ctdigit = False
        else:
            ctdigit = False

print("nums: ", nums)
print("gears: ", gears)

def gear_around(y, x):
    result = set()
    for i, j in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
        if (y == 0 and i == -1) or (y == heigth - 1 and i == 1):
            continue
        if (x == 0 and j == -1) or (x == width - 1 and j == 1):
            continue
        sy = y + i
        sx = x + j
        if lines[sy][sx].isdigit():
            result.add((sy, sx))
    return result



for gear in gears:
    factors = []
    factor_coords = set()
    factor_coords.update(gear_around(gear[0], gear[1]))
    for coord in factor_coords:
        for num in nums:
            if coord in num[1]:
                hash = 0
                for c in num[1]:
                    hash += (c[0] + c[1])
                factors.append((int(num[0]), hash))
    factors = set(factors)
    if len(factors) == 2:
        sum += (factors.pop()[0] * factors.pop()[0])
    elif len(factors) != 2:
        print("not 2: ", factors)






print(len(gears))
print(sum)



