import random
import string


def generate_password(keyword, length):
    if length < 8:
        raise ValueError("비밀번호는 최소 8자 이상이어야 합니다.")

    # 사용할 문자 집합 정의 (숫자와 특수문자를 제외한 알파벳만 사용)
    characters = string.ascii_letters

    # 키워드가 비밀번호의 일부로 포함됨
    password = list(keyword)

    # 비밀번호의 나머지 자리를 무작위로 채움
    while len(password) < length:
        password.append(random.choice(characters))

    # 비밀번호 섞기
    random.shuffle(password)

    return "".join(password)


def generate_input():
    # 키워드와 비밀번호 길이 입력
    keyword = input("키워드를 입력하세요: ")
    password_length = int(input("비밀번호 길이를 입력하세요: "))

    length = random.randint(1, 6)  # 1부터 6까지 랜덤 자릿수
    random_number = "".join(
        str(random.randint(0, 9)) for _ in range(length)
    )  # 자릿수만큼 0부터 9까지 랜덤 숫자 뽑기

    special_chars = ["!", "@", "#"]

    # 비밀번호 생성 및 출력
    try:
        generated_password = generate_password(keyword, password_length)
        print(
            "생성된 비밀번호:",
            generated_password + random_number + random.choice(special_chars),
        )
    except ValueError as e:
        print(e)
