import random
import string


# 개체 하나 생성 (대소문자, 숫자, 숫자, 특수문자 포함)
def create_individual(length):
    character_set = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(character_set) for _ in range(length))


# 적합도 함수 (비밀번호가 목표 비밀번호와 얼마나 가까운지 평가)
def fitness(individual, target_password):
    indv = individual
    tgt_pwd = target_password
    return sum(indv[i] == tgt_pwd[i] for i in range(len(tgt_pwd)))


# 비밀번호 길이에 따른 점수 부여
def length_score(individual):
    length = len(individual)
    if length >= 12:
        return 5
    elif length >= 8:
        return 3
    else:
        return 1


# 비밀번호 다양성에 따른 점수 부여 (대문자, 소문자, 숫자, 특수문자 포함 여부)
def diversity_score(individual):
    has_upper = any(c.isupper() for c in individual)
    has_lower = any(c.islower() for c in individual)
    has_digit = any(c.isdigit() for c in individual)
    has_special = any(c in string.punctuation for c in individual)

    return sum([has_upper, has_lower, has_digit, has_special])


# 비밀번호 총점 계산
def total_score(individual):
    return length_score(individual) + diversity_score(individual)


# 보안 등급 구분
def security_rating(individual):
    score = total_score(individual)
    if score >= 8:
        return "안전"
    elif score >= 5:
        return "보통"
    else:
        return "위험"


# 개체 교배 (부모 두 개체의 유전자를 교환)
def crossover(parent1, parent2):
    index = random.randint(0, len(parent1) - 1)
    return parent1[:index] + parent2[index:]


# 변이 (개체의 유전자를 일부 변경, 변이율을 높여서 다양한 해 탐색)
def mutate(individual, mutation_rate=0.05):
    character_set = string.ascii_letters + string.digits + string.punctuation
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.choice(character_set)
    return "".join(individual)


# 메인 유전 알고리즘 함수
def genetic_algorithm(target_password):
    population_size = 100
    generations = 1000
    mutation_rate = 0.05
    population = [
        create_individual(len(target_password)) for _ in range(population_size)
    ]

    for generation in range(generations):
        population = sorted(
            population, key=lambda x: fitness(x, target_password), reverse=True
        )
        best_individual = population[0]
        if fitness(best_individual, target_password) == len(target_password):
            gen = generation
            best_indv = best_individual
            print(f"Generation {gen}: " f"Found password {best_indv}")
            print(
                f"Total Score: {total_score(best_individual)}, "
                f"Security Rating: {security_rating(best_individual)}"
            )
            break
        next_generation = population[:10]  # 상위 10개 개체 선택
        for _ in range(population_size - 10):
            parent1, parent2 = random.sample(next_generation, 2)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            next_generation.append(child)
        population = next_generation
        print(
            f"Generation {generation}: Best so far {best_individual}, "
            f"Security Rating: {security_rating(best_individual)}"
        )

    print(
        f"{best_individual} 해당 비밀번호는 "
        f"{security_rating(best_individual)} 입니다"
    )