from itertools import combinations

with open("input") as input:
	lines = input.readlines()
	lines = [line.strip() for line in lines]
	field = []
	for line in lines:
		field.append([c for c in line])

ans = 0

# PREPARE EXPANSION
double_rows = []
for idx, line in enumerate(field):
	if all(c == '.' for c in line):
		double_rows.append(idx)
double_cols = []
for idx in range(len(field[0])):
	broke = False
	for jdx in range(len(field)):
		if field[jdx][idx] != '.':
			broke = True
			break
	if not broke:
		double_cols.append(idx)

# NAME GALAXIES
galaxy_id = 0
galaxies = []
for idx, line in enumerate(field):
	for jdx, char in enumerate(line):
		if char == '#':
			field[idx][jdx] = galaxy_id
			galaxies.append((idx, jdx))
			galaxy_id += 1  # account for exclusive range below

for g1, g2 in combinations(galaxies, 2):
	# print(g1, '=>', g2)
	path = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
	ans += path
	for d in double_rows:
		coords = sorted((g1[0], g2[0]))
		if d in range(coords[0]+1, coords[1]):
			ans += 999_999
	for d in double_cols:
		coords = sorted((g1[1], g2[1]))
		if d in range(coords[0]+1, coords[1]):
			ans += 999_999

print(ans)


