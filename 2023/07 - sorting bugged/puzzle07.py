from collections import Counter

with open("input") as input:
    lines = input.readlines()
    lines = [line.strip() for line in lines]


hands = [line.split() for line in lines]
print(hands)
LENGTH = len(hands)

def get_high_card(hand):
    for value in ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']:
        if value in hand:
            return value


hands_ranked = [[] for _ in range(7)]
for hand, bid in hands:
    counted = Counter(hand)
    max_repeat = counted.most_common(1)[0][1]
    try:
        next_repeat = counted.most_common(2)[1][1]
    except IndexError:
        next_repeat = 0
    if max_repeat == 5:
        print("5 of a kind")
        hands_ranked[0].append((hand, bid))
    elif max_repeat == 4:
        print("4 of a kind")
        hands_ranked[1].append((hand, bid))
    elif max_repeat == 3 and next_repeat == 2:
        print("full house")
        hands_ranked[2].append((hand, bid))
    elif max_repeat == 3:
        print("3 of a kind")
        hands_ranked[3].append((hand, bid))
    elif max_repeat == 2 and next_repeat == 2:
        print("two pair")
        hands_ranked[4].append((hand, bid))
    elif max_repeat == 2 and next_repeat == 1:
        print("one pair")
        hands_ranked[5].append((hand, bid))
    else:
        print("high card")
        hands_ranked[6].append((hand, bid))

print(hands_ranked)


def bubble_sort(array, SORT_ORDER):
    """https://realpython.com/sorting-algorithms-python/#the-bubble-sort-algorithm-in-python
    """
    n = len(array)
    for i in range(n):
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            found = False
            char_idx = 0
            while not found:
                a = array[j][0][char_idx]
                b = array[j+1][0][char_idx]
                if a != b:
                    found = True
                    if SORT_ORDER[a] > SORT_ORDER[b]:
                        # If the item you're looking at is greater than its
                        # adjacent value, then swap them
                        array[j], array[j + 1] = array[j + 1], array[j]

                        # Since you had to swap two elements,
                        # set the `already_sorted` flag to `False` so the
                        # algorithm doesn't finish prematurely
                        already_sorted = False

                char_idx += 1

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array


for rank in hands_ranked:
    SORT_ORDER = {'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T': 4, '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12}
    for hand, bid in rank:
        rank.sort(key=lambda val: SORT_ORDER[val[0][1]])
        bubble_sort(rank, SORT_ORDER)
    print(rank)

sum = 0
counter = 0
for rank in hands_ranked:
    for hand, bid in rank:
        print(bid, "*", (LENGTH - counter))
        sum += int(bid) * (LENGTH - counter)
        counter += 1

print(sum)




