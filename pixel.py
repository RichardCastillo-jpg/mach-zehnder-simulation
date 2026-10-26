import random
MAX_ATTEMPTS = 10

def attempt(has_bomb):
    if has_bomb:
        percentage = random.random()
        if percentage < 0.5:
            return "EXPLODED"
        elif percentage < 0.75:
            return "FUNCTIONAL"
        else:
            return "UNKNOWN"

    else: 
        return "UNKNOWN"

def test_pixel(has_bomb):
    for _ in range(MAX_ATTEMPTS):
        result = attempt(has_bomb)
        if result != "UNKNOWN": 
            return result
    
    return "UNKNOWN"
        

