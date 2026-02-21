class Storage:
    def __init__(self, size):
        self.size = size

class FreePlan(Storage):
    def limit(self):
        return 100  # MB

class ProPlan(Storage):
    def limit(self):
        return 1000  # MB


s = FreePlan(50)
print("Storage Limit:", s.limit(), "MB")