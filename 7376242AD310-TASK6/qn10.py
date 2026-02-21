from datetime import datetime

class Experiment:
    def start(self):
        self.start_time = datetime.now()
        print("Started at", self.start_time)

    def end(self):
        self.end_time = datetime.now()
        print("Ended at", self.end_time)

exp = Experiment()
exp.start()
exp.end()