with open("input") as f:
    line = f.readline().strip()

fid = 0
disk = []
blocks = 0
for i, n in enumerate(line):
    if i % 2 == 0:
        if fid == 0:
            starter = [fid] * int(n)
            fid += 1
        else:
            disk.extend([fid] * int(n))
            fid += 1
            blocks += 1 * int(n)
    else:
        disk.extend([0] * int(n))

print(starter)
print(disk)
blocks = fid - 1

def find_block_right(disk, target):
    target = [target]
    for i in reversed(range(len(disk))):
        if disk[i] == target[0]: target.append(i)
        if disk[i] == 0 and len(target) > 1: break
    return target

def find_space_left(disk, space, max):
    s = 0
    for i in range(max):
        if disk[i] == 0:
            s += 1
            if s == space: return i + 1 - space
        else:
            s = 0

for fid in reversed(range(1, max(disk) + 1)):
    t = find_block_right(disk, fid)
    s = find_space_left(disk, len(t)-1, t[-1])
    if s is None: continue
    for w in range(s, s+len(t)-1): disk[w] = fid
    for x in t[1:]: disk[x] = 0

print(disk)

ans = 0
disk = starter + disk
for i in range(len(disk)):
    ans += disk[i] * i
print(ans)
