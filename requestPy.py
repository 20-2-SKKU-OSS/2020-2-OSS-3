import requests
import os
import shutil
import sys
import time

from threading import Event, Thread
from tkinter import Tk, ttk
from urllib.request import urlretrieve

base_dir = "D:\\test_downloader\\"


def getPHP(contentID):
    response = requests.get(
        "https://lcms.skku.edu/viewer/ssplayer/uniplayer_support/content.php?content_id="+contentID)
    return response.text


def downloadLecture(urls):
    pass


def downloader(link, file_name):
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
        print (total_length / 1024/1024, "mb")

        if total_length is None:  # no content length header
            f.write(response.content)
        else:
            dl = 0
            for data in response.iter_content(chunk_size=4096):
                #dl += len(data)
                f.write(data)
                # done = int(50 * dl / total_length)
                # sys.stdout.write("\r[%s%s] %s bps" % (
                #     '=' * done, ' ' * (50-done), dl//(time.perf_counter() - start)))
                # sys.stdout.flush()
            if(f.tell()/total_length < 0.95):
                print(file_name+ "-"+link+ "fsize error")

            print(f.tell()/1024/1024,"mb")

# def downloader(url, filename):
#     root = progressbar = quit_id = None
#     ready = Event()

#     def reporthook(blocknum, blocksize, totalsize):
#         nonlocal quit_id
#         if blocknum == 0:  # started downloading
#             def guiloop():
#                 nonlocal root, progressbar
#                 root = Tk()
#                 root.withdraw()  # hide
#                 progressbar = ttk.Progressbar(root, length=400)
#                 progressbar.grid()
#                 # show progress bar if the download takes more than .5 seconds
#                 root.after(500, root.deiconify)
#                 ready.set()  # gui is ready
#                 root.mainloop()
#                 root.quit()
#             Thread(target=guiloop).start()
#         ready.wait(1)  # wait until gui is ready
#         percent = blocknum * blocksize * 1e2 / totalsize  # assume totalsize > 0
#         if quit_id is None:
#             root.title('%%%.0f %s' % (percent, filename,))
#             progressbar['value'] = percent  # report progress
#             if percent >= 100:  # finishing download
#                 quit_id = root.after(0, root.destroy)  # close GUI

#     return shell(url, filename, reporthook)


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
        week_dict = workload[week]
        week_dir = class_dir + "\\" + classCode+" "+week+"주차\\"
        rcDir(week_dir)

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
                print(filename)
                downloader(content["vid_urls"][0], week_dir+filename)

            elif(searchSubstring("_camera", vids)):
                for vid in vids:
                    if("camera" in vid):
                        filename = fname + "-camera" + getFileType(vid)
                        print(filename)
                        downloader(vid, week_dir+filename)
                    elif("screen" in vid):
                        filename = fname + "-screen" + getFileType(vid)
                        print(filename)
                        downloader(vid, week_dir+filename)

            else:
                for vid in vids:
                    filename = fname + "-" + vid.split("/")[-1]
                    print(filename)
                    downloader(vid, week_dir+filename)

