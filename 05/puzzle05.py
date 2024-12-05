with open("input-training") as f:
    nums = f.read().splitlines()

n = False
rules = dict()
updates = []
for num in nums:
    if num == "":
        n = True
        continue
    if not n:
        a, b = num.split("|")
        a, b = int(a), int(b)
        if not rules.get(a):
            rules[a] = set()
        rules[a].add(b)
    else:
        updates.append(list(map(int, num.split(","))))

print(rules)
print(updates)

ans = 0

for update in updates:
    print("---------------------")
    print("running:", update)
    try:
        for u in update:
            vset = rules.get(u)
            if vset is None: continue
            for v in vset:
                if v not in update: continue
                if not update.index(u) < update.index(v):
                    print(u, '|', v)
                    raise(UserWarning('Update not in right order'))
    except UserWarning as e :
        print(e)
        continue
    middle_idx = (len(update) - 1) // 2
    print(update[middle_idx], "<==", update)
    ans += update[middle_idx]

print(ans)

