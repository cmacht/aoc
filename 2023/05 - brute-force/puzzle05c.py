with open("input") as input:
    lines = input.readlines()
    lines = [line.strip() for line in lines]

seeds = lines.pop(0).split(":")[1]
seeds = seeds.split()

new_seeds = []
for idx, seed in enumerate(seeds):
    if idx % 2 == 0:
        new_seeds.append(int(seed))
    else:
        start = new_seeds.pop()
        new_seeds.append((start, int(seed)))
seeds = new_seeds

lookup = {}
map_id = -1
for line in lines:
    if 'map' in line:
        continue
    elif not line.strip():
        map_id += 1
        lookup[map_id] = []
        continue
    else:
        nums = [int(n) for n in line.split()]
        dest, src, steps = nums[0], nums[1], nums[2]
        lookup[map_id].append({'src': src, 'dest': dest, 'steps': steps})
        # for d, s in zip(range(dest, dest+steps), range(src, src+steps)):
        #     lookup[map_id].update({s:d})

print(lookup)

def look_up_input(input, d_id):
    for r in lookup[d_id]:
        if input >= r['src'] and input < (r['src'] + r['steps']):
            diff = input - r['src']
            return r['dest'] + diff
        else:
            continue
    return input

result = 0
for idx, (start, step) in enumerate(seeds):
    print(result)
    print("seed:", idx)
    for pos in (start, start+step):
        for l_id in range(len(lookup)):
            pos = look_up_input(pos, l_id)
        if result == 0:
            result = pos
        if pos < result:
            result = pos

print("result:", result)




















