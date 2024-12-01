from collections import deque

with open("input.txt") as input:
    lines = input.readlines()
    lines = [line.strip() for line in lines]

print(lines)
valid_digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
valid_digits_reverse = {'eno': 1, 'owt': 2, 'eerht': 3, 'ruof': 4, 'evif': 5, 'xis': 6, 'neves': 7, 'thgie': 8, 'enin': 9}
sum = 0


def has_digit(blob):
    for word, digit in valid_digits.items():
        if word in blob:
            return digit
    return 0

def has_reverse_digit(blob):
    for word, digit in valid_digits_reverse.items():
        if word in blob:
            return digit
    return 0


def find_left(line):
    word = ''
    for char in line:
        try:
            int(char)
            return char
        except ValueError:
            word += char
            if digit := has_digit(word):
                return str(digit)


def find_right(line):
    word = ''
    for char in reversed(line):
        try:
            int(char)
            return char
        except ValueError:
            word += char
            if digit := has_reverse_digit(word):
                return str(digit)


for line in lines:
    left = find_left(line)
    right = find_right(line)
    result = int(f'{left}{right}')

    sum += result

print('sum total', sum)