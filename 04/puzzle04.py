import itertools
import re

with open("input-training") as f:
    grid = f.read().splitlines()

print(grid)
ans = 0


def search_vert(lines):
    transposed = list(map(list, itertools.zip_longest(*lines, fillvalue=None)))
    return search_hori(["".join(line) for line in transposed])

def search_hori(lines):
    for line in lines:
        print(line)
    print('-------')
    hits = 0
    for line in lines:
        hits += len([x.start() for x in re.finditer('XMAS', line)])
        line_backwards = line[::-1]
        hits += len([x.start() for x in re.finditer('XMAS', line_backwards)])
    return hits

def search_diag(lines):
    



ans += search_hori(grid)
print(ans)
ans += search_vert(grid)
print(ans)
