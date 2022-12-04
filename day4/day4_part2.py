def elf_pair_generator():
    with open('input.txt', 'r') as elf_pairs:
        for elf_pair in elf_pairs:
            yield elf_pair.strip().split(',')

def expand_section_range(elf: str):
    abbreviated_section_range = elf.split('-')
    return [
        section for section in range(
            int(abbreviated_section_range[0]),
            int(abbreviated_section_range[1])+1
        )
    ]

def one_section_intersects_another(section_range_a, section_range_b):
    return len(set(section_range_a).intersection(section_range_b)) >= 1

if __name__ == '__main__':
    redundant_assignment_count = 0
    for elf_pair in elf_pair_generator():
        range_one, range_two = elf_pair
        if one_section_intersects_another(expand_section_range(range_one), expand_section_range(range_two)):
            redundant_assignment_count += 1
    print(redundant_assignment_count)
