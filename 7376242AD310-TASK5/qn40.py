import datetime

class ExecutionTime:
    def finish(self):
        return datetime.datetime.now()


print("Program running...")
e = ExecutionTime()
print("Finished at:", e.finish())