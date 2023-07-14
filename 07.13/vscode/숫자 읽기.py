n = input()

def korean_number(n):
    my_dict = {'0': '영', '1': '일','2': '이','3': '삼', '4': '사', '5': '오', '6': '육', '7': '칠', '8': '팔', '9': '구'}
    return my_dict[n]

result = korean_number(n)
print(result)