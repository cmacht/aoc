with open("input") as f:
    line = f.readline().strip()

print(line)
d_id = 0
disk = []
files = 0
for i, n in enumerate(line):
    if i % 2 == 0:
        disk.extend([d_id] * int(n))
        d_id += 1
        files += 1 * int(n)
    else:
        disk.extend([''] * int(n))

print(disk)
print(len(disk))
print(files)

l = 0
for r in reversed(range(files, len(disk))):
    v = disk[r]
    if not isinstance(v, int): continue
    disk[r] = ''
    for left in range(l, files):
        if not isinstance(disk[left], int):
            l = left
            break
    disk[l] = v

ans = 0
for i in range(files):
    ans += disk[i] * i

print(ans)
