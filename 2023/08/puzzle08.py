
with open("input-training3") as input:
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

finished = False
steps = 0
o = 'AAA'
while not finished:
    for i in instructions:
        if i == 'R':
            o = graph[o]['rdest']
        else:
            o = graph[o]['ldest']
        steps += 1
        if o == 'ZZZ':
            finished = True
            break

print(steps)


