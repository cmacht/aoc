from itertools import tee

with open("input") as input:
    lines = input.readlines()
    lines = [line.strip() for line in lines]
    history = []
    for line in lines:
        history.append([int(n) for n in line.split()])

def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ...
    """
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def create_subarray(array, result=None):
    if result is None:
        result = [array]
    pairs = pairwise(array)
    subarray = [(b - a) for a, b in pairs]
    if sum(subarray) == 0 and subarray[-1] == 0:
        result.append(subarray)
    else:
        result.append(subarray)
        create_subarray(subarray, result)
    return result


sums = []
for line in history:
    subarray = create_subarray(line)
    add = 0
    for arr in subarray[::-1]:
        new = arr[-1] + add
        add = new
        arr.append(new)
    sums.append(subarray[0][-1])
    print(subarray)
    # print(subarray[0][-1])

print(sums)
print(sum(sums))



