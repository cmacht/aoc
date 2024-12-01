with open("input") as input:
    lines = input.readlines()
    lines = [line.strip() for line in lines]

sum = 0

for line in lines:
    have, winning = line.split(':')[1].split('|')

    have = [int(num) for num in have.split()]
    have = set(have)
    winning = [int(num) for num in winning.split()]
    winning = set(winning)

    inter = winning.intersection(have)
    pow = len(inter)

    if pow == 1 or pow == 0:
        sum += pow
    else:
        sum += 2 ** (pow - 1)


    print(have)
    print(winning)
    print(inter)
    print(sum)
print(sum)

