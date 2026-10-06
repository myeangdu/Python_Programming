# 1. 패키지를 import 할 때 실행되어야 하는 초기화 코드(환경 확인, 설정값 로드)

print("__init__")
# 2. 패키지 메타데이터 설정(버전 정보, 작성자)
VERSION = "1.0.0"

from .mymain import add