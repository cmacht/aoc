with open("input") as f:
    grid = list(map(list, f.read().splitlines()))

rows = len(grid)
cols = len(grid[0])

for idx, line in enumerate(grid):
    if '^' in line:
        r, c = idx, line.index('^')

def loops(grid, r, c):
    dr = -1
    dc = 0
    pset = set()
    while True:
        pset.add((r, c, dr, dc))
        if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols: return False
        if grid[r + dr][c + dc] == "#":
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc
        if (r, c, dr, dc) in pset:
            return True

blocks = 0

for cr in range(rows):
    for cc in range(cols):
        if grid[cr][cc] != ".": continue
        grid[cr][cc] = "#"
        if loops(grid, r, c):
            blocks += 1
        grid[cr][cc] = "."

print(blocks)





