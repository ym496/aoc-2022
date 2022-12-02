fdescriptor = open('aoc_input/day2.txt', 'r')
totalScore = 0
mapVar = {
  "X": "Rock",
  "Y": "Paper",
  "Z": "Scissors",
  "A": "Rock",
  "B": "Paper",
  "C": "Scissors"
}
mapChoice = {"Rock": 1, "Paper": 2, "Scissors": 3}
defeats = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

def outcome(choice1, choice2):
  if choice1 == choice2:
    return 3
  elif defeats[choice2] == choice1:
    return 6
  else:
    return 0

for i in fdescriptor:
  if i == '\n':
    break
  totalScore += outcome(mapVar[i[0]], mapVar[i[2]]) + mapChoice[mapVar[i[2]]]
