# 비트 연산자

a = 5
b = 3
print(a&b)
print(a|b)
print(a^b)
print(a << b)

print(40 >> 3)
print(~a)

# 멤버십 연산자
print("a" in "apple")
print(3 in [1, 2, 3])

# 삼항 연산자
# int max = a>b?a:b
max = a if a>b else b
print(max)

print("짝수" if a % 2 == 0 else "홀수")

a = 85
print("A" if a >= 90 else "B" if a >= 80 else "C" if a>= 70 else "D")