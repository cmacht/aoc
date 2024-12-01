with open("input") as input:
    lines = input.readlines()
    lines = [line.strip() for line in lines]


times = lines.pop(0).split(":")[1]
times = times.split()
distances = lines.pop(0).split(":")[1]
distances = distances.split()

records = [(int(t), int(d)) for t, d in zip(times, distances)]

print(records)
results = [[] for _ in range(len(records))]

for idx, (time, record) in enumerate(records):
    for charge in range(time + 1):
        run = time - charge
        if run * charge > record:
            results[idx].append(charge)

print(results)
for result in results:

    print(len(result))








