from seleniumwire import webdriver  # Import from seleniumwire
import time
import credentials
import parse_json
import dataPy

# Create a new instance of the Firefox driver
driver= webdriver.Chrome()

classList = ["4962", "5362", "6762", "7082", "7915", "9212", "5881"]

#login
driver.get("https://icampus.skku.edu/login")
driver.find_element_by_css_selector("#userid").send_keys(credentials.id)
driver.find_element_by_css_selector("#password").send_keys(credentials.pw)
driver.find_element_by_css_selector("#btnLoginBtn").click()
time.sleep(1)

completeddata = None

def getDB(classNum):
    url = "https://canvas.skku.edu/courses/"+classNum+"/external_tools/1"
    del driver.requests
    driver.get(url)
    classCode = driver.find_element_by_css_selector("#breadcrumbs > ul > li:nth-child(2) > a > span").text
    classC = classCode[classCode.find("_")+1:classCode.find("(")].replace("_", "-")
    classN = classCode[:classCode.find("_")]
    classT = classCode[classCode.rfind("(")+1:classCode.rfind(")")]
    print("")
    print(classC, classN, classT)
    db = driver.wait_for_request("allcomponents_db?").response.body
    week_data = driver.wait_for_request("sections_db?").response.body
    parse_json.parseClass(db.decode("utf-8"), week_data.decode("utf-8"), classC, classN, classT)
    #print(parsed_db)


parse_json.loadCompleted()
for cl in classList:
    getDB(cl)

parse_json.writeCompleted()
#getVidlink("https://lcms.skku.edu/em/5e576266c0a25")
#input('Press Enter to exit')