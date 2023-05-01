from random import randint

def get_words(filename):
    row = []
    crimefile = open(filename, 'r')
    for line in crimefile.readlines():
        word = line[:5]
        row.append(word.upper())
    crimefile.close()
    return row


def search_words(L,word):
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] == word[j]:
                print(L[i][j] + " Green")
            elif L[i][j] in word:
                print(L[i][j] + " Yellow")
            else:
                print(L[i][j] + " Grey")
        print("__________________________")
    return 0

def gen_rand_int(size):
    return randint(0,size)

def guesser(word):
    guess = input("Enter guess: ")
    while len(guess) != 5:
        guess = input("Please enter a 5 word guess: ")
    #print(guess.upper())
    guess = guess.upper()
    for i in range(len(word)):
        #print("Current index is ")
        #print(i)
        if word[i] == guess[i]:
            print(guess[i] + " Green")
        elif guess[i] in word:
            print(guess[i] + " Yellow")
        else:
            print(guess[i] + " Grey")
    return 0

def wordle():
    words = get_words("sgb-words.txt")
    index = gen_rand_int(len(words))
    print("INDEX = " + str(index))
    word = words[index]
    guess = input("Enter guess to start wordle: ")
    while len(guess) != 5:
        guess = input("Please enter a 5 letter guess: ")
    guess = guess.upper()
    for i in range(len(word)):
        if word[i] == guess[i]:
            print(guess[i] + " Green")
        elif guess[i] in word:
            print(guess[i] + " Yellow")
        else:
            print(guess[i] + " Grey")
    while guess != word:
        guess = input("Enter another 5 letter guess: ")
        while len(guess) != 5:
            guess = input("Please enter a 5 letter guess: ")
        guess = guess.upper()
        for i in range(len(word)):
            if word[i] == guess[i]:
                print(guess[i] + " Green")
            elif guess[i] in word:
                print(guess[i] + " Yellow")
            else:
                print(guess[i] + " Grey")
    print("Your guess of " + guess + " is correct!")



def return_info(words, word, guess):
    result = []
    #guess = input("Put in first guess: ")
    print("Words chosen is " + word)
    #while len(guess) != 5:
        #guess = input("Please enter a 5 letter guess: ")
    #guess = guess.upper()
    if guess == word:
        print("Your guess of " + guess + " is correct!")
        return 0
    else:
        for i in range(len(word)):
            if word[i] == guess[i]:
                tup = (0,guess[i])
                result.append(tup)
            elif guess[i] in word:
                tup = (1,guess[i])
                result.append(tup)
            else:
                tup = (2,guess[i])
                result.append(tup)
    return result

def green_clean(words, letter, index):
    new = []
    for i in range(len(words)):
        if letter == words[i][index]:
            new.append(words[i])
    return new

def new_list(words, info):
    greys = []
    yellows = []
    temp = []
    mid = []
    final = []
    for i in range(len(info)):
        if info[i][0] == 2:
            greys.append(info[i][1])
        if info[i][0] == 1:
            yellows.append(info[i][1])
    #print(greys)
    #print(yellows)
    for i in range(len(words)):
        if all(char in words[i] for char in yellows):
            temp.append(words[i])
    for i in range(len(temp)):
        flag = 0
        j = 0
        while flag != 1 and j < len(greys):
            if greys[j] in temp[i]:
                flag = 1
                j = j + 1
            else:
                j = j + 1
        if flag == 0:
            mid.append(temp[i])
    for i in range(len(info)):
        if info[i][0] == 0:
            mid = green_clean(mid,info[i][1],i)
    return mid

def rand_auto_worlde(words,guess,correct):
    if correct == guess:
        print("Your guess of " + guess + " is correct")
        return guess
    else:
        info = return_info(words,correct,guess)
        update = new_list(words,info)
        rand = gen_rand_int(len(update))
        print(update)
        print(update[rand])
        rand_auto_worlde(update,update[rand],correct)
    
        


if __name__ == "__main__":
    #List = ["BERRY","PASTA","PRUNE","FUNNY","CUNTY","RUTYB"]
    #word = "BUNNY"
    #search_words(List,word)            
    #print(gen_rand_int())
    #guesser(word)
    #Words = get_words("sgb-words.txt")
    #wordle()
    words = get_words("sgb-words.txt")
    index = gen_rand_int(len(words))
    print(rand_auto_worlde(words,words[index],"WEARY"))
    #info = return_info(words,words[index],"WEARY")
    #print(info)
    #print(new_list(words,info))

    