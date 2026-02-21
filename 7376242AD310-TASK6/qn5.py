class Model:
    def predict(self, x):
        pass

class LinearModel(Model):
    def predict(self, x):
        print("Prediction:", x * 2)

model = LinearModel()
model.predict(5)