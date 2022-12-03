calories_input = open('day1_input.txt', 'r')
elf_calories = list()
current_elf_calories = 0

for line in calories_input:
    if line != '\n':
        current_elf_calories += int(line)
    else:
        elf_calories.append(current_elf_calories)
        current_elf_calories = 0

print(max(elf_calories))