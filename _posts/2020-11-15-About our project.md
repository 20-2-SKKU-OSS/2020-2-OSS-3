---
layout: post
title: "About Our Project"
subtitle: "SKKU iCampus Auto Downloader"
date: 2020-11-15 18:22:00 +0900
background: '/img/posts/02.jpg'
---

# SKKU iCampus Auto Downloader
<https://github.com/trayo9852/skku_icampus_auto_downloader>

<img class="img-fluid" src="/2020-2-OSS-3/img/posts/icampus_front.png"/>


## What is this project?
---------------
프로젝트 이름 그대로 성균관대학교 아이캠퍼스(icampus.skku.edu)에서 강의를 다운 받아주는 프로그램이다.

아이캠퍼스 사이트에서 강의를 수강할 때 자유로운 spanning이 어렵고 시험기간과 같은 중요한 시기에 서버가 터지는 등 강의를 수강하는데 불편함이 많아 
기존에도 수동으로 직접 다운 받거나 강의 별로 chrome extension을 사용하여 다운 받는 방법들이 많이 사용되엇다.
그러나 이러한 방법들은 매 강의마다 사용자가 직접 강의를 재생하고 다운받아야 하며 다운받은 파일을 따로 정리 및 관리 해야하는 것이 매우 번거롭다.

해당 프로젝트는 이러한 불편점들을 해결하기 위해 해당 사용자가 수강하는 강좌들을 전부 자동으로 다운받고 강좌별 주차별로 다운받은 파일을 관리해주며 
매주 업데이트 되는 강좌들을 자동으로 다운 받아주는 All-in-one 솔루션을 제공한다.


## Current Status
------------------------
해당 프로젝트는 현재 browser automation 라이브러리인 selenium과 이를 proxy server와 연결하여 사용할 수 있는 라이브러리인 selenium-wire을 사용하여 구현되었으며 정상적으로 작동은 하나 현재 가장 기본적인 기능만 제공하며 작동한다. 또한 아직 사용자 계정에 대한 일반화가 되지 않아 수강하는 강좌의 class id를 직접 설정하여야 하고 UI를 제공하지 않는 등 일반적인 사용자가 사용하기 쉽지 않은 상태이다.


## Ways to improve
-------------------------
* 상세한 Documentation 및 사용법 제공
* 다양한 다운로드 옵션 추가 (다운받지 않은 교과목 선택, 다운 받을 주 선택, 등)
* CLI 및 UI를 추가하여 사용자 친화적인 UX 제공
* 간단한 ID, PW 입력만으로도 작동하도록 사용자 계정에 대한 일반화 시도
* canvas API 분석을 통해 browser automation에 대한 의존도 감소 및 작동 속도 개선
* 코드 개선 및 모듈화
* 다운 받은 강의를 cloud sync 기능 제공(gdrive, onedrive)
* 발생할 수 있는 저작권 문제에 대한 확실한 안내


## Dependencies
-------------------------
* python
* selenium
* selenium-wire
* chrome driver

