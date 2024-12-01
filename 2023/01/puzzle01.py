

with open("input.txt") as input:
    lines = input.readlines()
    lines = [line.strip() for line in lines]

print(lines)
sum = 0

for line in lines:
    for char in line:
        try:
            int(char)
            current = char
            break
        except ValueError:
            pass

    rline = reversed(line)
    for char in rline:
        try:
            int(char)
            current = f'{current}{char}'
            break
        except ValueError:
            pass

    sum += int(current)

print("final", sum)