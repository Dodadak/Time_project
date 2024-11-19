import random
import string


def generate_password(keyword, length):
    if length < 8:
        raise ValueError("비밀번호는 최소 8자 이상이어야 합니다.")


    characters = string.ascii_letters
    password = list(keyword)
    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    return "".join(password)


def generate_input():
    keyword = input("키워드를 입력하세요: ")
    password_length = int(input("비밀번호 길이를 입력하세요: "))

    length = random.randint(1, 6) 
    random_number = "".join(
        str(random.randint(0, 9)) for _ in range(length)
    )  

    special_chars = ["!", "@", "#"]

    try:
        generated_password = generate_password(keyword, password_length)
        print(
            "생성된 비밀번호:",
            generated_password + random_number + random.choice(special_chars),
        )
    except ValueError as e:
        print(e)
