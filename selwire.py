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
    """
     Extract user authentication tokens(cookies) from selenium(web browser)

     By analysis on canvas API, we found out that 3 kinds of auth token is mainly used
     - xn_api_token: used as Bearer token in http request header
     - uid: user id on canvas requested as url params
     - _normandy_session: usef for initial auth token until xn_api_token is loaded

     xn_api_token is not fully loaded until we enter at least 1 course page
     Therefore, we should visit course page with selenium in advance before extracting cookies from selenium
     Since this procedure is done in advance of loading classes we will just simply visit
     first class that appears on the list when clicking class list page.

     UID can be extracted automaticly when loading class so UID will be dealt by getClassesAndUid()
    """
    
    # 1. load any class with selenium
    driver.get("https://canvas.skku.edu/courses")
    item = driver.find_element_by_css_selector(
        "#my_courses_table > tbody > tr:nth-child(1) > td.course-list-course-title-column.course-list-no-left-border > a")
    cid = item.get_attribute("href").split("/")[-1]
    url = "https://canvas.skku.edu/courses/" + cid + "/external_tools/1"
    driver.get(url)

    header = {}
    cook = {}
    # 2. extract tokens from browser cookies
    cookies = driver.get_cookies()
    for cookie in cookies:
        # extract xn_api_token
        if (cookie["name"] == "xn_api_token"):
            header["Authorization"] = "Bearer " + cookie["value"]
        # extract _normandy_seesion
        if (cookie["name"] == '_normandy_session'):
            cook["_normandy_session"] = cookie['value']
    # 3. return extracted tokens as header and cookie
    return header, cook


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