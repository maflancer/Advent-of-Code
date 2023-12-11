cards = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


def getType(hand):
    highest_type = -1

    test_hand = hand.replace("J", "")
    if len(test_hand) <= 1:
        return 6
    elif len(test_hand) == 2 and test_hand[0] == test_hand[1]:
        return 6
    elif len(test_hand) == 2 and test_hand[0] != test_hand[1]:
        return 5

    unique_cards = set(hand.replace("J", ""))
    for card in unique_cards:
        new_hand = hand.replace("J", card)
        pairs = set()
        for card in new_hand:
            num_cards = new_hand.count(card)
            if num_cards == 5:
                return 6
            elif num_cards == 4 and 5 > highest_type:
                highest_type = 5
            elif (
                num_cards == 3
                and new_hand.replace(card, "")[0]
                == new_hand.replace(card, "")[1]
                and 4 > highest_type
            ):
                highest_type = 4
            elif num_cards == 3 and 3 > highest_type:
                highest_type = 3
            elif num_cards == 2:
                pairs.add(card)

    return len(pairs) if highest_type == -1 else highest_type


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
