import requests
from dotenv import load_dotenv
import os
import datetime


load_dotenv()

BASE_URL = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst"
SERVICE_KEY = os.getenv("WEATHER_SERVICE_KEY")
DATA_TYPE = "JSON"

NULL_DATA = {"value": "NULL"}

# 맑음(1), 구름많음(3), 흐림(4)
SKY_CODE = {
    "1": "맑음",
    "3": "구름많음",
    "4": "흐림",
}

# 없음(0), 비(1), 비/눈(2), 눈(3), 소나기(4), 빗방울(5), 빗방울/눈날림(6), 눈날림(7)
PTY_CODE = {
    "0": "없음",
    "1": "비",
    "2": "비/눈",
    "3": "눈",
    "4": "소나기",
    "5": "빗방울",
    "6": "빗방울/눈날림",
    "7": "눈날림",
}


def getVilageFcst(date, time, nx, ny):
    requestUrl = (
        "{}?serviceKey={}&dataType={}&base_date={}&base_time={}&nx={}&ny={}".format(
            BASE_URL, SERVICE_KEY, DATA_TYPE, date, time, nx, ny
        )
    )

    r = requests.get(requestUrl)

    result = r.json()["response"]

    if result["header"]["resultCode"] != "00":
        print(
            "ERROR! CODE: {}, MESSAGE: {}".format(
                result["header"]["resultCode"], result["header"]["resultMsg"]
            )
        )
        return

    result = dict(
        map(
            lambda item: (
                item["category"],
                {
                    "value": item["fcstValue"],
                    "date": item["fcstDate"],
                    "time": item["fcstTime"],
                },
            ),
            result["body"]["items"]["item"],
        )
    )

    return result

def print_useful_data(result):
    print("강수 확률:", result["POP"]["value"])
    print("강수 형태:", PTY_CODE[result["PTY"]["value"]])
    print("하늘 상태:", SKY_CODE[result["SKY"]["value"]])
    print(
        "풍속:",
        result.get("VVV", NULL_DATA).get("value"),
        result.get("UUU", NULL_DATA).get("value"),
    )


def is_umbrella_required():
    result = getVilageFcst(getTodayDate(), getNearTime(), 61, 121)
    return int(result["POP"]["value"]) > 50


def getTodayDate():
    return datetime.date.today().strftime("%Y%m%d")


def getNearTime():
    now = datetime.datetime.now()

    hour = now.hour
    minute = now.minute
    time = hour * 100 + minute

    # - Base_time : 0200, 0500, 0800, 1100, 1400, 1700, 2000, 2300 (1일 8회)
    # - API 제공 시간(~이후) : 02:10, 05:10, 08:10, 11:10, 14:10, 17:10, 20:10, 23:10
    if time >= 2310:
        return "2300"
    elif time >= 2010:
        return "2000"
    elif time >= 1710:
        return "1700"
    elif time >= 1410:
        return "1400"
    elif time >= 1110:
        return "1100"
    elif time >= 810:
        return "0800"
    elif time >= 510:
        return "0500"
    elif time >= 210:
        return "0200"
    else:
        # TOOD: ERROR
        return "0000"


if __name__ == "__main__":
    result = getVilageFcst(getTodayDate(), getNearTime(), 61, 129)

    print_useful_data(result)

    print(is_umbrella_required())

    print("현재 공개된 가장 최근의 시간코드:", getNearTime())
