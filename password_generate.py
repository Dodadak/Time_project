import random
import string


def generate_password(keywords, length=12):
    # 키워드 리스트에서 랜덤으로 선택한 문자열
    password_base_length = length // 2
    password_base = "".join(
        random.choice(keywords) for _ in range(password_base_length)
    )

    # 비밀번호에 필요한 길이를 맞추기 위해 문자만 추가
    length = length - password_base_length

    # 제외할 특수문자를 제외한 나머지 문자들
    chars = string.ascii_letters  # 문자만 사용

    # 추가 문자 생성 (문자만 포함)
    additional_chars = "".join(random.choices(chars, k=length))

    # 키워드 기반 문자열과 추가 문자를 합친 후 섞기
    password = list(password_base + additional_chars)
    random.shuffle(password)

    # 최종적으로 섞인 비밀번호 반환
    password = "".join(password)

    return password[:length]


def generate_input():
    # 키워드 입력 받기
    keywords_input = input("키워드를 입력해주세요:")
    keywords = [word.strip() for word in keywords_input.split(",")]
    password_length = int(input("Enter password length: "))

    length = random.randint(1, 6)  # 1부터 6까지 랜덤 자릿수
    random_number = ''.join(str(random.randint(0, 9)) for _ in range(length))  # 자릿수만큼 0부터 9까지 랜덤 숫자 뽑기

    special_chars = ['!', '@', '#']  
    random.choice(special_chars)
    
    # 비밀번호 생성
    if password_length < 8:
        print("8 이상의 비밀번호만 생성 가능합니다")
    else:
        password = generate_password(keywords, password_length)
        print(f"Generated Password: {password+random_number+random.choice(special_chars)}")

