with open("input") as f:
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

def sort_list(nums):
    sl = nums[:]
    for a in nums:
        sl.remove(a)
        bset = rules.get(a)
        if bset is None:
            sl.append(a)
            continue
        smallest = []
        for b in bset:
            if b in sl:
                smallest.append(sl.index(b))
        if not smallest:
            sl.append(a)
        else:
            sl.insert(min(smallest), a)
    return sl

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
                    raise(UserWarning('Update not in right order'))
    except UserWarning as e :
        update = sort_list(update)
        print(update)
        middle_idx = (len(update) - 1) // 2
        print(update[middle_idx], "<==", update)
        ans += update[middle_idx]


print(ans)

