import requests
from dotenv import load_dotenv
import os
import datetime


load_dotenv()

BASE_URL = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'
SERVICE_KEY = os.getenv('WEATHER_SERVICE_KEY')
DATA_TYPE='JSON'


def getVilageFcst(date, time, nx, ny):
  requestUrl = '{}?serviceKey={}&dataType={}&base_date={}&base_time={}&nx={}&ny={}'.format(BASE_URL, SERVICE_KEY, DATA_TYPE, date, time, nx, ny)

  # print(requestUrl)

  r = requests.get(requestUrl)

  result = r.json()['response']

  if result['header']['resultCode'] != '00':
    print('ERROR! CODE: {}, MESSAGE: {}'.format(result['header']['resultCode'], result['header']['resultMsg']))
    return

  result = dict(map(lambda item: (item['category'], item['fcstValue']), result['body']['items']['item']))
  print(result)


  return result

def getTodayDate():
  return datetime.date.today().strftime('%Y%m%d')

if __name__ == "__main__":
  getVilageFcst(getTodayDate(), '0500', 60, 126)