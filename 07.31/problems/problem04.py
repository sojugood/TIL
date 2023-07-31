############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def make_answer(security_str, security_code):
    result = ''
    for code in security_code:
        result += security_str[code]
    # 여기에 코드를 작성하여 함수를 완성합니다.
    return result
    
    

# 아래 코드는 실행을 위한 코드입니다. 
if __name__ == '__main__':
    # 아래의 코드는 수정하지 마세요.
    answer = make_answer('kXeFSOo1spkSMsuuoAiklFeqYz', [4,11,17,21,24])
    print(answer)   # => SSAFY
    # 아래에 추가 테스트를 위한 코드 작성 가능합니다.