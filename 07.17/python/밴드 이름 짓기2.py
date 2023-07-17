import random

def random_line_from_each_file(file_path1, file_path2):
    with open(file_path1, 'r', encoding='utf-8') as file1, open(file_path2, 'r', encoding='utf-8') as file2:
        line1 = random.choice(file1.readlines()).strip()  # strip()은 줄 끝의 줄바꿈 문자를 제거
        line2 = random.choice(file2.readlines()).strip()  # strip()은 줄 끝의 줄바꿈 문자를 제거
        combined_line = line1 + ' ' + line2
    return combined_line

# 함수 사용 예시
print(random_line_from_each_file('color.txt', 'food.txt'))
