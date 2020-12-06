---
layout: post
title: "Code improvement1"
subtitle: "Works just by login without any additional settings"
date: 2020-12-2 17:32:00 +0900
background: '/img/posts/02.jpg'
---

# Update Availability




## Problems in the Previous Version
---------------
프로그램을 사용하여 영상들을 다운 받기 위해서는, 사용자 계정에 맞는 설정을 직접 코드 수정을 통해 해주어야만 사용이 가능했다. 
따라서 사용자들에 따라 직접 코드를 수정해야 하기 떄문에 일반화하여 사용하기 어렵다는 단점이 존재했다. 
 




## Update
------------------------
여러 사용자의 계정에 테스트하여 별도의 설정 없이 로그인만으로 작동하도록 일반화 함.
 



## Ways to improve
-------------------------
1. user.py 에 user class를 추가
2. user의 token들을 추출. (getToken함수)
3. user의 즐겨찾기 목록을 통해 수강하는과목들의 정보를 추출.
 



## Detailed explanation
-------------------------

* 2.user의 token들을 추출. (getToken함수)
  
  Selenium을 통한 웹 브라우저에서 사용자 인증 토큰 (쿠키) 추출 결과.
  
  Canvas API 분석을 통해 다음 3가지 인증 토큰이 주로 사용되고 있음을 알 수 있었다.
    - xn_api_token : http 요청 헤더에서 Bearer 토큰으로 사용
    - uid : URL 매개 변수로 요청 된 캔버스의 사용자 ID
    - normandy_session : xn_api_token이로드 될 때까지 초기 인증 토큰을 위한 usef
 
  (추가적인 설명)
 
  xn_api_token은 적어도 하나의 강의 페이지를 입력 할 때까지 완전히로드되지 않는다. 따라서 selenium에서 쿠키를 추출하기 전에 임의의 강의 페이지를 미리 방문해야한다. 이 절차는 강의를 load하기전에 수행되기 때문에, 강의 목록 페이지를 클릭하면 목록에 나타나는 첫 번째 클래스를 방문하도록 하였다. 강의를 Load 할 때 UID를 자동으로 추출 할 수 있으므로 UID는 getClassesAndUid ()에 의해 처리된다.



* 3.user의 즐겨찾기 목록을 통해 수강하는과목들의 정보를 추출.

  코로나로 인해 전체 온라인 강의가 되면서, 수강하는 과목에 이전 강의 들까지 모두 포함이 되어 현재 학기에 수강하는 과목들만 추출해 내는 부분이 문제점이었다. 따라서 해당하는 교과목 아이디(학수번호랑 다름)을 직접 사용자가 넣어야 불필요한 강의를 받지 않을 수 있었다. 하지만 학교 측에서 "즐겨찾기" 목록을 이번 학기에 수강하는 목록으로 바꿔줘서 canvas가 즐겨찾기를 불러오는 방법을 분석하여 구현했다.
