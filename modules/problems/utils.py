DIFFICULTY_MAP = {
    1: 'Easy',
    2: 'Medium',
    3: 'Hard'
}

def get_difficulty_level(numeric_difficulty):
    return DIFFICULTY_MAP.get(numeric_difficulty, 'Easy')
