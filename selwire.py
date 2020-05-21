from seleniumwire import webdriver  # Import from seleniumwire
import time
import credentials
import parse_json
import dataPy

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

classList = ["4962", "5362", "6762", "7082", "7915", "9212", "5881"]

# login


def login(i):
    driver.get("https://icampus.skku.edu/login")
    driver.find_element_by_css_selector("#userid").send_keys(credentials.id[i])
    driver.find_element_by_css_selector(
        "#password").send_keys(credentials.pw[i])
    driver.find_element_by_css_selector("#btnLoginBtn").click()
    time.sleep(1)


def loadClass():
    driver.get("https://canvas.skku.edu/courses")
    classList = driver.find_element_by_css_selector(
        "#my_courses_table > tbody")
    classTags = driver.find_elements_by_tag_name("a")
    lists = []
    for cl in classTags:
        if(cl.get_attribute("title") and ("안전교육" not in cl.get_attribute("title"))):
            lists.append(cl.get_attribute("href").split("/")[-1])

    return lists


def getDB(classNum):
    url = "https://canvas.skku.edu/courses/"+classNum+"/external_tools/1"
    del driver.requests
    driver.get(url)
    classCode = driver.find_element_by_css_selector(
        "#breadcrumbs > ul > li:nth-child(2) > a > span").text
    classC = classCode[classCode.find(
        "_")+1:classCode.find("(")].replace("_", "-")
    classN = classCode[:classCode.find("_")]
    classT = classCode[classCode.rfind("(")+1:classCode.rfind(")")]
    print("")
    print(classC, classN, classT)
    db = driver.wait_for_request("allcomponents_db?").response.body
    week_data = driver.wait_for_request("sections_db?").response.body
    parse_json.parseClass(db.decode("utf-8"),
                          week_data.decode("utf-8"), classC, classN, classT)
    # print(parsed_db)


parse_json.loadCompleted()

login(0)
classList1 = loadClass()
if "2516" in classList1: classList1.remove("2516")
print(classList1)


for cl in classList1:
    getDB(cl)

login(1)

classList2 = loadClass()
if "2564" in classList2: classList2.remove("2564")
classList2 = set(classList2)-set(classList1)
print(classList2)

for cl in classList2:
    getDB(cl)

parse_json.writeCompleted()
