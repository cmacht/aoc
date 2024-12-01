with open("input") as input:
    lines = input.readlines()
    lines = [line.strip() for line in lines]

cards = dict()

for idx in range(len(lines)):
    cards[idx] = 1

for idx, line in enumerate(lines):
    have, winning = line.split(':')[1].split('|')

    have = [int(num) for num in have.split()]
    have = set(have)
    winning = [int(num) for num in winning.split()]
    winning = set(winning)

    multiplier = cards[idx]
    current_winners = len(winning.intersection(have))
    for _ in range(multiplier):
        for add_id in range(1, current_winners + 1):
            new_idx = idx + add_id
            cards[new_idx] += 1


print(cards)

print(sum(cards.values()))

