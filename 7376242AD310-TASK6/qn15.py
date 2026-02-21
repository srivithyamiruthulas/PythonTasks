import sys

if sys.version_info < (3, 8):
    sys.exit("Unsupported Python version")
print("Version supported")