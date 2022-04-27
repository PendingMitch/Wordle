array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def useWord(word):
    for letter in word:
        if letter.lower() not in array: return False
    return True


from time import sleep
f = open("dictionary.txt", "r")

for word in f:
    word = word.replace('\n', '')
    if useWord(word):
        length = len(word)

        with open("dictionary"+str(length)+".txt", "a") as newDict:
            newDict.write(word + '\n')
            newDict.close()
    

    
    bool = True



