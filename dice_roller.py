def main():

  import random

  dice_rolls = 2
  dice_sum = 0

  for i in range(0, dice_rolls):
      roll = random.randint(1, 6)
      dice_sum = dice_sum + roll
      if roll == 1:
          print(f'You rolled a {roll}! Schade...')
      elif roll == 2:
          print(f'You rolled a {roll}! Du wirst besser!')
      elif roll == 5:
               print(f'You rolled a {roll}! Knapp daneben!')
      elif roll == 6:
          print(f'You rolled a {roll}! Das ist Spitze!')
      else:
          print(f'You rolled a {roll}')
          
  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()
