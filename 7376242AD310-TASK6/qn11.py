import os

folder = "dataset"
if not os.path.exists(folder):
    os.mkdir(folder)
print("Folder ready")