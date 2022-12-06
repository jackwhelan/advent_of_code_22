import re
import string
import random

def split_stack_and_procedure_input():
    with open('input.txt', 'r') as entire_input:
        with open('stacks.txt', 'w') as stack_data, open('procedure.txt', 'w') as procedure_data:
            for line in entire_input:
                if line.startswith((' ', '[')):
                    stack_data.write(line)
                else:
                    procedure_data.write(line)


def parse_stack_data():
    with open('stacks.txt', 'r') as stack_data:
        lines = {}
        for i in range(1, 34, 4):
                lines[i] = []
        for line in stack_data:
            for i in range(1, 34, 4):
                if line[i] not in string.digits + ' ':
                    lines[i].append(line[i])
        stacks = list(lines.values())
        for stack in stacks:
            stack.reverse()
        return stacks


def procedure_data_generator():
    with open('procedure.txt', 'r') as procedure_data:
        for line in procedure_data:
            yield line


def follow_procedure(procedure, stack_data):
    instructions = [int(x) for x in re.findall(r'\d+', procedure)]
    quantity, column_from, column_to = instructions
    stack_data[column_to-1].extend(stack_data[column_from-1][-quantity:])
    del stack_data[column_from-1][-quantity:]
    return stack_data


if __name__ == '__main__':
    split_stack_and_procedure_input()
    stack_data = parse_stack_data()
    for procedure in procedure_data_generator():
        if procedure[0].isalpha():
            stack_data = follow_procedure(procedure, stack_data)
    final_string = ''
    for stack in stack_data:
        final_string += stack.pop()
    print(final_string)

