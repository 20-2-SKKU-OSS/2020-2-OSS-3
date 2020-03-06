import requests

def getPHP(contentID):
    response = requests.get("https://lcms.skku.edu/viewer/ssplayer/uniplayer_support/content.php?content_id="+contentID)
    return response.text

