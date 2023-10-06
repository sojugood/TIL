from django.shortcuts import render
import pandas as pd
csv_path = 'weathers/data/austin_weather.csv'
import matplotlib.pyplot as plt
from io import BytesIO
import base64
plt.switch_backend('Agg')


def index(request):
    return render(request, 'base.html')


def problem1(request):
    df = pd.read_csv(csv_path)

    context = {
        'df': df,
    }
    
    return render(request, 'problem1.html', context)


def problem2(request):
    df = pd.read_csv(csv_path)
    # 날짜 필드 : 날짜 형식으로 변환
    df['Date'] = pd.to_datetime(df['Date'])

    plt.clf()

    plt.figure(figsize=(8,5))
    plt.plot(df['Date'], df['TempHighF'], label='High Temperature')
    plt.plot(df['Date'], df['TempAvgF'], label='Avg Temperature')
    plt.plot(df['Date'], df['TempLowF'], label='Low Temperature')
    plt.grid(True)
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.legend()

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }

    return render(request, 'problem2.html', context)


def problem3(request):
    df = pd.read_csv(csv_path)
    # 날짜 필드 : 날짜 형식으로 변환
    df['Date'] = pd.to_datetime(df['Date'])
    # 온도 필드 : 숫자 형식으로 변환
    df['TempHighF'] = pd.to_numeric(df['TempHighF'], errors='coerce')
    df['TempAvgF'] = pd.to_numeric(df['TempAvgF'], errors='coerce')
    df['TempLowF'] = pd.to_numeric(df['TempLowF'], errors='coerce')

    temp_df = df[['Date', 'TempHighF', 'TempAvgF', 'TempLowF']]
    temp_df = temp_df.set_index('Date').resample('M').mean()

    plt.clf()

    plt.figure(figsize=(8,5))
    plt.plot(temp_df.index, temp_df['TempHighF'], label='High Temperature')
    plt.plot(temp_df.index, temp_df['TempAvgF'], label='Avg Temperature')
    plt.plot(temp_df.index, temp_df['TempLowF'], label='Low Temperature')
    plt.grid(True)
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.legend(loc=4)

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }

    return render(request, 'problem3.html', context)


from collections import Counter
import numpy as np

def problem4(request):
    df = pd.read_csv(csv_path)

    # 이벤트 발생하지 않은 경우(공백) -> No Events로 이름 지정
    df['Events'].replace(' ', 'No Events', inplace=True)

    events_counter = Counter()
    for events in df['Events']:
        lst = [event.strip() for event in events.split(',')]
        events_counter.update(lst)

    # 기상 현상과 발생 횟수 리스트 생성(발생 횟수 기준으로 내림차순 정렬)
    sorted_items = sorted(events_counter.items(), key=lambda x: x[1], reverse=True)
    events, counts = zip(*sorted_items)

    plt.clf()

    # 히스토그램 그리기
    plt.figure(figsize=(8,5))
    y_pos = np.arange(len(events))
    plt.bar(y_pos, counts, align='center', alpha=0.5, color='blue')
    plt.xticks(y_pos, events)
    plt.grid(True)
    plt.xlabel('Events')
    plt.ylabel('Count')
    plt.title('Event Counts')

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }

    return render(request, 'problem4.html', context)