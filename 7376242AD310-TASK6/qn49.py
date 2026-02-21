class Processor:
    def process(self):
        pass

class ImageProcessor(Processor):
    def process(self):
        print("Processing image")

p = ImageProcessor()
p.process()