import random 

words = ["banana",
"elephant",
"computer",
"chocolate",
"butterfly",
"adventure",
"sunshine",
"happiness",
"universe",
"mountain",
"waterfall",
"telephone",
"guitar",
"kangaroo",
"pizza",
"rainbow",
"treasure",
"whisper",
"vacation",
"icecream"]

# extract word from a file

# f = open("words.txt", "r")
# data = f.readline()
# words = data.split()
# word = random.choice(words)
# word = word.lower()


word = random.choice(words)
total_chances = 7
guess_word = "-" * len(word)
print("Let's Begin!")
print(guess_word)

while total_chances != 0:
    
    print("Guess a word:")
    letter = input("Guess a letter :").lower()
    
    if letter in word:
        
            for i in range(len(word)):
                if word[i] == letter:
                    guess_word = guess_word[:i] + letter + guess_word[i + 1:]
                    print(guess_word)

            if guess_word == word:
                print("Congratulations, You Won!!")
                break  
        
    else :
        total_chances -= 1
        print("Incorrect Guess")
        print (guess_word)
        print("Your remaining chances are:", total_chances)

else :
    print("Game Over")
    print("Sorry You Lose")
    print("The correct word is :", word) 