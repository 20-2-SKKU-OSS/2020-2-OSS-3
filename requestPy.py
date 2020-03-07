import requests
import os
import shutil

base_dir = "C:\\Users\\Jaeyoon\\Desktop\\0.3학년 1학기\\ㅎ.인강\\"


def getPHP(contentID):
    response = requests.get(
        "https://lcms.skku.edu/viewer/ssplayer/uniplayer_support/content.php?content_id="+contentID)
    return response.text


def downloadLecture(urls):
    pass

def rcDir(d):
    removeDir(d)
    while(os.path.exists(d)):pass
    os.makedirs(d)

def removeDir(d):
    if(os.path.exists(d)):
        shutil.rmtree(d)

def createDir(d):
    if(not os.path.exists(d)):
        os.makedirs(d)


def getFileType(url):
    return "."+url.split(".")[-1]


def downloadWeek(classCode="SWE3003-43", className="데이터베이스개론", professor="김응모", workload={
    "1": {
        "298624": {
            "assignment_id": 15546,
            "component_id": 298624,
            "title": "26312PC_SWE300342_1_1_03050905_Ch1",
            "date": "200301",
            "content_id": "5e4e16cf060ec",
            "content_type": "movie",
            "content_url": "https://lcms.skku.edu/em/5e4e16cf060ec",
            "vid_urls": [
                "https://lcms.skku.edu:58443/contents/skku100001/5e4e16cf060ec/contents/media_files/media/ssmovie.mp4"
            ],
            "week_id": "1-1"
        },
        "298632": {
            "assignment_id": 15550,
            "component_id": 298632,
            "title": "26312PC_SWE300342_1_2_03071034_Ch1",
            "date": "200301",
            "content_id": "5e4e111e701a0",
            "content_type": "movie",
            "content_url": "https://lcms.skku.edu/em/5e4e111e701a0",
            "vid_urls": [
                "https://lcms.skku.edu:58443/contents/skku100001/5e4e111e701a0/contents/media_files/media/ssmovie.mp4"
            ],
            "week_id": "1-2"
        }
    }
}):
    class_dir = base_dir + classCode+" "+className+"("+professor+")"
    createDir(class_dir)

    for week in list(workload.keys()):
        week_dict = workload[week]
        week_dir = class_dir + "//" + classCode+" "+week+"주차"
        rcDir(week_dir)

        for lecture in list(week_dict.keys()):
            content = week_dict[lecture]
            fname = content["week_id"]+"_"

            if(len(content["vid_urls"]) == 1):
                fname = fname+content["title"] + \
                    getFileType(content["vid_urls"][0])
                print(fname)
            else:
                pass

downloadWeek()
