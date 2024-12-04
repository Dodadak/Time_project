import random
import string

keyword_data = {
    "apple": {"color": "red", "taste": "sweet"},
    "lemon": {"color": "yellow", "taste": "sour"},
    "chocolate": {"color": "brown", "taste": "bitter"},
    "sky": {"color": "blue", "taste": "none"},
    "coffee": {"color": "black", "taste": "bitter"}
}

def generate_password(keyword, length=12):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
    
    info = keyword_data.get(keyword.lower())
    if not info:
        return "Keyword not found in database. Try another keyword."
    
    color = info["color"]
    taste = info["taste"]
    
    combined_info = (color + taste)[:length - 4]
    remaining_length = length - len(combined_info) - 4

    random_letters = ''.join(random.choices(string.ascii_letters, k=remaining_length))
    
    random_numbers = ''.join(random.choices(string.digits, k=2))
    random_special = ''.join(random.choices("!@#$%^&*", k=2))
    
    password = combined_info + random_letters + random_numbers + random_special
    return password
