from collections import defaultdict

wordMatrix = []
wordCountPerPerson = []

def checkWord(word):
    accents = "áéíóúÁÉÍÓÚ"
    hasUppercase = False
    hasAccent = False
    hasSpace = False
    flag = False
    
    for char in word:
        if char.isupper():
            hasUppercase = True
            break
        if char in accents:
            hasAccent = True
            break
        if char == " ":
            hasSpace = True
            break
        
    if not hasUppercase and not hasAccent and not hasSpace:
        flag = False
    else:
        flag = True
    return flag
            
def collectWords():
    words = []
    
    numberOfWords = int(input())
    
    if 1 <= numberOfWords <= 100:
        wordCountPerPerson.append(numberOfWords)
        for i in range(0, numberOfWords):
            line = input()
            if checkWord(line) == False:
                words.append(line)
            else:
                print("Check the spelling of the words.")
                break
        wordMatrix.append(words)
    else:
        print("Not within the allowed range.")
        
def getWords(numberOfPeople, wordMatrix):
    counter = defaultdict(int)
    if numberOfPeople == 1:
        for word in wordMatrix:
            counter[word] += 1
        return sorted(counter.items(), key=lambda x: (-x[1], x[0])) 
        # -x[1] ensures descending order by frequency; x[0] is used as a secondary criterion (alphabetical ascending).
    else:                                                          
        common = set(wordMatrix[0])
        for row in wordMatrix:
            common &= set(row)                                   
            for word in row:
                counter[word] += 1
        return sorted([(w, counter[w]) for w in common], key=lambda x: (-x[1], x[0])) 
        # Creates a list of tuples (word, frequency) only with common words, then sorts them with the lambda function.

people = int(input("Enter the number of people in the group: "))
if 1 <= people <= 100:
    for person in range(people):
        collectWords()
    result = getWords(people, wordMatrix)
    for element, _ in result:
        print(element)
else:
    print("Not within the allowed range.")
