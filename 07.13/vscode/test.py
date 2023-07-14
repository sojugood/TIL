# 규칙 정의
rules = {"111": "0", "110": "1", "101": "0", "100": "1", "011": "1", "010": "0", "001": "1", "000": "0"}

# 초기 상태
state = "0000000000000000000000000000001000000000000000000000000000000"

# 30 줄 출력
for _ in range(30):
    print(state)
    # 상태 문자열의 양 끝에 0 추가
    extended_state = "0" + state + "0"
    # "" 구분자(빈 문자열 = 이어붙임).join() <- 리스트의 모든 요소를 문자열로 변환하고 구분자 사이의 값을 삽입하여 연결함.
    state = "".join(rules[extended_state[i-1:i+2]] for i in range(1, len(extended_state)-1))