import C10_wordsforhangman

picked_word=C10_wordsforhangman.wordpicker()

def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    word=word.upper()
    rletters = list(word)
    wletters = list()
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages)-1:
        print("\n")
        msg = "Guess a letter: "
        print("Enter quit to exit")
        char = input(msg).upper()
        if char == "QUIT":
            break
        if char in rletters:
            cind = rletters.index(char)
            board[cind]=char
            rletters[cind]='$'
        else:
            wrong +=1
            wletters.append(char)
        print("You already tried: ", wletters)
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You win! The word was: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! The word was: {}.".format(word))



hangman(picked_word)
        
