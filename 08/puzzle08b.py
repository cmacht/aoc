from itertools import pairwise, combinations

with open("input") as f:
    lines = f.read().splitlines()

antennas = {}
for r in range(len(lines)):
    for c in range(len(lines[0])):
        char = lines[r][c]
        if char.isalnum():
            if antennas.get(char):
                antennas[char].append((r, c))
            else:
                antennas[char] = [(r, c)]

print(antennas)

ans = 0
antinodes = set()
for char, positions in antennas.items():
    print('-----', char)
    for a, b in combinations(positions, 2):
        v = (a[0] - b[0], a[1] - b[1])
        print(a, b, v)

        t0, t1 = a[0], a[1]
        while 0 <= t0 < len(lines) and 0 <= t1 < len(lines[0]):
            antinodes.add((t0, t1))
            t0 += v[0]
            t1 += v[1]

        b0, b1 = b[0], b[1]
        while 0 <= b0 < len(lines) and 0 <= b1 < len(lines[0]):
            antinodes.add((b0, b1))
            b0 -= v[0]
            b1 -= v[1]

for r, line in enumerate(lines):
    for an in [a for a in antinodes if a[0] == r]:
        line = line[:an[1]] + '#' + line[an[1]:]
    print(line)

print(len(antinodes))





