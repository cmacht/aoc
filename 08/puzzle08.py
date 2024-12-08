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
        if 0 <= a[0] + v[0] < len(lines) and 0 <= a[1] + v[1] < len(lines[0]):
            an = (a[0] + v[0], a[1] + v[1])
            # print('add top:', an)
            antinodes.add(an)
        if 0 <= b[0] - v[0] < len(lines) and 0 <= b[1] - v[1] < len(lines[0]):
            an = (b[0] - v[0], b[1] - v[1])
            # print('add bot:', an)
            antinodes.add(an)

for r, line in enumerate(lines):
    for an in [a for a in antinodes if a[0] == r]:
        line = line[:an[1]] + '#' + line[an[1]:]
    print(line)

print(len(antinodes))





