fdescriptor = open('aoc_input/day2.txt', 'r')
totalScore = 0
mapVar = {"A": "Rock", "B": "Paper", "C": "Scissors"}
mapChoice = {"Rock": 1, "Paper": 2, "Scissors": 3}
defeats = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
outcome = {"X": 0, "Y": 3, "Z": 6}


def choice2(choice1, var):
  if var == 'X':
    return defeats[choice1]
  elif var == 'Y':
    return choice1
  else:
    choice = [
      i for i in defeats.keys() if i not in [choice1, defeats[choice1]]
    ]
    return choice[0]


for i in fdescriptor:
  if i == '\n':
    break
  totalScore += outcome[i[2]] + mapChoice[choice2(mapVar[i[0]], i[2])]
