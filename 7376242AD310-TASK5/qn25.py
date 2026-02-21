class Inference:
    def run(self):
        pass

class FastInference(Inference):
    def run(self):
        print("Running fast inference")

class AccurateInference(Inference):
    def run(self):
        print("Running accurate inference")


i = FastInference()
i.run()