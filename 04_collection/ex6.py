# 딕셔너리 심화

# ===========================================================
#  딕셔너리에서 제공하는 메소드
# ===========================================================

d = {"name": "뽀로로", "age": 5}

d2 = {"age": 23, "city": "일산"}

d.update()
print(d)

print(d2.pop("city"))
print(d)
# ===========================================================
#  그 외
# ===========================================================

d = {"kor": 90, "mat": 85, "eng": 80, "prog": 100}

# 딕셔너리 언패킹
print(*d)
print(*d.values())
print(*d.items())

a, *b, c = d
print(a, b, c)

print({**d})


# 위 딕셔너리를 key 리스트와 value 리스트로 만들기
subjects = list(d)
print(subjects)

# 리스트를 다시 딕셔너리로 만들기
# zip 함수로 튜플을 먼저 만들고, dict()에서 튜플의 [0]값을 key로, [1]값을 value로 넣음
print(dict(zip(subjects, d)))


# ===========================================================
#  딕셔너리 Comprehension
# ===========================================================

# 1 ~ 10의 제곱수 딕셔너리 만들기
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25 .. }

result = {i: i ** 2 for i in range(1, 11)}
print(result)


# 1 ~ 10 중 홀수를 키로, 제곱수를 값으로 하는 딕셔너리
# {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
result = {i: i ** 2 for i in range(1, 11, 2)}
print(result)


# 위 result 딕셔너리의 키와 값 바꾸기
# {1: 1, 9: 3, 25: 5, 49: 7, 81: 9}
result = {v: k for k, v in result.items()}
print(result)


# 점수 90 이상만 필터링하기
scores = {"국어": 90, "영어": 85, "수학": 95, "과학": 90}
result = {v:k for k, v in scores.items() if v >= 90}
print(result)


# =========================================================
#  🔥 실습 문제
# =========================================================

# 1️⃣ 바구니에 있는 과일의 단어 개수 세기
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
result = {}
for w in words:
    if w not in result:
        result[w] = 1
    else:
        result[w] += 1

print(result)

count = {}
for w in words:
    count[w] = count.get(w, 0) + 1

count = {w: words.count(w) for w in words}

from collections import Counter
print(Counter())

                                    # ✅ {'apple': 3, 'banana': 2, 'cherry': 1}


# 2️⃣ 60점 이상인 경우 합격 설정하기
scores = {"국어": 85, "영어": 50, "수학": 95, "과학": 40, "사회": 72}
result = {v: k for v, k in scores.items() if k >= 60}
print(result)

                                    # ✅ {'국어': '합격', '수학': '합격', '사회': '합격'}


# 3️⃣ 과목 리스트와 점수 리스트로 딕셔너리 만들기
subjects = ["국어", "영어", "수학"]
grades = [90, 80, 100]
result = {subjects[i]:grades[i] for i in range(3)}
print(result)

                                    # ✅ {'국어': 90, '영어': 80, '수학': 100}


# 4️⃣ 기존 재고에 입고 내역을 합치기 (이미 있는 상품은 합산, 새 상품은 추가)
stock = {"연필": 10, "지우개": 5, "노트": 3}
incoming = {"지우개": 4, "노트": 7, "볼펜": 12}

for item, count in incoming.items():
    if item in stock:
        stock[item] += count
    else:
        stock[item] = count

stock.update({item: stock.get(item, 0) + qty for item, qty in incoming.items()})
print(stock)
                                    # ✅ {'연필': 10, '지우개': 9, '노트': 10, '볼펜': 12}