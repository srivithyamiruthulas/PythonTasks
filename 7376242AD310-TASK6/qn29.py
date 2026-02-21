class Media:
    def play(self):
        pass

class MP3(Media):
    def play(self):
        print("Playing MP3")

m = MP3()
m.play()