import json

def parseAssignment(db):
    db = db.decode("utf-8")
    data = json.loads(db)
    for item in data:
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
        print(item_parsed)