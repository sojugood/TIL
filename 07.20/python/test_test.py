import requests
from pprint import pprint as print

dummy_data = []

for i in range(1, 11):
    # 무작위 유저 정보 요청 경로
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    # API 요청
    response = requests.get(API_URL)
    # JSON -> dict 데이터 변환
    parsed_data = response.json()

    selected_data = {
    'company': parsed_data['company']['name'],
    'lat': parsed_data['address']['geo']['lat'],
    'lng': parsed_data['address']['geo']['lng'],
    'name': parsed_data['name']
}
    a = parsed_data['address']['geo']['lat']
    b = parsed_data['address']['geo']['lng']

    if float(a) < 80 and float(a) > -80 and float(b) < 80 and float(b) > -80:
        dummy_data.append(selected_data)

print(dummy_data)
