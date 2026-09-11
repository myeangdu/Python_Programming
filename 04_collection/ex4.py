# 튜플 심화

# ===========================================================
#  튜플에서 제공하는 메소드
# ===========================================================

t = (1, 1, 2, 2, 2)

print(t.count(1))                   # 1이 몇개 있는지?

print(t.index(2))                   # 2의 첫번째 인덱스는?


# ===========================================================
#  그 외
# ===========================================================

# tuple -> list 변환
l = list(t)
print(l)

# list -> tuple 변환
t = tuple(l)
print(t)

# 튜플을 이용해서 swap하기
a, b = 10, 20
a,b = b, a
print(a, b)

# 튜플 언패킹
t = (1, 2, 3, 4)

print(*t)

a, b, c, d = t
print(a, b, c, d)

a, *b, c = t
print(a, b, c)

t2 = (5, 6)
print(t + t2)

print((*t, *t2))

# zip 함수 사용
subjects = ("국어", "수학", "영어")
scores = (80, 90, 95)

# (('국어', 80), ('수학', 90), ('영어', 95)) 출력하기
result = tuple(zip(subjects, scores, strict=True))
print(result)

# ===========================================================
#  Tuple Comprehension은 없음
# ===========================================================

gen = ( x for x in range(1, 11) )
print(result)
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
    print(i, end=" ")
print()

# Generator는 순회가 끝나면 소진됨
for i in gen:
    print(i, end=" ")
print()

# List Comprehension vs Generator
a = [x for x in range(1, 11)]
b = (x for x in range(1, 11))
print(a, b)

print(sum(a), sum(a))
print(sum(b), sum(b))

# 1 ~ 10의 제곱수 튜플 만들기
# ()는 튜플이 아니라 generator를 생성하는 generator 표현식임
result = tuple( i ** 2 for i in range(1, 11))       # tuple 안 인자가 1개일 경우 ()생략 가능
print(result)

# tuple의 생성자에 generator를 넘겨 값을 순회하면서 튜플을 만듦



# 두 점의 x, y, z축 좌표값끼리 더한 튜플을 만들기
p1 = (1, 2, 3)
p2 = (10, 20, 30)
result = tuple(a + b for a, b in zip(p1, p2))

# =========================================================
#  🔥 실습 문제
# =========================================================

# 일주일 동안의 학습 시간을 저장한 튜플
days = ("일","월","화","수","목","금","토")
hours = (2, 3, 1, 4, 5, 2, 6)

# 1️⃣ 월 ~ 금까지 총 학습시간 출력하기
print(sum(hours))                                                    # ✅ 15시간


# 2️⃣ 가장 많이 공부한 시간 출력하기
print(max(hours))                                                    # ✅ 6시간


# 3️⃣ 가장 많이 공부한 요일 출력하기
print(days[hours.index(max(hours))])                                                    # ✅ 토요일


# 4️⃣ 가장 높은 점수와 가장 낮은 점수 출력하기
scores = (90, 85, 78, 92, 88, 76)


print(f"max 점수: {max(scores)}점, min 점수: {min(scores)}점")                                                    # ✅ max 점수: 92점, min 점수: 76점


# # 5️⃣ 과일가게 총 재고 금액 구하기
# stocks = (
#     ("사과", 1000, 5),
#     ("바나나", 2000, 3),
#     ("체리", 5000, 2),
# )

# # 총 재고 금액 출력
# print(sum(b * c for a, b, c in stocks))                                        # ✅ 총액: 21,000원


# 5️⃣ 과일가게 총 재고 금액 구하기
stocks = (
    ("사과", "바나나", "체리"),
    (100, 2000, 500),
    (5, 3, 2),
)

# 총 재고 금액 출력
print(sum(stocks[1][i] * stocks[2][i] for i in range))                                        # ✅ 총액: 21,000원
