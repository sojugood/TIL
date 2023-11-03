import os
import pandas as pd
from django.http import JsonResponse

# 데이터를 글로벌 변수로 읽어온다.
csv_file = os.path.join('data', 'test_data_has_null.CSV')
global_df = pd.read_csv(csv_file, encoding='euc-kr')


# A. CSV 데이터를 DataFrame으로 변환 후 반환
def load_csv(request):
    # CSV 파일의 경로 설정
    csv_file = os.path.join('data', 'test_data.CSV')
    # CSV 파일 읽기
    df = pd.read_csv(csv_file, encoding='euc-kr')
    # 결과를 딕셔너리 리스트로 변환
    data = df.to_dict('records')
    # JSON 응답으로 반환
    return JsonResponse({'data': data}, json_dumps_params={'ensure_ascii': False}, status=200)


# B. 결측치 처리 후 데이터 반환
def handle_missing_data(request):
    # CSV 파일의 경로 설정
    csv_file = os.path.join('data', 'test_data_has_null.CSV')
    # CSV 파일 읽기
    df = pd.read_csv(csv_file, encoding='euc-kr')
    # 결측치를 "NULL"로 치환
    df.fillna("NULL", inplace=True)
    # '나이' 필드를 정수로 변환 (NULL 값을 제외하고)
    df.loc[df['나이'] != "NULL", '나이'] = df.loc[df['나이'] != "NULL", '나이'].astype(int)
    # 결과를 딕셔너리 리스트로 변환
    data = df.to_dict('records')
    # JSON 응답으로 반환
    return JsonResponse({'data': data}, json_dumps_params={'ensure_ascii': False}, status=200)


# C. 알고리즘 구현하기(평균 나이와 가장 비슷한 10명)
def find_similar_age(request):
    # CSV 파일의 경로 설정
    # csv_file = os.path.join('data', 'test_data_has_null.CSV')
    # CSV 파일 읽기
    # df = pd.read_csv(csv_file, encoding='euc-kr')

    # 함수 호출마다 파일을 읽어오면 비효율적이기 때문에 전역으로 파일을 읽어오고 그 데이터를 복사하여 사용
    df = global_df.copy()
    # '나이' 필드의 결측치를 제외한 평균값 계산
    avg_age = df['나이'].mean(skipna=True)
    # 각 행의 '나이'와 평균 나이의 차이를 절대값으로 취한 새로운 필드 생성
    df['diff'] = abs(df['나이'] - avg_age)
    # age_diff 필드를 기준으로 오름차순 정렬하고, 상위 10개의 행만 선택
    result_df = df.nsmallest(10, 'diff')
    # '나이' 필드를 정수로 변환
    result_df['나이'] = result_df['나이'].astype(int)
    # 결과를 딕셔너리 리스트로 변환하여 JSON 응답으로 반환
    data = result_df.to_dict('records')
    return JsonResponse({'data': data}, json_dumps_params={'ensure_ascii': False}, status=200)
