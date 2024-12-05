import itertools
import re

with open("input") as f:
    grid = f.read().splitlines()

print(grid)
ans = 0

for r in range(1, len(grid) - 1):
    for c in range(1, len(grid[0]) - 1):
        if grid[r][c] != "A": continue
        corners = [grid[r - 1][c - 1], grid[r - 1][c + 1], grid[r + 1][c + 1], grid[r + 1][c - 1]]
        if "".join(corners) in ["MMSS", "SMMS", "SSMM", "MSSM"]:
            ans += 1

print(ans)
