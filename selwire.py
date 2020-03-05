from seleniumwire import webdriver  # Import from seleniumwire
import time
import credentials
import parse_json
import xml.etree.ElementTree as ET

# Create a new instance of the Firefox driver
driver= webdriver.Chrome()

classList = ["4692", "5362", "6762", "7082", "7915", "9212", "5881"]

#login
driver.get("https://icampus.skku.edu/login")
driver.find_element_by_css_selector("#userid").send_keys(credentials.id)
driver.find_element_by_css_selector("#password").send_keys(credentials.pw)
driver.find_element_by_css_selector("#btnLoginBtn").click()
time.sleep(1)

def getDB(classNum):
    url = "https://canvas.skku.edu/courses/"+classNum+"/external_tools/1"
    del driver.requests
    driver.get(url)
    classCode = driver.find_element_by_css_selector("#breadcrumbs > ul > li:nth-child(2) > a > span").text
    classCode = classCode[classCode.find("_")+1:classCode.find("(")].replace("_", "-")
    print(classCode)
    db = driver.wait_for_request("allcomponents_db?").response.body
    parse_json.parseAssignment(db)

def getVidlink(content_url):
    del driver.requests
    driver.get(content_url)
    vid = driver.wait_for_request("content.php?").response.body
    print(vid)

getDB("9212")
#getVidlink("https://lcms.skku.edu/em/5e5784cd77e59")
input('Press Enter to exit')