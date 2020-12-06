---
layout: post
title: "Code improvement3"
subtitle: "Speed is improved by more than 2 times"
date: 2020-12-6 18:22:00 +0900
background: '/img/posts/02.jpg'
---

# Improved speed & Reduced dependence



## Problems in the Previous Version
---------------
기존에는 selenium과 proxy를 사용하여 traffic capture를 사용하여 작동하기 떄문에 속도가 저하됨.



## update
------------------------
따라서 Session sharing을 통한 direct request를 통해 browser automation에 대한 의존도를 감소시키고 작동 속도 개선.



## Detailed explanation
-------------------------
<img class="img-fluid" src="/2020-2-OSS-3/img/posts/code_img1.png"/>

getContentDB()와 getWeekDB()를 추가하여 direct request를 통해 browser automation에 대한 의존도를 감소.
