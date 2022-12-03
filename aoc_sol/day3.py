import re

rucksacks = open('aoc_input/day3.txt', 'r')
sum = 0
group = []


def priority(letter):
  if letter.isupper():
    return ord(letter.lower()) - 96 + 26
  else:
    return ord(letter) - 96


for rucksack in rucksacks:
  group.append(rucksack.rstrip())
  if len(group) == 3:
    commonItemtype1 = re.sub("[^" + group[1] + "]", "", group[0])
    commonItemtype2 = re.sub("[^" + group[2] + "]", "", commonItemtype1)
    sum += priority(commonItemtype2[0])
    group.clear()
