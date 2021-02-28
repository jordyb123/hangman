def hangman(word):
    wrong = 0
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print('Welcome to Hangman')
    while wrong < len(stages) - 1:
        print('\n')
        guess = input("Guess a Letter")
        if guess in rletters:
            cind = rletters.index(guess)
            board[cind] = guess
            rletters[cind] = '$'
        else:
            wrong += 1
        print((' '.join(board)))
        print('\n'.join(stages[0: wrong]))
        if '__' not in board:
              print('You Win!')
              print(' '.join(board))
              win = True
              break
    if not win:
        print('\n'.join(stages[0: wrong]))
        print('You Lose! it was {}.'.format(word))

hangman("cat")
