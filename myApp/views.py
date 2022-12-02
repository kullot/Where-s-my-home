from django.shortcuts import render
# 추가
from django.http import HttpResponse
# 추가
import csv
import os
import pandas as pd
import numpy as np
# 데이타프레임의 컬럼을 10컬럼까지 모두 표시
pd.set_option('display.max_columns', 10)
# 추가
import json
import requests
# 추가 데이타베이스 연동
from .models import N_apartment
# 소스 수정
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup


def index(request):
    return HttpResponse("<h1>부산 재건축 아파트 5조 프로젝트</h1>")

def sub1_1(request):
    # csv => 데이타프레임 => 넘파이 => 리스트 => 컨텍스트 => 웹페이지
    df = pd.read_csv('myApp/data/final_final.csv', encoding='cp949')
    # arr = df.to_numpy()
    # data_list = arr.tolist()
    arr = df.to_numpy()
    data_list = arr.tolist()

    context = {
                'data_list' : data_list
                }
    return render(request, 'myApp/sub1.html', context)

def apartment(request):
    # csv => 데이타프레임 => 넘파이 => 리스트 => 컨텍스트 => 웹페이지
    df = pd.read_csv('myApp/data/final_final.csv', encoding='cp949')
    # arr = df.to_numpy()
    # data_list = arr.tolist()
    arr = df.to_numpy()
    data_list = arr.tolist()
    dictionary = {i[0]: i[1:] for i in data_list}
    data_list = []

    for i, k in dictionary.items():
        data_list.append([i]+k)

    context = {
                'data_list' : data_list
                }
    return render(request, 'myApp/apartment.html', context)    
            


def home(request):

    return render(request, 'myApp/home.html')

def home_1(request):
    
# csv => 데이타프레임 => 넘파이 => 리스트 => 컨텍스트 => 웹페이지
    df = pd.read_csv('myApp/data/final_final.csv', encoding='cp949')
    # arr = df.to_numpy()
    # data_list = arr.tolist()
    arr = df.to_numpy()
    data_list = arr.tolist()

    data_list_list = []
    for i in data_list:
        if '강서구' in i[2]:
            data_list.append(i)

    context = {
                'data_list_list' : data_list_list
                }
    return render(request, 'myApp/home_1.html', context)

def home_2(request):
    
# csv => 데이타프레임 => 넘파이 => 리스트 => 컨텍스트 => 웹페이지
    df = pd.read_csv('myApp/data/final_final.csv', encoding='cp949')
    # arr = df.to_numpy()
    # data_list = arr.tolist()
    arr = df.to_numpy()
    data_list = arr.tolist()

    data_list_list = []
    for i in data_list:
        if '사하구' in i[2]:
            data_list.append(i)

    context = {
                'data_list_list' : data_list_list
                }
    return render(request, 'myApp/home_2.html', context)

def home_3(request):
    
# csv => 데이타프레임 => 넘파이 => 리스트 => 컨텍스트 => 웹페이지
    df = pd.read_csv('myApp/data/final_final.csv', encoding='cp949')
    # arr = df.to_numpy()
    # data_list = arr.tolist()
    arr = df.to_numpy()
    data_list = arr.tolist()

    data_list_list = []
    for i in data_list:
        if '사상구' in i[2]:
            data_list.append(i)

    context = {
                'data_list_list' : data_list_list
                }
    return render(request, 'myApp/home_3.html', context)

def home_4(request):
    
# csv => 데이타프레임 => 넘파이 => 리스트 => 컨텍스트 => 웹페이지
    df = pd.read_csv('myApp/data/final_final.csv', encoding='cp949')
    # arr = df.to_numpy()
    # data_list = arr.tolist()
    arr = df.to_numpy()
    data_list = arr.tolist()

    data_list_list = []
    for i in data_list:
        if '북구' in i[2]:
            data_list_list.append(i)

    context = {
                'data_list_list' : data_list_list
                }
    return render(request, 'myApp/home_4.html', context)

def home_5(request):
    
# csv => 데이타프레임 => 넘파이 => 리스트 => 컨텍스트 => 웹페이지
    df = pd.read_csv('myApp/data/final_final.csv', encoding='cp949')
    # arr = df.to_numpy()
    # data_list = arr.tolist()
    arr = df.to_numpy()
    data_list = arr.tolist()

    data_list_list = []
    for i in data_list:
        if '중구' in i[2]:
            data_list_list.append(i)

    context = {
                'data_list_list' : data_list_list
                }
    return render(request, 'myApp/home_5.html', context)

def home_6(request):
    
# csv => 데이타프레임 => 넘파이 => 리스트 => 컨텍스트 => 웹페이지
    df = pd.read_csv('myApp/data/final_final.csv', encoding='cp949')
    # arr = df.to_numpy()
    # data_list = arr.tolist()
    arr = df.to_numpy()
    data_list = arr.tolist()

    data_list_list = []
    for i in data_list:
        if '동구' in i[2]:
            data_list_list.append(i)

    context = {
                'data_list_list' : data_list_list
                }
    return render(request, 'myApp/home_6.html', context)

