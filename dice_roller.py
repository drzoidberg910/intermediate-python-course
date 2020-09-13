def main():

  import random

  dice_size = int(input('Wie viele Seiten hat dein Würfel?'))
  dice_rolls = int(input('Wie viele Würfel möchtest du werfen?'))
  dice_sum = 0

  for i in range(0, dice_rolls):
      roll = random.randint(1, dice_size)
      dice_sum = dice_sum + roll
      if roll == 1:
          print(f'You rolled a {roll}! Schade...')
      elif roll == dice_size:
          print(f'You rolled a {roll}! Das ist Spitze!')
      else:
          print(f'You rolled a {roll}')

  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()
