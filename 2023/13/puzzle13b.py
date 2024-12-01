import difflib
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
			passed, error = is_fully_reflected(field, idx)
			if passed and error == 1:
				return idx+1 #lines above
		else:
			error = 0
			for cidx, chars in enumerate(zip(line, field[idx+1])):
				if chars[0] != chars[1]:
					error += 1
			if error == 1:
				passed, error = is_fully_reflected(field, idx, error=1)
				if passed and error == 1:
					return idx+1
	return 0


def search_horizontal(field):
	above = search_field(field)
	return above*100

def search_vertical(field):
	field = rotate_right(field)
	above = search_field(field)
	return above


def is_fully_reflected(field, idx, factor=1, is_fully=False, error=0):
	#search outwards
	if idx-factor < 0 or idx+1+factor > len(field)-1:
		return True, error
	if field[idx-factor] == field[idx+1+factor]:
		factor += 1
		return is_fully_reflected(field, idx, factor, is_fully, error)
	elif error < 1:
		for cidx, chars in enumerate(zip(field[idx-factor], field[idx+1+factor])):
			if chars[0] != chars[1]:
				error += 1
		if error == 1:
			factor += 1
			return is_fully_reflected(field, idx, factor, is_fully, error)

	return False, error



ans = 0
for count, field in enumerate(fields):
	print('field', count, ':')
	hori = search_horizontal(field)
	verti = search_vertical(field)
	ans += hori + verti

print('ans', ans)

