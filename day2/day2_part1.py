encrypted_strategy_guide = open('input.txt', 'r')
total_score = 0

def rock_paper_scissors(your_shape, opp_shape):
    base_score = { 'X': 1, 'Y': 2, 'Z': 3 }
    round_score = {
        'X': { 'A': 3, 'B': 0, 'C': 6 },
        'Y': { 'A': 6, 'B': 3, 'C': 0 },
        'Z': { 'A': 0, 'B': 6, 'C': 3 }
    }
    return base_score[your_shape] + round_score[your_shape][opp_shape]

for line in encrypted_strategy_guide:
    opp_shape, your_shape = line.strip().split(' ')
    total_score += rock_paper_scissors(your_shape, opp_shape)

print(total_score)