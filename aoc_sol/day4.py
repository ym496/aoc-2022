import re

pairs = open('aoc_input/day4.txt', 'r')
overlapCount = 0
fullyContainCount = 0

for i in pairs:
  pairList = re.split('[-,]', i.rstrip())
  firstPair = set(range(int(pairList[0]), int(pairList[1]) + 1))
  secondPair = set(range(int(pairList[2]), int(pairList[3]) + 1))
  if firstPair & secondPair:
    overlapCount += 1
  if firstPair.issubset(secondPair) or secondPair.issubset(firstPair):
    fullyContainCount += 1
