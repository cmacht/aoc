import math
from itertools import combinations

with open("input-training") as input:
	lines = input.readlines()
	lines = [line.strip() for line in lines]
	field = []
	for line in lines:
		field.append([c for c in line])

ans = 0

# EXPAND
double_row = []
for idx, line in enumerate(field):
	if all(c == '.' for c in line):
		double_row.append(idx)
double_col = []
for idx in range(len(field[0])):
	broke = False
	for jdx in range(len(field)):
		if field[jdx][idx] != '.':
			broke = True
			break
	if not broke:
		double_col.append(idx)

# for add, row in enumerate(double_row):
# 	field.insert(row+add, field[row+add][:])
# for add, col in enumerate(double_col):
# 	for idx in range(12):
# 		field[idx].insert(col+add, '.')

# NAME GALAXIES
galaxy_count = 0
galaxies = []
for idx, line in enumerate(field):
	for jdx, char in enumerate(line):
		if char == '#':
			field[idx][jdx] = galaxy_count
			galaxies.append((idx, jdx))
			galaxy_count += 1  # too much to account for exclusive range below

for line in field:
	line = [str(x) for x in line]
	print(''.join(line))
	pass

print('double_row', double_row)
print('double_col', double_col)
for g1, g2 in combinations(galaxies, 2):
	print(g1, '=>', g2)
	path = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
	ans += path
	print(path, '/', ans)
	for d in double_row:
		if d in range(g1[0]+1, g2[0]):
			print('+1 double row', d)
			ans += 1
	for d in double_col:
		if d in range(g1[1]+1, g2[1]):
			print('+1 double col', d)
			ans += 1

print(ans)


