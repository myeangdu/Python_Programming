# 리스트 심화

# ===========================================================
#  리스트에서 제공하는 메소드
# ===========================================================

langs = ["c", "c++", "java", "python"]

langs.append("go")  # 끝에 추가
print(langs)

langs.insert(2, "c#")  # 인덱스 2에 "c#" 추가
print(langs)

langs[3] = "javascript"  # 인덱스 3을 "javascript"로 변경
print(langs)

langs.remove("c++")  # "c++" 삭제 (첫번째 데이터만 삭제)
print(langs)

langs.pop(1)  # 인덱스 1 삭제
print(langs)

langs.pop()  # 인덱스 생략 시 마지막 항목 삭제
print(langs)

print(langs.index("python"))  # "python" 인덱스 찾기

langs.reverse()  # 리스트 순서를 거꾸로 뒤집기
print(langs)

langs.sort()  # 오름차순 정렬
print(langs)

langs.sort(reverse=True)  # 내림차순 정렬
print(langs)

langs.clear()  # 모든 item 삭제
print(langs)

# 리스트 복사
ori = [1, 2, 3]

result = ori.copy()
print(result)

# 얕은 복사(shallow copy) vs 깊은 복사(deep copy)
ori = [[1, 2], [3, 4]]

result2 = ori.copy()
result2[0].append(100)
# 깊은 복사를 하려면?
import copy

result2 = copy.deepcopy(ori)
result2.append(10000)   # 복사본만 바뀜
print(result2, ori)

# ===========================================================
#  그 외
# ===========================================================

# 중첩리스트
nested_list = [1, ["a", ["x", "y"], "b"], 2]

print(nested_list[1][1][0])         # x 출력하기
print(nested_list[1][2])            # b 출력하기
print(nested_list[2])               # 2 출력하기

# 리스트 언패킹
num = [1, 2, 3, 4]
print(*num)

a, b, c, d = num
print(a, b, c, d)

a, *b, c = num
print(a, b, c)

num2 = [5, 6]
print(num + num2)

print(*num, *num2)



# zip함수: 반복 가능(iterable)한 여러 객체를 인자로 받아
# 동일한 인덱스에 있는 원소들끼리 튜플로 묶어주는 파이썬 내장 함수
subjects = ["국어", "수학", "영어"]
scores = [80, 90, 95]

print(zip(subjects, scores))

a, b, c = zip(subjects, scores)
print(a, b, c)

for subjects, score in zip(subjects, scores):
    print(f"{subjects, score}")

print(list(zip(subjects, scores)))

# ===========================================================
#  List Comprehension
#  for문을 이용하여 각 원소에 식을 적용하여 리스트를 만드는 방법
# ===========================================================

# 1 ~ 10의 제곱수 리스트 만들기
list = []
for i in range(1, 11):
    list.append(i * i)
print(list)

result = [x**2 for x in range(1, 11)]
print(result)

# 1 ~ 10 중 짝수의 제곱수로 된 리스트 만들기 (필터링 if문 추가)
list = []
for i in range(2, 11, 2):
    list.append(i * i)
print(list)

result = [x**2 for x in range(1, 11) if x %2==0]
print(result)
# 1 ~ 10 중 짝수면 "짝", 홀수면 "홀" 출력하기

result = ["짝" if x % 2 == 0 else "홀" for x in range(1, 11)]
print(result)

# 각 이름의 길이로 이루어진 리스트 만들기
names = ["pororo", "crong", "poby", "eddy"]
result = [len(i) for i in names]

print(result)

# 길이가 5 이상인 이름만 뽑기
names = ["pororo", "crong", "poby", "eddy"]
result = [len(i) for i in names if len(i) >= 5]

print(result)

# 중첩 for문도 가능


# =========================================================
#  🔥 실습 문제
# =========================================================

# 1️⃣ 60점 이상인 점수만 뽑기
scores = [85, 42, 73, 55, 90, 68, 35, 100]

result = [i for i in scores if i >= 60]
print(result)                       # ✅ [85, 73, 90, 68, 100] 출력


# 2️⃣ 60점 이상인 경우 "합격", 60점 미만은 "불합격"으로 처리
result = ["합격" if i >= 60 else "불합격" for i in scores]
print(result)                       # ✅ ['합격', '불합격', '합격', '불합격', '합격', '합격', '불합격', '합격']


# 3️⃣ 1 ~ 100 중 3 또는 5의 배수의 합 구하기 (sum() 함수 이용)
result = [i for i in range(1, 100) if (i%3==0) or (i%5==0)]
print(sum(result))                       # ✅ 2418 출력


# 4️⃣ n을 포함하고 있는 단어만 뽑기
words = ["apple", "banana", "kiwi", "mango"]

result = [i for i in words if 'n' in i]
print(result)                       # ✅ ['banana', 'mango'] 출력


# 5️⃣ 세 학생의 3과목 점수표에서 과목별 평균 구하기
scores = [
    [90, 80, 70],       # 학생 1
    [100, 90, 80],      # 학생 2
    [80, 70, 60],       # 학생 3
]

result = [(scores[0][i] + scores[1][i] + scores[2][i])/3 for i in range(3)]
print(result)                       # ✅ [90.0, 80.0, 70.0]

# 은행가 반올림
print(round(0.5))
print(round(1.5))
print(round(2.5))
print(round(3.5))