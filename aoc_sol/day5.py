import re

StacksofCrates = open('aoc_input/day5.txt', 'r')
count = 0
stacks = {}


def createStacks(crates, line):
  start = 0
  for i in line:
    if i == '[':
      pos = line.find('[', start)
      start = pos + 1
      crateNum = int((pos / 4)) + 1
      if crateNum in stacks.keys():
        stacks[crateNum].insert(0, crates[0])
      else:
        stacks[crateNum] = []
        stacks[crateNum].append(crates[0])
      crates.pop(0)


def move(n, stackFrom, stackTo):
  c = 0
  while c != n:
    stackTo.append(stackFrom[-1])
    stackFrom.pop()
    c += 1
  return stackFrom, stackTo


for i in StacksofCrates:
  count += 1
  if count < 9:
    a = re.findall('\w', i)
    createStacks(a, i)
  if count > 10:
    a = re.findall('\d+', i)
    f, t = stacks[int(a[1])], stacks[int(a[2])]
    stacks[int(a[1])], stacks[int(a[2])] = move(int(a[0]), f, t)

firstCrate = []
for i in range(1, len(stacks.keys()) + 1):
  try:
    firstCrate.append(stacks[i][-1])
  except:
    continue
message = ''.join(firstCrate)
