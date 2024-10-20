from password_generate import generate_input
from password_security import genetic_algorithm


def main():
    print(
        """
==================================================
            1. 보안 등급 확인하기
            2. 추천 비밀번호 생성받기
            3. 종료
==================================================
"""
    )

    while True:
        a = int(input("선택: "))
        if a == 1:
            TARGET_PASSWORD = input("비밀번호: ")
            genetic_algorithm(TARGET_PASSWORD)
        elif a == 2:
            generate_input()
        elif a == 3:
            print("종료되었습니다")
            break
        else:
            print("없는 번호입니다")


if __name__ == "__main__":
    main()
