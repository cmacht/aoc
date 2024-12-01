from math import lcm

with open("input") as input:
    lines = input.readlines()
    instructions = lines.pop(0).strip()
    lines.pop(0)
    lines = [line.strip() for line in lines]

print(instructions)

graph = {}
for line in lines:
    origin, dest = line.split('=')
    ldest, rdest = dest.split(',')
    dests = {'ldest': ldest.strip(' ()'), 'rdest': rdest.strip(' ()')}
    graph.update({origin.strip(): dests})
print(graph)

origins = [k for k in graph.keys() if k[2] == 'A']
print(origins)
destinations = [k for k in graph.keys() if k[2] == 'Z']
print(destinations)

total_steps = []
for o in origins:
    steps = 0
    finished = False
    while not finished:
        for count, choose in enumerate(instructions, 1):
            if choose == 'R':
                o = graph[o]['rdest']
            else:
                o = graph[o]['ldest']
            if o.endswith('Z'):
                finished = True
                steps += count
                break
        if not finished:
            steps += len(instructions)
    total_steps.append(steps)

test = lcm(*total_steps)
print(test)


