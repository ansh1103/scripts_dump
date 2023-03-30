import os

filename = "d:/New folder/pythonProject/ScriptsDump/Python"
if os.path.exists(filename) and os.path.isdir(filename):
    print("File Exits")
else:
    print("File doesn't exits")