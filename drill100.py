

import os

for file in os.listdir("C:\\A\\"):
    if file.endswith(".txt"):
        path = os.path.join("C:\\A\\", file)
        mtime = os.path.getmtime(path)
        print(file, mtime)

