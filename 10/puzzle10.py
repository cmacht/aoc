import re
from collections import deque

with open("input") as f:
    grid = f.read().splitlines()

starts = []
peaks = []
ans = []
for i in range(len(grid)):
    print(grid[i])
    for hit in re.finditer('0', grid[i]):
        starts.append((i, hit.start()))
    for hit in re.finditer('9', grid[i]):
        peaks.append((i, hit.start()))

print(f'{starts=}')
print(f'{peaks=}')

def neighbours(r, c):
    for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and int(grid[nr][nc]) == (int(grid[r][c]) + 1):
            yield nr, nc

ans = 0
for s in starts:
    queue = deque([s])
    tpeaks = set()

    while queue:
        p = queue.popleft()
        for n in neighbours(*p):
            if n in peaks:
                tpeaks.add(n)
            else:
                queue.append(n)
    ans += len(tpeaks)

print(ans)



