#
# try:
#     file = open("myfile2.txt", encoding="utf-8")
#     s = file.readlines()
#     file.close()
# except FileNotFoundError:
#     print("File not found")

with open("myfile.txt", 'a+') as file:
    file.seek(0)
    print(file.readlines())




