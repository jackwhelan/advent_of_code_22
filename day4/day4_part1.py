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

def one_section_range_is_subset_of_another(section_range_a, section_range_b):
    a_contains_b = set(section_range_b).issubset(set(section_range_a))
    b_contains_a = set(section_range_a).issubset(set(section_range_b))
    return a_contains_b or b_contains_a

if __name__ == '__main__':
    redundant_assignment_count = 0
    for elf_pair in elf_pair_generator():
        range_one, range_two = elf_pair
        if one_section_range_is_subset_of_another(expand_section_range(range_one), expand_section_range(range_two)):
            redundant_assignment_count += 1
    print(redundant_assignment_count)
