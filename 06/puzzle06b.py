from unittest import case

with open("input") as f:
    grid = f.read().splitlines()

for line in grid:
    print(line)
print()

ol = ['up', 'right','down', 'left']
o = 'up'
r = 0
c = 0
ans = 0
pset = set()
verts = set()
blocks = set()
just_turned = False

for idx, line in enumerate(grid):
    if '^' in line:
        r, c = idx, line.index('^')
        pset.add((r,c))
        o = 'up'

def is_obstacle(r, c):
    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
        if grid[r][c] == '#':
            return True

def turn_right():
    idx = ol.index(o)
    if idx < len(ol) - 1:
        return ol[idx+1]
    else:
        return ol[0]

def show_map():
    for idx, line in enumerate(grid):
        if idx == r:
            line = line[:c] + 'o' + line[c+1:]
        print(line)
    print(len(pset))
    print('---------')


def show_verts_and_blocks():
    for r, line in enumerate(grid):
        for c, _ in enumerate(line):
            if (r, c) in verts:
                line = line[:c] + '+' + line[c+1:]
            if (r, c) in blocks:
                line = line[:c] + 'O' + line[c+1:]
        print(line)

def shoot_right(orientation):
    """ Scan at 90deg for a vertex. If found, you can rejoin the path there and have a loop!
    """
    assert orientation in ['up', 'right', 'down', 'left']
    match orientation:
        case 'up':
            d = (0, 1)
            b = (-1, 0)
            limit = len(grid[0]) - c
        case 'right':
            d = (1, 0)
            b = (0, 1)
            limit = len(grid) - r
        case 'down':
            d = (0, -1)
            b = (1, 0)
            limit = c + 1
        case 'left':
            d = (-1, 0)
            b = (0, -1)
            limit = r + 1

    for i in range(1, limit):
        sr = r + d[0] * i
        sc = c + d[1] * i
        shot = grid[sr][sc]
        if shot == '#': return False
        if (r+b[0], c+b[1]) in blocks: return False
        if (sr, sc) in verts: return True

while 0 <= r < len(grid) and 0 <= c < len(grid[0]): # while in grid
    if o == 'up':
        if is_obstacle(r-1, c):
            o = turn_right()
            just_turned = True
            verts.add((r, c))
        elif shoot_right(o) and not just_turned:
            blocks.add((r-1, c))
        else:
            just_turned = False
            r -= 1
    elif o == 'right':
        if is_obstacle(r, c+1):
            o = turn_right()
            just_turned = True
            verts.add((r, c))
        elif shoot_right(o) and not just_turned:
            blocks.add((r, c+1))
        else:
            just_turned = False
            c += 1
    elif o == 'down':
        if is_obstacle(r+1, c):
            o = turn_right()
            just_turned = True
            verts.add((r, c))
        elif shoot_right(o) and not just_turned:
            blocks.add((r+1, c))
        else:
            just_turned = False
            r += 1
    elif o == 'left':
        if is_obstacle(r, c-1):
            o = turn_right()
            just_turned = True
            verts.add((r, c))
        elif shoot_right(o) and not just_turned:
            blocks.add((r, c-1))
        else:
            just_turned = False
            c -= 1


# show_verts_and_blocks()
print(len(pset))
print(f'{verts=}')
print(len(blocks))








