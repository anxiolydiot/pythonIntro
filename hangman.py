import random
import os
import sys


words = [
  
'bird',
'cat',
'hat',
'grapes',
'mouse'  
  
  
]

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
    
def draw(guess_wrong, guess_right, word):
  clear()
  
  print('Strikes: {}/10'.format(len(guess_wrong)))
  print('\n\n')

  for letter in guess_wrong:
    print(letter, end= '')
  print('\n\n')
  
  for letter in word:
    if letter in guess_right:
      print(letter, end='')
    else:
      print('_',end='')
  print('')
  
  
    
def get_guess(guess_wrong, guess_right):
    while True:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1:
            print('Please only guess one letter at a time')
        elif guess in guess_wrong or guess in guess_right:
            print('You have already used this letter')
        elif not guess.isalpha():
            print("You can't guess numbers or symbols")
        else:
          return guess

def play(done):
  clear()
  word = random.choice(words)
  guess_wrong = []
  guess_right = []
  
  while True:
    draw(guess_wrong, guess_right, word)
    guess = get_guess(guess_wrong, guess_right)
    
    if guess in word:
      guess_right.append(guess)
      found = True
      for letter in word:
          if letter not in guess_right:
            found = False
          if found:
            print("You win!")
            print("Word was {}".format(word))
            done= True
    else:
      guess_wrong.append(guess)
      if len(guess_wrong) == 10:
        draw(guess_wrong, guess_right, word)
        print('rekt :(')
        print('word was {}'.format(word))
        done = True 
        
        
    if done:
      again = input('again?, Y/n:' ).lower()
      if again != 'n':
        return play(done= False)
      else:
        sys.exit()
        
def welcome():
  start = input('Return to Start, Q to Quit').lower()
  if start == 'q':
    print("good choice this is boring af")
    sys.exit()
  else:
    return True
  
  
print('Python Hangman')
done = False 

while True:
      clear()
      welcome()
      play(done)