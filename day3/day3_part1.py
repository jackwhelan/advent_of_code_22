import string

rucksacks_input = open('input.txt', 'r')
priorities = {key: value for (key, value) in zip(string.ascii_letters, [num for num in range(1, 53)])}
common_items = []
sum_of_priorities = 0

for rucksack in rucksacks_input:
    first = rucksack[:len(rucksack) // 2]
    second = rucksack[len(rucksack) // 2:]
    common_items.append(''.join(set(first).intersection(set(second))))

for item in common_items:
    sum_of_priorities += priorities[item]

print(sum_of_priorities)