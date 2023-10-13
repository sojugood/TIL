from django.shortcuts import render, redirect, get_object_or_404
from .models import Keyword, Trend
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import matplotlib.pyplot as plt
from io import BytesIO
import base64
plt.switch_backend('Agg')


# Create your views here.
def keyword(request):
    keywords = Keyword.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        keyword = Keyword(name=name)
        keyword.save()
        return redirect('keyword')
    context = {
        'keywords': keywords,
    }
    return render(request, 'keyword.html', context)


def keyword_detail(request, pk):
    keyword = get_object_or_404(Keyword, pk=pk)
    Trend.objects.filter(name=keyword.name).delete()
    keyword.delete()
    return redirect('keyword')


def crawling(request):
    # 모든 Keyword 객체를 가져온다.
    keywords = Keyword.objects.all()

    if len(keywords) == 0:
        context = {
            'message': '키워드를 입력해주세요!'
        }
    else:
        # Chrome 옵션 생성
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        
        # 각 키워드에 대하여 크롤링을 수행한다.
        for keyword in keywords:
            url = f'https://www.google.com/search?q={keyword.name}'

            driver = webdriver.Chrome(options=chrome_options)
            driver.get(url)

            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            result_stats = soup.select_one("div#result-stats")
            text = result_stats.text
            
            # 정규 표현식을 사용하여 숫자만을 추출한다.
            number = int(''.join(re.findall(r'[\d,]+', text)).replace(',', ''))
            
            # Trend 테이블에 검색 결과를 저장한다.
            # 이미 저장되어 있는 키워드는 새로 생성하지 않고 검색 결과 개수를 변경한다.
            # result는 null 값을 허용하지 않기에 최초 객체 생성 시 기본값 할당해준다.
            trend, created = Trend.objects.get_or_create(name=keyword.name, search_period="all", defaults={'result': 0})
            trend.result = number
            trend.save()

            driver.quit()

        trends = Trend.objects.filter(search_period="all")  # Trend 테이블에서 모든 객체를 불러옴

        context = {
            'trends': trends,  # trends를 context에 추가
        }

    return render(request, 'crawling.html', context)


def crawling_histogram(request):
    trends = Trend.objects.filter(search_period="all")
    names = [trend.name for trend in trends]
    results = [trend.result for trend in trends]

    if len(trends) == 0:
        context = {
            'message': '키워드를 입력해주세요!'
        }
    else:
        plt.clf()

        plt.figure(figsize=(8, 5))
        plt.bar(names, results, align='center', label='Trends')
        plt.grid(True)
        plt.xlabel('Keyword')
        plt.ylabel('Result')
        plt.title('Technology Trend Analysis')
        plt.legend()

        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
        buffer.close()

        context = {
            'chart_image': f'data:image/png;base64,{image_base64}',
        }

    return render(request, 'crawling_histogram.html', context)


def crawling_advanced(request):
    keywords = Keyword.objects.all()

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    
    for keyword in keywords:
        # "지난 1년" 을 기준으로 필터링하는 부분 "&tbs=qdr:y" 를 추가
        url = f'https://www.google.com/search?q={keyword.name}&tbs=qdr:y'

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        result_stats = soup.select_one("div#result-stats")
        text = result_stats.text
        
        number = int(''.join(re.findall(r'[\d,]+', text)).replace(',', ''))
        
        # search_period 에 year 로 저장
        trend, created = Trend.objects.get_or_create(name=keyword.name, search_period="year", defaults={'result': 0})
        trend.result = number
        trend.save()

        driver.quit()

    # 지난 1년 필터링
    trends = Trend.objects.filter(search_period="year")

    names = [trend.name for trend in trends]
    results = [trend.result for trend in trends]

    if len(trends) == 0:
        context = {
            'message': '키워드를 입력해주세요!'
        }
    else:
        plt.clf()

        plt.figure(figsize=(8, 5))
        plt.bar(names, results, align='center', label='Trends')
        plt.grid(True)
        # max_value = max(results) * 1.05
        # plt.ylim(0, max_value)
        plt.xlabel('Keyword')
        plt.ylabel('Result')
        plt.title('Technology Trend Analysis')
        plt.legend()

        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
        buffer.close()

        context = {
            'chart_image': f'data:image/png;base64,{image_base64}',
        }

    return render(request, 'crawling_advanced.html', context)