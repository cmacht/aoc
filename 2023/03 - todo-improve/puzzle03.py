with open("input") as input:
    lines = input.readlines()
    lines = [line.strip() for line in lines]

width = len(lines)
heigth = len(lines[0])
nums = []
syms = []
sum = 0

for posy, line in enumerate(lines):
    ctdigit = False
    for posx, char in enumerate(line):
        if char.isdigit():
            if ctdigit:
                d = nums.pop()
                d[0] += char
                nums.append(d)
                continue
            nums.append([char, posy, posx])
            ctdigit = True
        elif char == '.':
            ctdigit = False
            continue
        else:
            syms.append((posy, posx))
            ctdigit = False

print(nums)
print(syms)

def look_around(y, x):
    for i, j in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
        if (y == 0 and i == -1) or (y == heigth - 1 and i == 1):
            continue
        if (x == 0 and j == -1) or (x == width - 1 and j == 1):
            continue
        sy = y + i
        sx = x + j
        if lines[sy][sx].isdigit() or lines[sy][sx] == '.':
            continue
        else:
            return True
    return False


for num in nums:
    this_num = num[0]
    posy, posx = num[1], num[2]
    next = False
    for addx in range(len(this_num)):
        if look_around(posy, posx + addx):
            next = True
            break
    if next:
        sum += int(this_num)
        continue

print(sum)



