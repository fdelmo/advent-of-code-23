from enum import Enum

with open("day7/data/input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

rounds = {hand: int(bid) for hand, bid in (line.split(" ") for line in data)}


class HandType(Enum):
    """
    Ranks of hand types
    """

    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    TREE_OF_A_KIND = 4
    TWO_PAIR = 3
    PAIR = 2
    HIGH_CARD = 1


class SymbolCard(Enum):
    """
    Ranks of individual symbolic cards
    """

    T = 10
    J = 11
    Q = 12
    K = 13
    A = 14

    def __int__(self):
        return self.value


def get_hand_type(hand: str) -> HandType:
    """
    Get the type of hand. (we could use the Counter class from the
    collection library, but I am basically coding the algorithm here
    explicitely just because.)
    """
    counter = {}
    for ch in hand:
        try:
            counter[ch] += 1
        except KeyError:
            counter[ch] = 1

    counts = list(counter.values())

    if len(counts) == 1:
        return HandType.FIVE_OF_A_KIND
    if len(counts) == 5:
        return HandType.HIGH_CARD
    if len(counts) == 4:
        return HandType.PAIR
    if len(counts) == 3:
        if 3 in counts:
            return HandType.TREE_OF_A_KIND
        return HandType.TWO_PAIR
    if 4 in counts:
        return HandType.FOUR_OF_A_KIND
    return HandType.FULL_HOUSE


def lhand_is_greater(
    lhand: str, rhand: str, lhand_type: HandType | None = None
) -> bool:
    """
    Compares two hands and returns True if the left hand is greater
    than the right hand. Otherwise, return False. If lhand_type is passed we used
    this to speed up the process.
    """
    rhand_type = get_hand_type(rhand)
    if lhand_type is None:
        lhand_type = get_hand_type(lhand)

    if lhand_type.value == rhand_type.value:
        for i, ch in enumerate(lhand):
            try:
                lval = int(ch)
            except:
                lval = int(SymbolCard[ch])

            rchar = rhand[i]
            try:
                rval = int(rchar)
            except:
                rval = int(SymbolCard[rchar])

            if lval == rval:
                continue

            return lval > rval

        return False  # if both hands are equal

    return lhand_type.value > rhand_type.value


ordered_hands = []
for hand in rounds:
    if len(ordered_hands) == 0:
        ordered_hands.append(hand)
        continue

    for i, comparison in enumerate(ordered_hands):
        if lhand_is_greater(hand, comparison):
            ordered_hands.insert(i, hand)
            break

        if i == (len(ordered_hands) - 1):
            ordered_hands.append(hand)
            break


total_winnings = 0
for i, hand in enumerate(reversed(ordered_hands)):
    rank = i + 1
    bid = rounds[hand]
    total_winnings += rank * bid

print(total_winnings)