def home_7(request):
    
# csv => 데이타프레임 => 넘파이 => 리스트 => 컨텍스트 => 웹페이지
    df = pd.read_csv('myApp/data/final_final.csv', encoding='cp949')
    # arr = df.to_numpy()
    # data_list = arr.tolist()
    arr = df.to_numpy()
    data_list = arr.tolist()

    data_list_list = []
    for i in data_list:
        if '서구' in i[2]:
            data_list_list.append(i)

    context = {
                'data_list_list' : data_list_list
                }
    return render(request, 'myApp/home_7.html', context)

def home_8(request):
    
# csv => 데이타프레임 => 넘파이 => 리스트 => 컨텍스트 => 웹페이지
    df = pd.read_csv('myApp/data/final_final.csv', encoding='cp949')
    # arr = df.to_numpy()
    # data_list = arr.tolist()
    arr = df.to_numpy()
    data_list = arr.tolist()

    data_list_list = []
    for i in data_list:
        if '남구' in i[2]:
            data_list_list.append(i)

    context = {
                'data_list_list' : data_list_list
                }
    return render(request, 'myApp/home_8.html', context)

def home_9(request):
    
# csv => 데이타프레임 => 넘파이 => 리스트 => 컨텍스트 => 웹페이지
    df = pd.read_csv('myApp/data/final_final.csv', encoding='cp949')
    # arr = df.to_numpy()
    # data_list = arr.tolist()
    arr = df.to_numpy()
    data_list = arr.tolist()

    data_list_list = []
    for i in data_list:
        if '영도구' in i[2]:
            data_list_list.append(i)

    context = {
                'data_list_list' : data_list_list
                }
    return render(request, 'myApp/home_9.html', context)

def home_10(request):
    
# csv => 데이타프레임 => 넘파이 => 리스트 => 컨텍스트 => 웹페이지
    df = pd.read_csv('myApp/data/final_final.csv', encoding='cp949')
    # arr = df.to_numpy()
    # data_list = arr.tolist()
    arr = df.to_numpy()
    data_list = arr.tolist()

    data_list_list = []
    for i in data_list:
        if '부산진구' in i[2]:
            data_list_list.append(i)

    context = {
                'data_list_list' : data_list_list
                }
    return render(request, 'myApp/home_10.html', context)

def home_11(request):
    
# csv => 데이타프레임 => 넘파이 => 리스트 => 컨텍스트 => 웹페이지
    df = pd.read_csv('myApp/data/final_final.csv', encoding='cp949')
    # arr = df.to_numpy()
    # data_list = arr.tolist()
    arr = df.to_numpy()
    data_list = arr.tolist()

    data_list_list = []
    for i in data_list:
        if '수영구' in i[2]:
            data_list_list.append(i)

    context = {
                'data_list_list' : data_list_list
                }
    return render(request, 'myApp/home_11.html', context)

def home_12(request):
    
# csv => 데이타프레임 => 넘파이 => 리스트 => 컨텍스트 => 웹페이지
    df = pd.read_csv('myApp/data/final_final.csv', encoding='cp949')
    # arr = df.to_numpy()
    # data_list = arr.tolist()
    arr = df.to_numpy()
    data_list = arr.tolist()

    data_list_list = []
    for i in data_list:
        if '연제구' in i[2]:
            data_list_list.append(i)

    context = {
                'data_list_list' : data_list_list
                }
    return render(request, 'myApp/home_12.html', context)

def home_13(request):
    
# csv => 데이타프레임 => 넘파이 => 리스트 => 컨텍스트 => 웹페이지
    df = pd.read_csv('myApp/data/final_final.csv', encoding='cp949')
    # arr = df.to_numpy()
    # data_list = arr.tolist()
    arr = df.to_numpy()
    data_list = arr.tolist()

    data_list_list = []
    for i in data_list:
        if '동래구' in i[2]:
            data_list_list.append(i)

    context = {
                'data_list_list' : data_list_list
                }
    return render(request, 'myApp/home_13.html', context)

def home_14(request):
    
# csv => 데이타프레임 => 넘파이 => 리스트 => 컨텍스트 => 웹페이지
    df = pd.read_csv('myApp/data/final_final.csv', encoding='cp949')
    # arr = df.to_numpy()
    # data_list = arr.tolist()
    arr = df.to_numpy()
    data_list = arr.tolist()

    data_list_list = []
    for i in data_list:
        if '금정구' in i[2]:
            data_list_list.append(i)

    context = {
                'data_list_list' : data_list_list
                }
    return render(request, 'myApp/home_14.html', context)

def home_15(request):
    
# csv => 데이타프레임 => 넘파이 => 리스트 => 컨텍스트 => 웹페이지
    df = pd.read_csv('myApp/data/final_final.csv', encoding='cp949')
    # arr = df.to_numpy()
    # data_list = arr.tolist()
    arr = df.to_numpy()
    data_list = arr.tolist()

    data_list_list = []
    for i in data_list:
        if '해운대구' in i[2]:
            data_list_list.append(i)

    context = {
                'data_list_list' : data_list_list
                }

    return render(request, 'myApp/home_15.html', context)

