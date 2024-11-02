def diceroll(reroll):
    rolls=[]
    if not reroll:
      for i in range(6):
       roll=random.randint(1,6)
       rolls.append(roll)
    elif reroll:
       for i in range(len(reroll)):
          if reroll[i]==9:
             reroll[i]=random.randint(1,6)
       rolls=reroll
    return rolls

def totalscore(dice):
    return sum(dice)

def fiveofakind(dice):
    for die in set(dice):
        if dice.count(die)==5:
          return die*5
    return 0


def yatzycheck(dice):
    score=0
    if dice.count(dice[0])==6:
        score=100
    return score

def scorenumber(dice,number):
    count=dice.count(number)
    score=count*number
    return score
def scorepair(dice):
    pairs=[]
    for die in set(dice):
        if dice.count(die)>=2:
            pairs.append(die)
    score=0
    highestpair=0
    if len(pairs)>0:
        highestpair=max(pairs)
    else:
        highestpair=0
    score=highestpair*2
    return score

def onepair(dice):
    for die in set(dice):
        if dice.count(die)>=2:
            score=die*2
            return score
    return 0
def twopair(dice):
    pairs=[]
    for die in set(dice):
        if dice.count(die)>=2:
            pairs.append(die)
    if len(pairs)>=2:
        score=(pairs[0]*2)+(pairs[1]*2)
        return score
    return 0

def threekind(dice):
    for die in set(dice):
        if dice.count(die)>=3:
            score=die*3
            return score
    return 0

def fourkind(dice):
    for die in set(dice):
        if dice.count(die)>=4:
            score=die*4
            return score
    return 0
def smallstraight(dice):
    sorteddice=sorted(set(dice))
    if sorteddice==[1,2,3,4,5]:
        return 15
    return 0

def largestraight(dice):
    sorteddice=sorted(set(dice))
    if sorteddice==[2,3,4,5,6]:
        return 20
    return 0
def fullstraight(dice):
    sorteddice=sorted(set(dice))
    if sorteddice==[1,2,3,4,5,6]:
        return 21
    return 0

def fullhouse(dice):
    counts={}
    for die in dice:
        if die in counts:
            counts[die]+=1
        else:
            counts[die]=1
    pair=0
    triple=0
    for die in counts:
        if counts[die]==2:
            pair=1
        elif counts[die]==3:
            triple=1
    if len(counts)==2 and pair+triple==2:
        return sum(dice)
    return 0   
    
def villa(dice):
    counts={}
    for die in dice:
        if die in counts:
            counts[die]+=1
        else:
            counts[die]=1
    threeofkind=0
    for die in counts:
        if counts[die]==3:
            threeofkind+=1
    if threeofkind==2:
        return sum(dice)
    return 0
def tower(dice):
    counts={}
    for die in dice:
        if die in counts:
            counts[die]+=1
        else:
            counts[die]=1
    countfour=0
    counttwo=0
    for die in counts:
        if counts[die]==4:
            countfour+=1
        elif counts[die]==2:
            counttwo+=1
    if countfour==1 and counttwo==1:
        return sum(dice)
    return 0
        
def bonuscheck(scorecategories):
    uppersection=['ones','twos','threes','fours','fives','sixes']
    upperscore=0
    for category in uppersection:
        if category in scoredcategories:
            upperscore+=scoredcategories[category]
        if upperscore>=73:
            return 50
    return 0