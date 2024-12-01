import math
from itertools import combinations

with open("input") as input:
	lines = input.readlines()
	lines = [line.strip() for line in lines]

line = lines[0]
ins = line.split(',')

ans = 0

for instr in ins:
	local = 0
	for c in instr:
		local += ord(c)
		local = (local * 17) % 256
	print(local)
	ans += local

print(ans)