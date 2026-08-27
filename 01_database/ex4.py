# 문자열
# "", ''

a = "python"
print(a, type(a))
b = 'python'

# I'll be back
print("I'll be back")
# print('I'll be back')
print('I\'ll be back')

multiline = """
life is short
you need Python"""

print(multiline)

# docstring
def func():
    """이 함수는 테스트용입니다"""
    pass

print(func.__doc__)

# 문자열 연결
print("Hello" + "Python")

# 문자열 반복
print("Hello" * 10)

print("Hello" + str(10))
print("10" + "2")

#문자열 포맷팅
name = "pororo"
age = 23

print(f"이름:{name}, 나이:{age}살")

print(f"{name.upper()}")

pi = 3.141582

print(f"{pi:.3f}")
print(f"{pi:.0f}")

num = 123456789

print(f"{num:,}")
print(f"{num:15d}")
print(f"{num:<15d}")
print(f"{num:015d}")