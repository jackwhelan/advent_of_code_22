import string

def elf_group_generator(group_size):
    with open('input.txt', 'r') as elf_list:
        elf_group = []
        for elf in elf_list:
            elf_group.append(elf.strip())
            if len(elf_group) == group_size:
                yield elf_group
                elf_group = []

if __name__ == '__main__':
    priorities = {key: value for (key, value) in zip(string.ascii_letters, [num for num in range(1, 53)])}
    common_items = []
    sum_of_priorities = 0

    for elf_group in elf_group_generator(3):
        elf1, elf2, elf3 = elf_group
        badge = ''.join(set(elf1) & set(elf2) & set(elf3))
        sum_of_priorities += priorities[badge]

    print(sum_of_priorities)