# The Elf would first like to know which games would have been possible if the bag contained
# only 12 red cubes, 13 green cubes, and 14 blue cubes?

with open("input") as input:
    lines = input.readlines()
    lines = [line.strip() for line in lines]

games = dict()
for idx, line in enumerate(lines, 1):
    games[idx] = line.split(':')[1]

for game_id, rounds in games.items():
    games[game_id] = rounds.split(';')

for game_id, rounds in games.items():
    games[game_id] = []
    for idx, round in enumerate(rounds):
        games[game_id].append({})
        for pick in round.split(','):
            color = pick.split()[1]
            amount = int(pick.split()[0])
            games[game_id][idx].update({color: amount})

print(games)

RED = 12
GREEN = 13
BLUE = 14

sum = 0

for game_id, game in games.items():
    power = {'red': 0, 'green': 0, 'blue': 0}
    for round in game:
        get_red = round.get('red', 0)
        if round.get('red', 0) > power['red']:
            power['red'] = round.get('red')
        if round.get('green', 0) > power['green']:
            power['green'] = round.get('green')
        if round.get('blue', 0) > power['blue']:
            power['blue'] = round.get('blue')

    game_power = 0
    for value in power.values():
        if game_power == 0:
            game_power = value
        else:
            game_power = game_power * value

    sum += game_power

print(sum)





