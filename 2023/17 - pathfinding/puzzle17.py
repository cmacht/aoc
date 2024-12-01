import heapq
from collections import deque

with open("input-training") as input:
	lines = input.readlines()
	lines = [line.strip() for line in lines]

map_width = len(lines[0])
map_height = len(lines)

class Queue:
	def __init__(self):
		self.elements = deque()

	def empty(self):
		return not self.elements

	def put(self, x):
		self.elements.append(x)

	def get(self):
		return self.elements.popleft()


class PriorityQueue:
	def __init__(self):
		self.elements = []

	def empty(self):
		return not self.elements

	def put(self, item, priority):
		heapq.heappush(self.elements, (priority, item))

	def get(self):
		return heapq.heappop(self.elements)[1]


class GridWithWeights():
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.weights = {}

	def in_bounds(self, id):
		x, y = id
		return 0 <= x < self.width and 0 <= y < self.height

	def filter_blocker(self, id, blocker):
		if id == blocker:
			return False
		return True

	def neighbors(self, id, blocker):
		x, y = id
		blocker = (blocker[0] + x, blocker[1] + y)
		neighbors = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]
		if (x + y) % 2 == 0:
			neighbors.reverse()
		result = filter(lambda seq: self.filter_blocker(seq, blocker), neighbors)
		result = filter(self.in_bounds, result)
		return result

	def cost(self, from_node, to_node):
		return self.weights.get(to_node, 1)


def block_fourth(current, came_from):
	# if last_three_in_same_direction
	last_1 = came_from.get(current)
	last_2 = came_from.get(last_1)
	if any(l is None for l in [last_1, last_2]):
		return (0, 0)
	if current[0] == last_1[0] == last_2[0]:
		return (0, 1)
	elif current[1] == last_1[1] == last_2[1]:
		return (1, 0)
	return (0, 0)


def dijkstra_search(graph, start, goal):
	frontier = PriorityQueue()
	frontier.put(start, 0)
	came_from = {}
	cost_so_far = {}
	came_from[start] = None
	cost_so_far[start] = 0

	while not frontier.empty():
		current = frontier.get()

		if current == goal:
			break

		blocker = block_fourth(current, came_from)

		for next in graph.neighbors(current, blocker):
			new_cost = cost_so_far[current] + graph.cost(current, next)
			if next not in cost_so_far or new_cost < cost_so_far[next]:
				cost_so_far[next] = new_cost
				priority = new_cost
				frontier.put(next, priority)
				came_from[next] = current

	return came_from, cost_so_far


def reconstruct_path(came_from, start, goal):
	current = goal
	path = []
	if goal not in came_from:  # no path was found
		return []
	while current != start:
		path.append(current)
		current = came_from[current]
	path.append(start)  # optional
	path.reverse()  # optional
	return path


map = GridWithWeights(map_width, map_height)
weights = {}
for idx, line in enumerate(lines):
	for jdx, w in enumerate(line):
		weights[(idx, jdx)] = int(w)
map.weights = weights
start = (0, 0)
goal = (map_width - 1, map_height - 1)
came_from, cost_so_far = dijkstra_search(map, start, goal)
print(f'{came_from=}')
print(f'{cost_so_far=}')

path = reconstruct_path(came_from, start, goal)
print(f'{path=}')


def draw_grid(cost, width, height):
	base = [[] for y in range(height)]
	for y in range(height):
		for x in range(width):
			base[y].append(str(cost.get((y, x), 0)))
	for row in base:
		print(' '.join(row))
	print()

for line in lines:
	print(line)
print()


for y, line in enumerate(lines):
	printl = [l for l in line]
	print(' '.join(printl))
print()


for y, line in enumerate(lines):
	printl = [l for l in line]
	for x, char in enumerate(line):
		if (y, x) in path:
			printl[x] = '.'
	print(' '.join(printl))

print(cost_so_far[(map_width-1, map_height-1)])
# draw_grid(cost_so_far, map_width, map_height)


