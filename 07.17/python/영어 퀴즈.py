import random
import re  # 정규 표현식 모듈을 불러옵니다.

def ko_en(file):
    with open(file, 'r', encoding='utf-8') as file1:
        file1.readline()  # 첫 줄 건너뜀.
        while True:  # 무한 루프를 시작합니다.
            line = random.choice(file1.readlines())
            line1 = re.split('[.?]', line)  # '.' 또는 '?'를 기준으로 문자열을 분할합니다. / re.split('[분리할 기준]') <- 분리할 조건 다수 일 때
            if len(line1) > 1:  # 리스트에 2개 이상의 요소가 있을 때만 실행합니다.
                ko = line1[0] + '.' if '.' in line else line1[0] + '?'  # 기존의 구분자를 붙여줍니다.
                en = line1[1].strip() #strip() <- 문자열 앞 뒤 공백 제거
                en = en + '.' if '.' in line else en + '?'  # 기존의 구분자를 붙여줍니다.
                break  # 조건이 충족되면 무한 루프를 종료합니다.
        n = input(f'Write the following sentence in English.\n{ko}\n\nyour answer: ')
        if n == en:
            print('\nresult: Correct!')
        else:
            print(f"\nresult: Not correct!\nright answer: {en}")

ko_en('ko_en.txt')
