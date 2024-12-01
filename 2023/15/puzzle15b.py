import math
from collections import OrderedDict
from itertools import combinations

with open("input") as input:
	lines = input.readlines()
	lines = [line.strip() for line in lines]

line = lines[0]
ins = line.split(',')
boxes = {}

ans = 0

def calc_hash(label):
	hashsum = 0
	for c in label:
		hashsum += ord(c)
		hashsum = (hashsum * 17) % 256
	return hashsum


for instr in ins:
	if '=' in instr:
		op_set = True
		label, focal = instr.split('=')
		box_id = calc_hash(label)
	else:  # '-' in instr:
		op_set = False
		label, _ = instr.split('-')
		box_id = calc_hash(label)

	if boxes.get(box_id):
		if op_set:
			boxes[box_id].update({label: focal})
		else:
			# remove if exists
			boxes[box_id].pop(label, None)

	else:
		if op_set:
			boxes.update({box_id: {label: focal}})

	print(boxes)

for box_id, box in boxes.items():
	print(box_id)
	fac1 = box_id + 1
	for idx, (label, focal) in enumerate(box.items(), 1):
		fac2 = idx
		ans += fac1 * fac2 * int(focal)

print(ans)