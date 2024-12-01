import math
from itertools import combinations

with open("input") as input:
	lines = input.readlines()
	lines = [line.strip() for line in lines]

fields = []
new = False
new_field = []
for line in lines:
	if line.strip() == '':
		fields.append(new_field)
		new_field = []
		continue
	new_field.append(line)
# print(fields)

def rotate_right(field):
	vert = []
	for idx, line in enumerate(reversed(field)):
		for idy, char in enumerate(line):
			if len(vert) == idy:
				vert.append(char)
				continue
			vert[idy] += char
	return vert

def search_field(field):
	for idx, line in enumerate(field):
		if idx == len(field)-1:
			break  # break after max index
		if line == field[idx+1]:
			if is_fully_reflected(field, idx):
				return idx+1 #lines above
	return 0


def search_horizontal(field):
	above = search_field(field)
	return above*100

def search_vertical(field):
	field = rotate_right(field)
	above = search_field(field)
	return above


def is_fully_reflected(field, idx, factor=1, is_fully=False):
	#search outwards
	if idx-factor < 0 or idx+1+factor > len(field)-1:
		return True
	if field[idx-factor] == field[idx+1+factor]:
		factor += 1
		is_fully = is_fully_reflected(field, idx, factor, is_fully)
		return is_fully
	else:
		return False



ans = 0
for count, field in enumerate(fields):
	print('field', count, ':')
	hori = search_horizontal(field)
	verti = search_vertical(field)
	print(hori)
	print(verti)
	ans += hori + verti

print(ans)

