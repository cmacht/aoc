with open("input") as f:
    grid = f.read().splitlines()

for line in grid:
    print(line)

ol = ['up', 'right','down', 'left']
o = 'up'
r = 0
c = 0
ans = 0
pset = set()

for idx, line in enumerate(grid):
    if '^' in line:
        r, c = idx, line.index('^')
        o = 'up'

def is_obstacle(r, c):
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
    print(pset)
    print('---------')

# while 0 <= r < len(grid) and 0 <= c < len(grid[0]): # while in grid
while True:
    try:
        if o == 'up':
            if is_obstacle(r-1, c):
                o = turn_right()
            else:
                r -= 1
        elif o == 'right':
            if is_obstacle(r, c+1):
                o = turn_right()
            else:
                c += 1
        elif o == 'down':
            if is_obstacle(r+1, c):
                o = turn_right()
            else:
                r += 1
        elif o == 'left':
            if is_obstacle(r, c-1):
                o = turn_right()
            else:
                c -= 1

        pset.add((r,c))
        # show_map()

    except IndexError:
        break

print(len(pset))





