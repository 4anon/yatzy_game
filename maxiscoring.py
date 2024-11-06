import random

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
    for die in dice:
        if dice.count(die)>=5:
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
    for die in range(6,0,-1):
        if dice.count(die)>=2:
            score=die*2
            return score
    return 0
def twopair(dice):
    pairs=[]
    for die in range(6,0,-1):
        if dice.count(die)>=2:
            pairs.append(die)
    if len(pairs)>=2:
        score=(pairs[0]*2)+(pairs[1]*2)
        return score
    return 0

def threekind(dice):
    for die in range(6,0,-1):
        if dice.count(die)>=3:
            score=die*3
            return score
    return 0

def fourkind(dice):
    for die in dice:
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
        
def bonuscheck(scoredcategories):
    uppersection=['ones','twos','threes','fours','fives','sixes']
    upperscore=0
    for category in uppersection:
        if category in scoredcategories:
            upperscore+=scoredcategories[category]
        if upperscore>=73:
            return 50
    return 0
    
# Change global variable names to avoid conflicts with function names
highest_score = 0
highscorename = ''

def highscore(totalscore, playername):
    global highest_score, highscorename  # Updated variable name
    if totalscore > highest_score:       # Use updated variable here
        highest_score = totalscore       # Update the correct variable
        highscorename = playername
    return highest_score, highscorename

def highscoreinstall():
    try: 
        with open('highscore.txt','r') as file:
            score = file.read().strip().split(',')
            if len(score) == 2:
                highscorename = score[0]
                highscore = int(score[1])
                return highscorename, highscore
            else:
                return '',0  # Fallback if the file doesn’t contain two elements
    except (ValueError, FileNotFoundError):  # Handle both missing file and value errors
        return '',0  # Default return value if there's an error

def uploadhighscore(highscorename, highscore):
    with open('highscore.txt', 'w') as file:
        file.write(f'{highscorename},{str(highscore)}')


def uploadhighscore2(highscorename, highscore):
    try:
        with open('highscore.txt','r') as file:
            lines=files.readlines()
        highscores=[]
        for line in lines:
            if linestrip():
                name,score=line.strip().split(':')
                highscores.append((name,int(score)))
        highscores.append((highscorename,highscore))
        for i in range(len(highscores)):
            for j in range(i+1,len(highscores)):
                if highscores[j][1]>highscores[i][1]:
                    highscores[i],highscores[j]=highscores[j],highscores[i]
        with open('highscore.txt','w') as file:
            for name,score in highscores:
                file.write(f'{name}:{score}\n')
    except FileNotFoundError:
        with open('highscore.txt','r') as file:
            file.write(f'{name}:{score}\n')
