# 사용자 정의 모듈
print("start:", __name__)  # 모듈의 이름을 가져오는 내장 변수
PI = 3.14


def add(a, b):
    return a + b


print(PI)
print(add(10, 20))

# 직접 실행한 경우
if __name__ == "__main__":
    print(PI)
    print(add(10, 20))
