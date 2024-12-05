import itertools
import re

with open("input") as f:
    grid = f.read().splitlines()

print(grid)
ans = 0

for r in range(len(grid)):
    for c in range(len(grid[0])):
        print(r, c)
        if grid[r][c] != "X": continue
        for dr, dc in [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]:
            if not (0 <= r + 3 * dr < len(grid) and 0 <= c + 3 * dc < len(grid[0])): continue
            if grid[r + dr][c + dc] == "M" and grid[r + 2 * dr][c + 2 * dc] == "A" and grid[r + 3 * dr][c + 3 * dc] == "S":
                ans += 1



print(ans)
