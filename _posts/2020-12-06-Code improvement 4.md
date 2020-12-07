---
layout: post
title: "Code improvement 4"
subtitle: "Introducing multiprocessing to improve speed"
date: 2020-12-2 17:32:00 +0900
background: '/img/posts/02.jpg'
---

# Improved speed
 


## Problems in the Previous Version
---------------
이전 버전의 프로그램의 경우 영상을 하나하나 순차적으로 다운로드 받아서 속도 저하의 문제가 존재.
 




## update
------------------------
Multiprocessing을 도입하여 다운로드 속도 개선. (아이캠퍼스의 서버 상태에 따라 최대 4배의 속도 개선)
따라 최대 4개의 강의를 동시에 다운받을 수 있다.
  
  


## Detailed explanation
-------------------------
<img class="img-fluid" src="/2020-2-OSS-3/img/posts/Multi_code1.png"/>
<img class="img-fluid" src="/2020-2-OSS-3/img/posts/Multi_code2.png"/>
