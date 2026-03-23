def value_of_card(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    val1 = value_of_card(card_one)
    val2 = value_of_card(card_two)

    if val1 > val2:
        return card_one
    elif val2 > val1:
        return card_two
    else:
        return (card_one, card_two)


def value_of_ace(card_one, card_two):
    # Convert cards to values (Ace = 11 if already present)
    def card_value(card):
        if card in ['J', 'Q', 'K']:
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)

    total = card_value(card_one) + card_value(card_two)

    # If taking Ace as 11 doesn't bust (>21), use 11 else 1
    if total + 11 <= 21:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    # Blackjack = Ace (11) + 10-value card
    cards = [card_one, card_two]

    return (
        ('A' in cards) and
        any(card in ['10', 'J', 'Q', 'K'] for card in cards)
    )


def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in [9, 10, 11]