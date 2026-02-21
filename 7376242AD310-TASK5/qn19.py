class Model:
    def train(self):
        print("Training model...")

class LinearRegression(Model):
    def predict(self):
        print("Predicting using Linear Regression")

class DecisionTree(Model):
    def predict(self):
        print("Predicting using Decision Tree")


m = DecisionTree()
m.train()
m.predict()