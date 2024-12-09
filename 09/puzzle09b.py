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

print(disk)
print(starter)
fid = max(disk)
print(f'{fid=}')
print(len(disk))
print(blocks)


def find_gap_left(flen, limit):
    glen = 0
    for k in range(limit):
        if disk[k] == 0:
            glen += 1
        else:
            glen = 0
        if glen >= flen:
            return k - glen + 1
    return None

l = 0
flen = 0
for r in reversed(range(len(disk))):
    if flen > 0 and disk[r] != fid:
        idx = find_gap_left(flen, r)
        if idx is not None:
            for m in range(flen):
                disk[idx + m] = fid
                disk[r + 1 + m] = 0
        fid -= 1
        flen = 0
        # print(f'{flen=}', r)
        # print(f'{idx=}')
    if disk[r] == fid:
        flen += 1

disk = starter + disk
print(disk)
ans = 0
for i, e in enumerate(disk):
    ans += i * e
print(ans)

