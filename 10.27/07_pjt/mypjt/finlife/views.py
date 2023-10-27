from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.http import JsonResponse
import requests
from .serializers import DepositProductsSerializer, DepositOptionsSerializer
from .models import DepositProducts, DepositOptions

BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

# Create your views here.
@api_view(['GET'])
def api_test(request):
    url = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(url, params=params).json()
    return Response(response)


@api_view(['GET'])
def save_deposit_products(request):
    url = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(url, params=params).json()
    baseList = response.get('result').get('baseList')
    optionList = response.get('result').get('optionList')
    DepositProducts.objects.all().delete()
    DepositOptions.objects.all().delete()
    # 상품 데이터 저장
    for product_data in baseList:
        product_serializer = DepositProductsSerializer(data=product_data)
        if product_serializer.is_valid(raise_exception=True):
            product_serializer.save()

    # 옵션 데이터 저장
    for option_data in optionList:
        product = DepositProducts.objects.get(fin_prdt_cd=option_data.get('fin_prdt_cd'))
        options_serializer = DepositOptionsSerializer(data=option_data)
        if options_serializer.is_valid(raise_exception=True):
            options_serializer.save(product=product)
    return JsonResponse({ 'message': 'okay' })


@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data)
    else:
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    options = DepositOptions.objects.filter(product=product)
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def top_rate(request):
    top_option = DepositOptions.objects.order_by('-intr_rate2').first()
    product = top_option.product
    # 상품과 관련된 모든 옵션을 가져옵니다.
    product_options = DepositOptions.objects.filter(product=product)

    product_serializer = DepositProductsSerializer(product)
    options_serializer = DepositOptionsSerializer(product_options, many=True)

    return Response({
        'product': product_serializer.data,
        'options': options_serializer.data
    })