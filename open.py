
try:
    file = open("myfile2.txt", encoding="utf-8")
    s = file.readlines()
    file.close()
except FileNotFoundError:
    print("File not found")
