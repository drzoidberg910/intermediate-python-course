def main():


  import random
  diceOne = random.randint(1, 6)
  diceTwo = random.randint(1, 6)
  diceThree = random.randint(1, 6)

  print(f'You rolled a {diceOne}')
  print(f'You rolled a {diceTwo}')
  print(f'You rolled a {diceThree}')

  if diceOne == diceTwo == diceThree:
      print('Du hast einen Pasch gewürfelt! Herzlichen Glückwunsch!')
  else:
      print('Leider verloren. Viel Glück beim nächsten Wurf!')


if __name__== "__main__":
  main()
