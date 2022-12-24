mistakes = 0  # player(s) loses at 7 mistakes
isGuessed = False
word = input('Enter the secret word: ')
wordArr = []
guessedArr = []


for letter in word:
    if letter.isalpha():
        wordArr.append(letter)
    else:
        wordArr = wordArr

for i in range(len(wordArr)):
    guessedArr.append('_')

while mistakes < 7 and isGuessed is False:
    guess = input('Enter a guess: ')
    if guess == word:
        isGuessed = True
        break
    elif guess.isalpha() is False:
        print('Please enter a valid letter.')
    elif len(guess) >= 2:
        print('Guess contains multiple letters. Please enter only one letter.')
    elif guess not in wordArr:
        guessed = ''.join(guessedArr)
        mistakes += 1
        print('Letter is not in the word.')
        print(f'Guessed Letters: {guessed}\nMistakes: {mistakes}')
    else:
        for i in range(len(wordArr)):
            if guess == wordArr[i]:
                guessedArr[i] = guess
        guessed = ''.join(guessedArr)
        print(f'Letter guessed!\nGuessed Letters: {guessed}\nMistakes: {mistakes}')

    if ''.join(guessedArr).isalpha():
        isGuessed = True
    else:
        continue

if isGuessed:
    print(f'Player won! Word was: {word}')
else:
    print(f'Player lost! Word was: {word}')
