fdescriptor = open('aoc_input/day1.txt', 'r')
maxCalories = 0
elf = []
Elves = []
for i in fdescriptor:
  if i == '\n':
    Calories = sum(elf)
    Elves.append(Calories)
    if Calories > maxCalories:
      maxCalories = Calories
    elf.clear()

  else:
    elf.append(int(i.rstrip()))

Elves.sort(reverse=True)
TotalTopthree = Elves[0] + Elves[1] + Elves[2]
