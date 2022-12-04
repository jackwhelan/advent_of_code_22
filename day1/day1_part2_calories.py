with open('input.txt', 'r') as calories_input:
    elf_calories = list()
    current_elf_calories = 0

    for line in calories_input:
        if line != '\n':
            current_elf_calories += int(line)
        else:
            elf_calories.append(current_elf_calories)
            current_elf_calories = 0

    sum_of_top_three = 0
    for i in range(3):
        sum_of_top_three += elf_calories.pop(elf_calories.index(max(elf_calories)))

    print(sum_of_top_three)