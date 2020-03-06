import json
import xml.etree.ElementTree as ET
import dataPy
import requestPy


def testDB():
    with open("input.json", "r", encoding="utf-8-sig") as testdb:
        parseAssignment(testdb, "abcdef")


def loadCompleted():
    with open("complete.json", "r", encoding="utf-8-sig") as complete_file:
        dataPy.down_DB = json.load(complete_file, encoding="utf-8")


def writeCompleted():
    with open("complete.json", "w", encoding='UTF-8-sig') as write_file:
        write_file.write(json.dumps(dataPy.down_DB, ensure_ascii=False))


def findClass(classCode):
    for dict in dataPy.down_DB:
        if dict["classCode"] == classCode:
            return dict

    dataPy.down_DB.append(
        {"classCode": classCode, "classVids": []}
    )

    return findClass(classCode)


def loadClassVids(dic):
    l = dic["classVids"]
    rlist = []
    for item in l:
        rlist.append(item["content_id"])
    return rlist


def findDuplicate(db, content_id):
    pass


def parseAssignment(db, classCode):
    #site_data = json.loads(db)
    site_data = json.load(db)
    class_data = findClass(classCode)
    class_vids = class_data["classVids"]
    for item in class_vids:
        print(item["title"])
    class_vid_list = loadClassVids(class_data)
    work_list = []
    allowedType = ["screenlecture", "movie"]
    for item in site_data:
        try:
            if(item["commons_content"]["content_type"] in allowedType):
                if(item["commons_content"]["content_id"] not in class_vid_list):
                    item_parsed = {}
                    item_parsed.update({
                        "class_id": classCode,
                        "assignment_id": item["assignment_id"],
                        "component_id": item["component_id"],
                        "title": item["title"],
                        "date": item["unlock_at"][2:item["unlock_at"].find("T")].replace("-", ""),
                        "content_id": item["commons_content"]["content_id"],
                        "content_type": item["commons_content"]["content_type"],
                        "content_url": item["commons_content"]["view_url"],
                        "vid_urls": parseVidXml(requestPy.getPHP(item["commons_content"]["content_id"]))
                    })
                    class_vids.append(item_parsed)
                    work_list.append(item_parsed)

        except KeyError:
            pass

    return work_list


def parseVidXml(xml):
    #xml = xml.decode("utf-8")

    root = ET.fromstring(xml)
    vidlinks = []

    for url in root.iter('media_uri'):
        if ("_pseudo" not in url.text and url.text not in vidlinks):
            vidlinks.append(url.text)

    return vidlinks


loadCompleted()
testDB()
writeCompleted()

