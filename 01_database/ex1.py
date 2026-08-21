# 동적
# 동적 타이핑 언어

a = 2
b = 3
print(a, end = " ")
print(b)
print(a, b, sep = "")

a=2, b
print(a)
print(type(a))

a = 2;b = 3
print(a, b)

x = y = z = 0;
a, b = 2, 3
print(a, b)

# 값 swap
temp = a
a = b
b = temp

a, b = b, a
print(a, b)

# 변수명 규칙
# 문자, 숫자, 언더바만 가능
# 숫자로 시작 불가
# 대소문자 구분
# 예약어 사용 불가

name2 = "pororo"
_name = "pororo"
# class = "test"
# name! = "test"

이름 = "뽀로로"
print(이름)

student_name = "크롱"
studentName = "크롱"
MAX_COUNT = 100