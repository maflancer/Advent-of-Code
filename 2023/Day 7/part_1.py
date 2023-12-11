cards = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def getType(hand):
    pairs = set()
    for card in hand:
        num_cards = hand.count(card)
        if num_cards == 5:
            return 6
        elif num_cards == 4:
            return 5
        elif (
            num_cards == 3
            and hand.replace(card, "")[0] == hand.replace(card, "")[1]
        ):
            return 4
        elif num_cards == 3:
            return 3
        elif num_cards == 2:
            pairs.add(card)

    return len(pairs)


# converts a hand from string format to a number that can be
# used to compare high cards
def handToNum(hand):
    rank = 0
    card_num = 100000000
    for card in hand:
        rank += card_num * cards[card]
        card_num /= 100
    return rank


# with open("./test.txt", "r") as f:
with open("./input.txt", "r") as f:
    type_to_hands = {i: [] for i in range(7)}

    for line in f.readlines():
        hand = line.split(" ")[0]
        bet = line.split(" ")[1].strip()

        type_to_hands[getType(hand)].append(
            {"bet": bet, "hand": handToNum(hand)}
        )

    rank = 1
    total_winnings = 0
    for type, hands in type_to_hands.items():
        sorted_hands = sorted(hands, key=lambda hand: hand["hand"])

        for hand in sorted_hands:
            total_winnings += int(hand["bet"]) * rank
            rank += 1

    print(f"The total winnings are ${total_winnings}")
