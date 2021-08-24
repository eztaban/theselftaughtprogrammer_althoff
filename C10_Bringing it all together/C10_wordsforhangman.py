import random

def wordpicker():
    words = ["table",
             "car",
             "microphone",
             "water",
             "cat",
             "dog",
             "giraffe",
             "hangman",
             "hangwoman",
             "covid",
             "football",
             "quiet",
             "test",
             "winner",
             "loser",
             "horse",
             "tractor",
             "city",
             "traitor",
             "council",
             "speakerphone",
             "grammardoesnotmatter",
             "madeupword",
             "areyoufrustratedwiththisgame",
             "pencil",
             "unicorn",
             "potato",
             "potatomush",
             "boombaya",
             "munchkin",
             "madesebadel",
             "gubbi",
             "pinuchi"]
    maxw=len(words)-1
    idx=random.randint(0,maxw)
    picked_word = words[idx]
    return picked_word
