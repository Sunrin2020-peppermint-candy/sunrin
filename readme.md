# (WIP) 물건 챙김 알리미
20과학창의재단 산출물 대회 선린인터넷고등학교 영재원 `박하사탕` 팀 산출물, `물건 챙김 알리미`입니다.
# 실행하기
## Repo Clone
```sh
git clone https://github.com/Sunrin2020-peppermint-candy/sunrin.git
cd sunrin
```

## 환경변수
날씨 정보를 가져오기 위해 [공공데이터포털 동네예보 조회서비스](https://data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15057682)의 `동네예보조회` OpenAPI를 사용하고 있습니다.
`.env.example` 파일을 복제하여 이름을 `.env`으로 바꾼 뒤, 발급받은 서비스키를 입력해주세요.  

## 의존성 라이브러리
- `requests`
- `python_dotenv`
- `tensorflow`
- Tensorflow Object Detection API ([공식 문서](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2.md) 또는 [이 글](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html) 참고)

## 실행하기
```sh
python ./main.py
```
