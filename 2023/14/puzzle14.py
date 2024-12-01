import math
from itertools import combinations

with open("input_cub.txt") as input:
	lines = input.readlines()
	lines = [line.strip() for line in lines]


def print_grid(grid):
	for line in grid:
		print(' '.join(line))
	print()


def roll_rocks(field):
	for ldx, line in enumerate(field):
		empty = 0
		for idx, char in enumerate(line):
			if char == '.':
				empty += 1
			elif char == '#':
				empty = 0
			elif char == 'O':
				field[ldx][idx] = '.'
				field[ldx][idx-empty] = 'O'


def rotate_right(field):
	"""North is now right"""
	return [list(a) for a in zip(*reversed(field))]


def rotate_left(field):
	"""North is now left"""
	field = [reversed(line) for line in field]
	return [list(a) for a in zip(*field)]


def sum_up(field):
	ans = 0
	for line in field:
		for idx, char in enumerate(reversed(line), 1):
			if char == 'O':
				ans += idx
	print(ans)

def make_hash(grid):
	b = ''.join([''.join(row) for row in grid])
	return hash(b)


def rotation_cycle(grid_north):
	"""Rotate and Roll North, West, South, East
	Expects Input North"""
	roll_rocks(grid_north)
	grid_west = rotate_right(grid_north)
	roll_rocks(grid_west)
	grid_south = rotate_right(grid_west)
	roll_rocks(grid_south)
	grid_east = rotate_right(grid_south)
	roll_rocks(grid_east)
	grid_north = rotate_right(grid_east)
	return grid_north


hashmap = {}
gridmap = {}
grid_north = rotate_left(lines)
# North is now to the left

for r in range(1_000_000):
	key = make_hash(grid_north)
	if hashmap.get(key):
		grid_north = gridmap[key]
	else:
		for u in range(1000):
			grid_north = rotation_cycle(grid_north)
		gridmap[key] = grid_north
		value = make_hash(grid_north)
		hashmap[key] = value
	if r % 1_000 == 0:
		print('rotation', r, 'x1000')
print(len(hashmap))
sum_up(grid_north)

