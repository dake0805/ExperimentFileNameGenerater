class User:
    studentId = ""
    name = ""
    classId = ""

    def __init__(self, studentId, name, classId):
        self.studentId = studentId
        self.name = name
        self.classId = classId

    def to_dict(self):
        dict = {'studentId': self.studentId, 'name': self.name, 'classId': self.classId}
        return dict
