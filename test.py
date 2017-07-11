points = 0
total_points = 0
while len(hand) > 0:
    print('Current Hand: ', end='')
    displayHand(hand)
    word = input ("Enter word, or a '.' to indicate that you are finished: ")
    if word == '.':
        print ("Goodbye! Total score: %d  points." % total_points)
        break
    elif isValidWord(word, hand, wordList) == True :
        points = getWordScore(word, n)
        total_points += points
        print ('" %s "' " earned %d points. Total: %d points " % (word, points, total_points))
        print ()
        if len(hand) == len(word):
            print ("Run out of letters. Total score:  %d  points." % total_points)
            break
        else:
            hand = updateHand(hand, word)

    else:
        print ("Invalid word, please try again.\n")
