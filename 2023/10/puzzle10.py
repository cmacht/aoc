with open("input") as input:
	lines = input.readlines()
	lines = [line.strip() for line in lines]
	field = []
	for idx, line in enumerate(lines):
		field.append([c for c in line])
		if 'S' in line:
			START_Y = idx
			START_X = line.index('S')

lookup = {
	".": [],
	"S": [],
	"|": [(-1, 0), (1, 0)],
	"-": [(0, -1), (0, 1)],
	"L": [(-1, 0), (0, 1)],
	"J": [(-1, 0), (0, -1)],
	"F": [(1, 0), (0, 1)],
	"7": [(1, 0), (0, -1)]
}


def next_goto(pos_y, pos_x, previous, field, path):
	pipe = field[pos_y][pos_x]
	if pipe == "S":
		print("winning")
		return 0, 0, (0, 0)
	field[pos_y][pos_x] = "X"
	path.append((pipe, pos_y, pos_x))

	gotos = lookup[pipe]
	for goto in gotos:
		if goto == previous:
			continue
		y, x = goto
		new_y = pos_y + y
		new_x = pos_x + x
		opposite = get_opposite(y, x)
		return new_y, new_x, opposite


def find_first(pos_y, pos_x, field, path):
	for y, x in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
		new_y = pos_y + y
		new_x = pos_x + x
		if new_y < 0 or new_y >= len(field) or new_x < 0 or new_x >= len(field):
			continue
		neighbor = field[new_y][new_x]
		if get_opposite(y, x) in lookup[neighbor]:
			opposite = get_opposite(y, x)
			return new_y, new_x, opposite
	print("WTF", previous, new_y+1, new_x+1)


def get_opposite(y, x):
	match (y, x):
		case (-1, 0):
			return 1, 0
		case (0, 1):
			return 0, -1
		case (1, 0):
			return -1, 0
		case (0, -1):
			return 0, 1


path = []
y, x, previous = find_first(START_Y, START_X, field, path)
while not (y == 0 and x == 0):
	y, x, previous = next_goto(y, x, previous, field, path)
	# print(previous, y, x)

print(path)
print(len(path))


