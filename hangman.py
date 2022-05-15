def WordToList(word):
    '''takes in a word as a string and returns its elements as a list'''
    word_element = []
    for i in word:
        word_element.append(i) #inefficient but adds each string element into list
    return(word_element)
def CompareElements(listA, listB):
    '''takes in two Lists A and B and records the common elements'''
    common_elements = []
    for i in listA:
        for j in listB:
            if i == j: #compares each element of listA to each element of listB
                common_elements.append(i)
    return(common_elements)

from random_word import RandomWords
r = RandomWords()
start = input("begin game? (Y/N)")
if start == "Y":
    word = r.get_random_word()


attempts = 0 #initializes attempt counter
print("The word is", len(word),"letters long")
while attempts <=5 : #sets attempt limit
    guess = input("Enter a guess") #prompts user input
    while len(guess) != len(word):
        print("Your Guess is not long enough! Try another guess")
        guess = input("Enter another guess")
    if guess==word: #compares user guess to set word
        print("Game Clear") #prints clear message
        break
    else:
        
        word_element = WordToList(word) #breaks the word into a list
        guess_element = WordToList(guess) #breaks the guess into a list
        common_letter_count =len(set(word_element)&set(guess_element)) #determines the correct letters
        common_letters = CompareElements(word_element, guess_element) #determines the number of times letter appears
        print("Try Again") #prints failure message
        print("You got", common_letter_count, "letters right") #lets user know the correct letters
        print("They are:", common_letters) #lets user know if any letters are repeated
        attempts = attempts+1 #increments attempts
if attempts >5: #ensure failure message is only generated if more than 5 attempts are taken
    print("Game Not Cleared! The word was:", word) #failure message printed with correct word





        