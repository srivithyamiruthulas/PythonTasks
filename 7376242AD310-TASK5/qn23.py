class Attendance:
    def mark(self, name):
        pass

class Manual(Attendance):
    def mark(self, name):
        print(name, "marked present manually")

class FaceRecognition(Attendance):
    def mark(self, name):
        print(name, "marked present using Face Recognition")


a = Manual()
a.mark("Sri")