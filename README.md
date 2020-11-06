# WIP: skku_icampus_auto_downloader
성균관대 (신)icampus 자동 다운(동기화) 프로그램


## 개발 취지
시험기간만 되면 매번 서버가 터지고 가끔가다 수강 가능기간을 매우 짧게 설정되어있는 강의들이 있어서 강의를 수강하는데 많은 불편합이 있어 개발한 프로그램입니다.

## 개발 방향
매강의를 직접 손으로 다운받고 다운 받은 강의와 다운 받지 않은 강의를 구분하는 등 관리하기 힘들고 그렇다고 현재 존재하는 모든 강의를 다시 다 다운받는것도 낭비임으로 다운 받은 강의들을 리스팅하여 아이캠퍼스 서버와 one-way sync하는 방향으로 개발하였습니다.

## 개발 현황
python3에서 작동하며 현재 대부분의 기능이 작동되지만 매우 user friendly하지 않고 매우 account dependent하여 일반화 되어 있지 않으며 GUI등 많은 부분이 미흡한 상태입니다. 
또한 selenium-wire라는 라이브러리를 사용해 proxy dependent한 방법으로 임시 구현을 이부분을 개선할 필요가 있습니다.

## 사용법
1. dependencies와 chrome driver 설치
2. crendentials.py 파일을 생성후 아래와 같이 두개의 배열을 생성 및 저장
  ```
  id = [<사용자 아이디>]
  pw = [<사용자 비밀번호>]
  ```
3. selwire.py 실행

## Major Dependencies
+ chrome driver
+ selenium
+ selenium-wire
