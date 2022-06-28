import random

def main():
  dice_rolls = int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides do the dice have? '))
  dice_sum = 0

  for i in range(0, dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum += roll
    if roll == 0:
      print(f'You rolled a {roll}! Critical fail')
    elif roll == dice_size:
      print(f'You rolled a {roll}! Critical Success!')
    else:
      print(f'You rolled a {roll}')
    

  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()