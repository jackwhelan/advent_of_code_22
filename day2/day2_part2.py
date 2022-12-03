encrypted_strategy_guide = open('input.txt', 'r')
total_score = 0

def rock_paper_scissors(opp_shape, desired_outcome):
    round_score = { 'X': 0, 'Y': 3, 'Z': 6 }
    base_score = { 'A': 1, 'B': 2, 'C': 3 }
    your_shape = {
        'X': { 'A': 'C', 'B': 'A', 'C': 'B' },
        'Y': { 'A': 'A', 'B': 'B', 'C': 'C' },
        'Z': { 'A': 'B', 'B': 'C', 'C': 'A' }
    }
    return base_score[your_shape[desired_outcome][opp_shape]] + round_score[desired_outcome]

for line in encrypted_strategy_guide:
    opp_shape, desired_outcome = line.strip().split(' ')
    total_score += rock_paper_scissors(opp_shape, desired_outcome)

print(total_score)