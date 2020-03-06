from seleniumwire import webdriver  # Import from seleniumwire
import time
import credentials
import parse_json
import dataPy

# Create a new instance of the Firefox driver
driver= webdriver.Chrome()

classList = ["4692", "5362", "6762", "7082", "7915", "9212", "5881"]

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
    classCode = classCode[classCode.find("_")+1:classCode.find("(")].replace("_", "-")
    db = driver.wait_for_request("allcomponents_db?").response.body
    parsed_db = parse_json.parseAssignment(db, classCode)
    print(parsed_db)

def getVidlink(content_url):
    del driver.requests
    driver.get(content_url)
    vid = driver.wait_for_request("content.php?").response.body
    parse_json.parseVidXml(vid)



parse_json.loadCompleted()
print(dataPy.down_DB)


#getDB("4962")
#getVidlink("https://lcms.skku.edu/em/5e576266c0a25")
#input('Press Enter to exit')