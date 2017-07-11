
'''
Problem -2:

Problem Statement: https://github.com/subhsamal/Python_EDX/commit/5efe721940c8187166c3296c562df9056219d854
'''

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    new_hand = {}
    for key, value in hand.items():
        if key not in word:
            new_hand[key] = value
        elif value > word.count(key):
            new_hand[key] = value - word.count(key)
        elif value == word.count(key):
            new_hand[key] = 0
        else:
            pass

    return new_hand
