import json
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen, Request
import datetime
from bs4 import BeautifulSoup
from datetime import timedelta, time

from Tutoring import apiKey

now = datetime.datetime.now()

fullDate = now.strftime('%Y%m%d')

print(fullDate)

before_one_day = now - timedelta(days=1)

before_one_day = before_one_day.strftime('%Y%m%d')

print(before_one_day)

nowDate = now.strftime('%m%d')

filename = 'ir105' + '_' + nowDate

# filename = 'vi006' + '_' + nowDate

print(nowDate)

url = 'http://apis.data.go.kr/1360000/SatlitImgInfoService/getInsightSatlit'

# ServiceKey = Decoding 인증키 사용

# 기상청 위성영상 천리안 위성조회서비스

queryParams = '?' + urlencode({ quote_plus('ServiceKey') : apiKey.key, quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('dataType') : 'JSON', quote_plus('sat') : 'G2', quote_plus('data') : 'ir105', quote_plus('area') : 'ko', quote_plus('time') : before_one_day })

request = Request(url + queryParams)

request.get_method = lambda: 'GET'

response_body = urlopen(request, timeout=60).read() # get bytes data

data = json.loads(response_body) # convert bytes data to json

print(data)

with open('./'+ filename + '.json', 'w', encoding='utf-8') as file :
    json.dump(data, file, ensure_ascii=False, indent='\t')
