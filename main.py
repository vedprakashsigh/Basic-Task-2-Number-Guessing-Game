from random import randint 


INSTRUCTIONS = '''
1. Objective: Guess the computer's secret number within a given range.

2. Guess: Choose a number within the range (1-200), type "hint" to get number of digits of secret number, or "exit" to exit the game.

3. Feedback: Computer tells you if your guess is too high, too low, or correct.

4. Repeat: Keep guessing until you find the secret number or run out of guesses (you have 7 chances).

5. Win/Lose: Win if you find the number, lose if you run out of guesses.

6. Play Again: Option to play again after winning or losing. 
'''

def play_again() -> bool:
  wanna_play = input("Wanna play again? (y/n)").lower()
  if wanna_play == "y":
    return True
  elif wanna_play == "n":
    return False

def main() -> None:
  chances = 7
  secret_number = randint(1,200)
  isRunning = True
  print(INSTRUCTIONS)

  while isRunning and chances > 0:
    try:
      print("Lives Left: ", chances)
      k = input("Enter Your Guess Number (1-200) or 'hint' or 'exit': ")

      if k.lower() == "hint":
        print("Number of digits of the secret number: ",len(str(secret_number)))
        continue
      elif k.lower() == "exit":
        isRunning = False
        break

      k = int(k)
      if k == secret_number:
        print("Congo! You guessed correctly.")
        isRunning = play_again()
        if isRunning:
          main()
        break

      elif k > secret_number:
        print("Oops! it seems like you over shot.")
      else:
        print("Oops! it seems like you under shot. ")

      chances -= 1
      if chances > 0:
        print("Try again.")
      else:
        print("You Lost!")
        print("The number was: ",secret_number)
        isRunning = play_again()
        if isRunning:
          main()

    except:
      print("Oops! it looks like you have entered something other than a number.")

if __name__ == "__main__":
  main()