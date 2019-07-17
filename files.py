import os
import time

dir_path = os.path.dirname(os.path.realpath(__file__))

for entry in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, entry)):
        print(entry)


print("File name: ",__file__)
print("Size: ",os.path.getsize(__file__))


