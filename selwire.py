from seleniumwire import webdriver  # Import from seleniumwire
import time
import requests
import json

from user import *
import settings
import parse_json
import dataPy

# pre-setup for dev
# if devFlag set import login creds from credentials.py
# ADD "credentials.py" to gitignore
# Never upload raw id and pwd to repository
if settings.devFlag == True:
    import credentials

    user = User(credentials.sid, credentials.id, credentials.pw)
else:
    user = User(settings.sid, settings.id, settings.pw)


# login
def login(i):
    driver.get("https://icampus.skku.edu/login")
    driver.find_element_by_css_selector("#userid").send_keys(credentials.id[i])
    driver.find_element_by_css_selector(
        "#password").send_keys(credentials.pw[i])
    driver.find_element_by_css_selector("#btnLoginBtn").click()
    time.sleep(1)


# function for extracting user auth token should be written
def getToken(driver):
    pass


# function for automatically loading user's attending classes and canvas UID should be written
def getClassesAndUid(user):
    pass


# function for integrating selenium with getToken() and getClassesAndUid() for loading User data should be written
# This function will act as program entry point
def loadUser(driver, user):
    # 1.login with selenium
    # 2.extract auth token
    # 3.load classes and canvas uid
    pass

# After getClassesAndUid() is implemented, previous loadClass() function will be deprecated
def loadClass():
    driver.get("https://canvas.skku.edu/courses")
    classList = driver.find_element_by_css_selector(
        "#my_courses_table > tbody")
    classTags = driver.find_elements_by_tag_name("a")
    lists = []
    for cl in classTags:
        if (cl.get_attribute("title") and ("안전교육" not in cl.get_attribute("title"))):
            lists.append(cl.get_attribute("href").split("/")[-1])

    return lists


def getDB(classNum):
    url = "https://canvas.skku.edu/courses/" + classNum + "/external_tools/1"
    del driver.requests
    driver.get(url)
    classCode = driver.find_element_by_css_selector(
        "#breadcrumbs > ul > li:nth-child(2) > a > span").text
    classC = classCode[classCode.find(
        "_") + 1:classCode.find("(")].replace("_", "-")
    classN = classCode[:classCode.find("_")]
    classT = classCode[classCode.rfind("(") + 1:classCode.rfind(")")]
    print("")
    print(classC, classN, classT)
    db = driver.wait_for_request("allcomponents_db?").response.body
    week_data = driver.wait_for_request("sections_db?").response.body
    parse_json.parseClass(db.decode("utf-8"),
                          week_data.decode("utf-8"), classC, classN, classT)
    # print(parsed_db)


parse_json.loadCompleted()

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

login(0)
classList1 = loadClass()
# upper codes will be replaced by loadUser() after fully implemented

for cl in classList1:
    getDB(cl)

parse_json.writeCompleted()