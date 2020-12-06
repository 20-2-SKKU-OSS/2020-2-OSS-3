# WIP: skku_icampus_auto_downloader

성균관대 (신)icampus 자동 다운(동기화) 프로그램



- [WIP: skku_icampus_auto_downloader](#wip-skku_icampus_auto_downloader)
  - [개발 배경](#개발-배경)
    - [개발 취지](#개발-취지)
    - [개발 방향](#개발-방향)
    - [개발 현황](#개발-현황)
  - [사용법](#사용법)
  - [Repository Structure](#repository-structure)
  - [Major dependencies](#major-dependencies)
  - [저작권 관련 사항](#저작권-관련-안내-사항)
---

## 개발 배경
### 개발 취지
시험 기간만 되면 매번 서버가 터지고 가끔 가다 수강 가능 기간이 매우 짧게 설정되어있는 강의들이 있어서 강의를 수강하는데 많은 불편함이 있어 개발한 프로그램입니다.

### 개발 방향
매 강의를 직접 손으로 다운 받고 다운 받은 강의와 다운 받지 않은 강의를 구분하는 등 관리하기 힘들고, 그렇다고 현재 존재하는 모든 강의를 다시 다 다운 받는 것도 낭비이므로 다운 받은 강의들을 리스팅하여 아이캠퍼스 서버와 one-way sync하는 방향으로 개발하였습니다.



### 개발 현황
python3에서 작동하며 현재 대부분의 기능이 작동되지만 매우 user friendly하지 않고, 매우 account dependent하여 일반화 되어 있지 않으며, GUI 등 많은 부분이 미흡한 상태입니다. 또한 selenium-wire라는 라이브러리를 사용해 proxy dependent한 방법으로 임시 구현을 이 부분을 개선할 필요가 있습니다.

---

## 사용법
#### 1. dependency 설치
    pip install selenium selenium-wire

####  2. [chromedriver](https://chromedriver.chromium.org/downloads) 설치
   - 위 링크를 통해 Chrome 버전, OS에 맞게 chromedriver 다운로드 및 설치
     - Chrome 버전 확인: 크롬 우측 상단의 메뉴 버튼 > 도움말 > Chrome 정보
   - selwire.py와 같은 경로에 chromedriver.exe 추가
   
#### 3. selwire.py와 같은 경로에 crendentials.py 파일 생성
   
#### 4. selwire.py의 내용에 아래와 같이 세 개의 배열 추가 및 저장
    
    sid = [<사용자 학번>]
    id = [<사용자 아이디>]
    pw = [<사용자 비밀번호>]
    
#### 5. selwire.py 실행
    python selwire.py

---

## Repository Structure

```bash
.
├── slide
│   └── OSS_3조_발표_초안.pptx
├── dataPy.py
├── parse_json.py
├── requestPy.py
├── selwire.py
├── settings.py
├── user.py
├── .gitignore
└── README.md
```

## Major dependencies
+ chromedriver
+ selenium
+ selenium-wire

---

## 저작권 관련 안내 사항
해당 프로젝트를 사용함에 있어서 저작권 부분에서 발생할 문제를 우려하는 사용자들을 위해, 저작권 관련 안내 사항을 다음과 같이 공지합니다.
+ 개인이 지불하여 구매/대여한 저작물을 개인의 범위 안에서 공유하지 않고 개인적으로 사용하는 것은 저작권법에 저촉되지 않습니다.
+ 개인이 구매/대여한 저작물 사용을 돕는 프로그램을 “판매”하는 것은 문제의 소지가 있으나 “공유” 하는 것은 문제가 되지 않습니다.
+ 성균관대학교 규정상 사용자의 ID, 비밀번호가 사용자 기기 밖(서버)로 유출될 시 개인정보보호 규정상 위배가 되나 해당 프로그램은 사용자의 개인정보를 사용자의 기기 밖으로 유출하지 않으므로 규정에 저촉되지 않습니다.
+ 수강 기간 만료 후에 강의를 소지하는 것은 성균관대학교와 사용자 간의 계약 위반이며 법적으로 문제가 되지는 않습니다. 또한 이때 외부로 공유하지 않는 이상 성균관대학교에서 사용자의 강의 소지를 증빙할 수 없으므로 문제가 되지 않을 것으로 사료됩니다.
+ 모든 책임은 해당 프로젝트를 사용하기로 선택하고 사용한 사용자에게 있습니다.

---

## Updates
#### 1. 로그인만으로 작동
  이전 버전은 사용자 계정에 맞게 여러 설정을 하여야 사용이 가능하지만, 별도의 설정 없이 로그인 만으로 작동하도록 일반화 업데이트 완료.
#### 2.의존도 감소 및 속도개선
  Session sharing을 통한 direct request를 통해 browser automation에 대한 의존도를 감소시키고 작동 속도 개선
