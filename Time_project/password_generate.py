import random
import string

# 키워드와 관련된 데이터를 담고 있는 딕셔너리로, 색상(color)과 맛(taste) 정보 포함.
keyword_data = {
    "apple": {"color": "red", "taste": "sweet"},
    "lemon": {"color": "yellow", "taste": "sour"},
    "chocolate": {"color": "brown", "taste": "bitter"},
    "sky": {"color": "blue", "taste": "none"},
    "coffee": {"color": "black", "taste": "bitter"}
}

# 주어진 키워드와 길이를 기반으로 비밀번호를 생성하는 함수.
def generate_password(keyword, length=12):
    # 비밀번호 길이가 최소 8자 이상인지 확인.
    if length < 8:
        raise ValueError("비밀번호 길이는 최소 8자 이상이어야 합니다.")
    
    # 딕셔너리에서 키워드에 해당하는 데이터를 대소문자 구분 없이 검색.
    info = keyword_data.get(keyword.lower())
    # 키워드가 데이터베이스에 없을 경우, 오류 메시지를 반환.
    if not info:
        return "키워드가 데이터베이스에 없습니다. 다른 키워드를 시도하세요."
    
    # 키워드에 해당하는 색상(color)과 맛(taste)을 추출.
    color = info["color"]
    taste = info["taste"]
    
    # 색상과 맛을 결합하고, 비밀번호 길이를 초과하지 않도록 필요한 부분만 사용.
    combined_info = (color + taste)[:length - 4]
    # 나머지 비밀번호를 채우기 위해 필요한 문자 길이 계산.
    remaining_length = length - len(combined_info) - 4

    # 나머지 길이에 해당하는 랜덤 알파벳 문자 생성.
    random_letters = ''.join(random.choices(string.ascii_letters, k=remaining_length))
    # 랜덤 숫자 2자리 생성.
    random_numbers = ''.join(random.choices(string.digits, k=2))
    # 랜덤 특수 문자 2자리 생성.
    random_special = ''.join(random.choices("!@#$%^&*", k=2))
    
    # 최종 비밀번호 조합.
    password = combined_info + random_letters + random_numbers + random_special
    return password
