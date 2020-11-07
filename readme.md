# (WIP) 물건 챙김 알리미
20과학창의재단 산출물 대회 선린인터넷고등학교 영재원 박하사탕 팀 산출물, `물건 챙김 알리미`입니다.
# 실행하기
## Repo Clone
```sh
git clone https://github.com/Sunrin2020-peppermint-candy/sunrin.git
cd sunrin
```
## 의존성 라이브러리 설치
Python 의존성 라이브러리를 관리하기 위해 [Poetry](https://python-poetry.org/)를 사용하고 있습니다.  
Poetry를 설치한 후 다음 명령어를 실행해주세요.
```sh
poetry install
```
## GUI 실행하기
```sh
poetry run python ./프로젝트.py
```
## 날씨 정보 모듈 실행하기
날씨 정보는 [공공데이터포털 동네예보 조회서비스](https://data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15057682)의 `동네예보조회` OpenAPI를 사용하고 있습니다.
`.env.example` 파일을 복제하여 이름을 `.env`으로 바꾼 뒤, 발급받은 서비스키를 입력해주세요.  
이후 다음 명령어를 실행하시면 됩니다.
```sh
poetry run python ./weather.py
```