def home_16(request):
    
# csv => 데이타프레임 => 넘파이 => 리스트 => 컨텍스트 => 웹페이지
    df = pd.read_csv('myApp/data/final_final.csv', encoding='cp949')
    df[['층']] = df[['층']].astype(int)
    # arr = df.to_numpy()
    # data_list = arr.tolist()
    arr = df.to_numpy()
    data_list = arr.tolist()

    data_list_list = []
    for i in data_list:
        if '기장군' in i[2]:
            data_list_list.append(i)

    context = {
                'data_list_list' : data_list_list
                }
    return render(request, 'myApp/home_16.html', context)

def apartment111(request):
    # 테이블모델명.objects.all()
    apartment_list = N_apartment.objects.all()
    return HttpResponse(apartment_list)
    # 딕셔너리 구조로 만들어서 html 문서에 전달
    # context = {'city_list':city_list}
    # return render(request, 'myApp/city.html', context)

#myApp/views.py

# /myApp/search/ 주소와 연결되는 뷰함수
def search(request):
    return render(request, 'myApp/home/search.html')


# /myApp/searchCon/ 주소와 연결되는 뷰함수
def searchCon(request):
    # 폼에서 GET방식으로 전달받은 데이타를 변수에 저장
    search_word = request.GET['search']

    # 결과리스트명 = 테이블명.objects.filter(필드명__icontains=search_word)
    apartment_list = N_apartment.objects.filter(name__icontains=search_word)
    print('=' * 50)
    print(search_word, city)

    # 딕셔너리 구조로 만들어서 html 문서에 전달
    context = {'apartment_list': apartment_list}

    return render(request, 'myApp/search_result.html', context)


import matplotlib.pyplot as plt


def graph_1(request):
# csv => 데이타프레임 => 넘파이 => 리스트 => 컨텍스트 => 웹페이지
    df = pd.read_csv('myApp/data/final_final.csv', encoding='cp949')

    test_df = final[(final['아파트명'].str.contains('삼익')) & (final['건축일'].str.contains('1978'))& (final['면적'].str.contains('78.31')) ] 
    a = plt.figure(figsize = (20,5))
    plt.plot(test_df['거래일자'], test_df['실거래가(만원)'], label= 'deal_day' )
    plt.scatter(test_df['거래일자'], test_df['실거래가(만원)'], label= 'deal_day' )
    plt.legend()
    plt.show()


    
    context = {
                'data_list_list' : a
                }

    return render(request, 'myApp/graph_1.html', context)

def search(request):
    
    return render(request, 'myApp/search.html')

# /myApp/searchCon/ 주소와 연결되는 뷰함수
def searchCon(request):
    # 폼에서 GET방식으로 전달받은 데이타를 변수에 저장
    search_word1 = request.GET['sellist1']
    search_word2 = request.GET['sellist2']
    search_word3 = request.GET['sellist3']
    url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
    # params ={'serviceKey' : '서비스키', 'pageNo' : '1', 'numOfRows' : '10', 'LAWD_CD' : '11110', 'DEAL_YMD' : '201512' }
    params ={'serviceKey' : 'Yhq6n9vlpaKZsCOw0jec8zIdZ8p+Bpuku6WLjVgDhqXRW6dHnfXoauSEj19jpnjv59CUGspyTxVCgCeXOua7dg==', 
             'pageNo' : '1', 
             'numOfRows' : '50', 
             'LAWD_CD' : search_word3[-5:], 
             'DEAL_YMD' : str(search_word1)+str(search_word2) }

    response = requests.get(url, params=params)
    xml_str = response.text

    # 3) xml 텍스트 => soup 객체
    soup = BeautifulSoup(xml_str, 'xml')

    target_list = soup.find_all('item')
    apartment_list = []
    for item in target_list:
        deal_amount = item.거래금액.text
        build_year = item.건축년도.text
        if item.도로명:
            road_name = item.도로명.text
        else:
            road_name = ''

        if item.도로명건물본번호코드:
            road_name_bonbun= item.도로명건물본번호코드.text
        else:
            road_name_bonbun = ''


        dong = item.법정동.text
        apartment_name = item.아파트.text
        area = item.전용면적.text
        floor = item.층.text
        jibun = item.지번.text
        deal_day = item.년.text + '.' + item.월.text + '.' + item.일.text
        apartment_list.append({'apartment_name' : apartment_name,  
                               'build_year' : build_year,
                               'area' : area, 
                               'floor' : floor, 
                               'dong' : dong,
                               'road_name' : road_name,
                               'road_name_bonbun': road_name_bonbun,
                               'jibun' : jibun,
                               'deal_amount' : deal_amount,
                               'deal_day' : deal_day
                              })
    apartment_list = pd.DataFrame(apartment_list)
    arr = apartment_list.to_numpy()
    data_list = arr.tolist()
    context = {
                'data_list' : data_list
                }

    return render(request, 'myApp/data.html', context)