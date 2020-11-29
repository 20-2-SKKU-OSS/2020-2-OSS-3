import pprint

class User:
    """ class to store user credentials
    studentID, loginID, PW should be given at initialization
    studentID: integer
    id: string
    pw: string

    헤더랑 쿠키는 인증 정보 저장 및 핸들링
    classes는 이번학기에 수강중인 과목 id 저장
    classDatas는 위의 과목 교수님 이름 교과목 명(id 말고 text) 등등 저장 학수번호 저장
    show는 디버깅용으로 출력하는 메소드


    """
    def __init__(self, studentID: int, id: str, pw: str):
        self.sid = studentID
        self.id = id
        self.pw = pw
        self.headers = {}
        self.cookies = {}
        self.classes = []
        self.classDatas = {}
        self.uid = ""

    def show(self):
        pprint.pprint(vars(self))
