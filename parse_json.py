import json
import xml.etree.ElementTree as ET
import dataPy
import requestPy


def koreanJson(fname):
    with open(fname, "r", encoding="utf-8-sig") as korean:
        aa = json.load(korean, encoding="utf-8")

    with open(fname, "w", encoding="utf-8-sig") as kk:
        kk.write(json.dumps(aa, ensure_ascii=False))


def testDB():
    global aaa
    with open("input.json", "r", encoding="utf-8-sig") as testdb:
        parseClass(testdb, aaa, "12345", "수업명", "교수명")


def loadCompleted():
    try:
        with open("complete.json", "r", encoding="utf-8-sig") as complete_file:
            dataPy.down_DB = json.load(complete_file, encoding="utf-8")
    except json.decoder.JSONDecodeError:
        dataPy.down_DB = []
        
    with open("complete_bak.json", "w", encoding='UTF-8-sig') as write_file:
        write_file.write(json.dumps(dataPy.down_DB, ensure_ascii=False))

def writeCompleted():
    with open("complete.json", "w", encoding='UTF-8-sig') as write_file:
        write_file.write(json.dumps(dataPy.down_DB, ensure_ascii=False))


def findClass(classCode, className, professor):
    for dict in dataPy.down_DB:
        if dict["classCode"] == classCode:
            return dict

    dataPy.down_DB.append(
        {"classCode": classCode, "className": className,
            "professor": professor, "classVids": {}}
    )

    return findClass(classCode, className, professor)


# def loadClassVids(dic):
#     l = dic["classVids"]
#     rlist = []
#     for item in l:
#         rlist.append(item["content_id"])
#     return rlist


def findDuplicate(db, content_id):
    pass


def parseWeekdata(week_data, parsed_dict):
    data = {}
    key_list = list(parsed_dict.keys())
    for week in week_data:
        week_num = (week["title"][:week["title"].find("주")])
        week_id = 1
        data[week_num] = []
        week["subsections"].sort(key=lambda s: s["position"])  # position 기준 정렬
        for subsection in week["subsections"]:
            subsection["units"].sort(key=lambda s: s["position"])
            for unit in subsection["units"]:
                unit["components"].sort(key=lambda s: s["position"])
                for component in unit["components"]:
                    if(str(component["component_id"]) in key_list):
                        data[week_num].append(str(component["component_id"]))
                        parsed_dict[str(component["component_id"])]["week_id"] = week_num+"-"+str(week_id)
                        week_id += 1
    return data


def parseClass(db, week_db, classCode, className, professor):
    site_data = json.loads(db)
    w_data = json.loads(week_db)
    # site_data = json.load(db)  # 강의 정보
    # w_data = json.load(week_db)

    class_data = findClass(classCode, className, professor)  # 해당 분반 전체 json
    class_vids = class_data["classVids"]  # 해당 분반 저장된 강의 json

    parsed_dict = {}  # 전체 json화
    work_dict = {} #작업 필요한 주 json
    allowedType = ["screenlecture", "movie", "everlec"]  # 허용 강의 타입

    for item in site_data:
        try:
            if(item["commons_content"]["content_type"] in allowedType):
                item_parsed = {}
                item_parsed.update({
                    "assignment_id": item["assignment_id"],
                    "component_id": item["component_id"],
                    "title": item["title"],
                    "date": item["unlock_at"][2:item["unlock_at"].find("T")].replace("-", ""),
                    "content_id": item["commons_content"]["content_id"],
                    "content_type": item["commons_content"]["content_type"],
                    "content_url": item["commons_content"]["view_url"],
                    "vid_urls": getVidUrl(requestPy.getPHP(item["commons_content"]["content_id"]))
                })
                # class_vids.append(item_parsed)
                parsed_dict[str(item["component_id"])] = item_parsed

        except KeyError:
            pass

    week_data = parseWeekdata(w_data, parsed_dict)  # 주차 정보

    for week in list(week_data.keys()):
        # 사이트에도 정보가 없는 경우 패스
        if(not week_data[week]):
            continue

        workFlag = False
        for component in week_data[week]:
            try:
                if(class_vids[week][component] != parsed_dict[component]):
                    workFlag = True

            except KeyError:
                workFlag = True
                break

        if(workFlag):
            class_vids.pop(week, None)
            class_vids[week] = {}
            work_dict[week] = {}
            for component in week_data[week]:
                class_vids[week][component] = parsed_dict[component]
                work_dict[week][component] = parsed_dict[component]

    requestPy.downloadWeek(classCode, className, professor, work_dict)
    writeCompleted()

def getVidUrl(xml):
    #xml = xml.decode("utf-8")

    root = ET.fromstring(xml)
    vidlinks = []

    for url in root.iter('media_uri'):
        if ("_pseudo" not in url.text and "mobile" not in url.text and url.text not in vidlinks):
            vidlinks.append(url.text)

    if(not vidlinks):
        for url in root.iter('media_uri'):
            if ("_pseudo" not in url.text and url.text not in vidlinks):
                vidlinks.append(url.text)

    return vidlinks


# with open("section.json", "r", encoding="utf-8-sig") as aaa:
#     loadCompleted()
#     testDB()
#     writeCompleted()
# koreanJson("input.json")
