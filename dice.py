import random

def diceroll(reroll):
    rolls=[]
    if not reroll:
      for i in range(5):
       roll=random.randint(1,6)
       rolls.append(roll)
    elif reroll:
       for i in range(len(reroll)):
          if reroll[i]==9:
             reroll[i]=random.randint(1,6)
       rolls=reroll
    return rolls