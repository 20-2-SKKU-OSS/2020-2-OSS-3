import json
import xml.etree.ElementTree as ET
import dataPy

def loadCompleted():
    with open("complete.json", "r") as complete_file:
        dataPy.down_DB = json.load(complete_file)

def writeCompleted():
    with open("complete.json", "w") as write_file:
        json.dump(dataPy.down_DB, write_file)

def findClass(classCode):
    for dict in dataPy.down_DB:
        if dict["classCode"] == classCode:
            return dict

def findDuplicate(db, content_id):
    pass

def parseAssignment(db, classCode):
    db = db.decode("utf-8")
    data = json.loads(db)
    parsed_data = []
    allowedType = ["screenlecture", "movie"]
    for item in data:
        try:
            if(item["commons_content"]["content_type"] in allowedType):
                item_parsed = {}
                item_parsed.update({
                    "assignment_id": item["assignment_id"],
                    "component_id": item["component_id"],
                    "title": item["title"],
                    "date": item["unlock_at"][2:item["unlock_at"].find("T")].replace("-",""),
                    "content_id": item["commons_content"]["content_id"],
                    "content_type": item["commons_content"]["content_type"],
                    "content_url": item["commons_content"]["view_url"]
                })
                
                parsed_data.append(item_parsed)
        except KeyError:
            pass

    return parsed_data

def parseVidXml(xml):
    xml = xml.decode("utf-8")
    root = ET.fromstring(xml)
    vidlinks =[]

    for url in root.iter('media_uri'):
        if ("_pseudo" not in url.text and url.text not in vidlinks):
            vidlinks.append(url.text)

    print(vidlinks)

loadCompleted()
a = findClass("123456")
a["classVids"].append({"test":"test1234"})
writeCompleted()
