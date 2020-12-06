import requests
import os
import shutil
import sys
import time
from multiprocessing.pool import ThreadPool

from threading import Event, Thread
from tkinter import Tk, ttk
from urllib.request import urlretrieve
import settings # 다운로드 파일 경로 설정

base_dir = "D:\\test_downloader\\"

if settings.downloadDir:
    base_dir = settings.downloadDir
else:
    base_dir = "D:\\test_downloader\\"

def getPHP(contentID):
    response = requests.get(
        "https://lcms.skku.edu/viewer/ssplayer/uniplayer_support/content.php?content_id="+contentID)
    return response.text


def downloadLecture(urls):
    pass


def downloader(arguments):

    link = arguments[0]
    file_name = arguments[1]

    if("/[MEDIA_FILE]") in link:
        print("Media-file Error")
        return

    response = requests.get(link, stream=True)
    if(response.status_code ==  404):
        print ('err')
        return
    start = time.perf_counter()
    with open(file_name, "wb") as f:
        print ("Downloading %s" % file_name)
        response = requests.get(link, stream=True)
        total_length = int(response.headers.get('content-length'))
        #print (response.headers["content-type"])
        #print (total_length / 1024/1024, "mb")

        if total_length is None:  # no content length header
            f.write(response.content)
        else:
            dl = 0
            for data in response.iter_content(chunk_size=4096):
                
                f.write(data)
                
            if(f.tell()/total_length < 0.95):
                print(file_name+ "-"+link+ "fsize error")

            ##print(f.tell()/1024/1024,"mb")
    print("complete %s" % file_name)


def shell(a,b,c):
    try:
        urlretrieve(a, b, c)
    except Exception as e:
        print(e)

def rcDir(d):
    try:
        removeDir(d)
        while(os.path.exists(d)):
            pass
        os.makedirs(d)

    except:
        print("del_err")
        pass


def removeDir(d):
    if(os.path.exists(d)):
        shutil.rmtree(d)


def createDir(d):
    if(not os.path.exists(d)):
        os.makedirs(d)


def getFileType(url):
    return "."+url.split(".")[-1]


def searchSubstring(sub, mylist):
    return next((s for s in mylist if sub in s), None)


def downloadWeek(classCode, className, professor, workload):
    class_dir = base_dir + classCode+" "+className+"("+professor+")"
    createDir(class_dir)

    for week in list(workload.keys()):

        # only download desired week
        try:
            l = len(settings.week)
            if (l == 1):
                if (int(week) < settings.week[0]):
                    continue
            elif (l > 0):
                if (int(week) not in settings.week):
                    continue
        except:
            pass

        # print downloading week info
        print("")
        print(classCode+" "+className+" week"+week)
        print("-"*100)

        week_dict = workload[week]
        week_dir = class_dir + "\\" + classCode+" "+week+"주차\\"
        rcDir(week_dir)

        '''
            - 기존 구현 사항: 강의 순차적으로 다운로드
            - 개선 방향: 강좌 별 다운로드 할 영상 모아서 멀티프로세싱 구현
            (구현 예정이며 현재 구현을 위한 준비 단계)
        '''
        work_list = []

        for lecture in list(week_dict.keys()):
            content = week_dict[lecture]
            vids = content["vid_urls"]
            title = content["title"].replace(":", " ")
            title = content["title"].replace("/", "of")
            fname = content["week_id"]+"_"+title
            filename = ""

            if(len(content["vid_urls"]) == 1):
                filename = fname + \
                    getFileType(content["vid_urls"][0])
                #print(filename)
                 # downloader(content["vid_urls"][0], week_dir+filename)
                work_list.append([content["vid_urls"][0], week_dir+filename])

            elif(searchSubstring("_camera", vids)):
                for vid in vids:
                    if("camera" in vid):
                        filename = fname + "-camera" + getFileType(vid)
                        # downloader(vid, week_dir+filename)
                        work_list.append([vid, week_dir+filename])
                    elif("screen" in vid):
                        filename = fname + "-screen" + getFileType(vid)
                        #print(filename)
                        # downloader(vid, week_dir+filename)
                        work_list.append([vid, week_dir + filename])

            else:
                for vid in vids:
                    filename = fname + "-" + vid.split("/")[-1]
                    #print(filename)
                    # downloader(vid, week_dir+filename)
                    work_list.append([vid, week_dir + filename])

        # 멀티프로세싱 구현을 위함 (추후 수정 예정)
        # implemented multi threading
        p = ThreadPool(4)
        p.map(downloader, work_list)
        p.close()
        p.join()