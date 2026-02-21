class Storage:
    def upload(self):
        pass

class AWS(Storage):
    def upload(self):
        print("Uploaded to AWS")

s = AWS()
s.upload()