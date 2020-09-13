def main():

  import random

  question = str(input("Gerade oder ungerade?"))
  if question == "gerade":
       print("Du hast gerade gewählt, viel Glück!")
  if question == "ungerade":
       print("Du hast ungerade gewählt, viel Glück!")

  for i in 1:
      roll = random.randint(0, 6)
      print(f'Du hast eine {roll}')






  #dice_size = int(input('Wie viele Seiten hat dein Würfel?'))

  #dice_sum = 0

  #for i in range(0, dice_rolls):
      #roll = random.randint(1, dice_size)
      #dice_sum = dice_sum + roll
      #if roll == 1:
          #print(f'You rolled a {roll}! Schade...')
      #elif roll == dice_size:
          #print(f'You rolled a {roll}! Das ist Spitze!')
      #else:
          #print(f'You rolled a {roll}')

  #print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()
