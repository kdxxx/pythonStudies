import os
from datetime import  datetime
print(dir(os))

print(os.getcwd())
os.chdir("C:/Users/user/Desktop")
print(os.getcwd())

for i in os.listdir():
    print(i)

os.mkdir("deneme1")
os.makedirs("deneme2/deneme3")


os.rmdir("deneme2/deneme3")
os.makedirs("deneme2/deneme3")
os.removedirs("deneme2/deneme3")


os.rename("test.txt","test2.txt")

print(os.stat("test2.txt"))
print(os.stat("test2.txt").st_mtime)
print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime))



print(os.walk("C:/Users/user/Desktop"))

for i in os.walk("C:/user/user/Desktop"):
    print(i)

for klasör_yolu, klasör_isimleri,dosya_isimleri in os.walk("C:/Users/90546/Desktop"):
    print("klasör yolu: ",klasör_yolu)
    print("klasör isimleri: ",klasör_isimleri)
    print("dosya isimleri: ",dosya_isimleri)
    print("------------------------")

for klasör_yolu, klasör_isimleri,dosya_isimleri in os.walk("C:/Users/90546/Desktop"):
    for i in dosya_isimleri:
        print(i)

for klasör_yolu, klasör_isimleri,dosya_isimleri in os.walk("C:/Users/90546/Desktop"):
    for i in dosya_isimleri:
        if(i.endswith(".txt")):
            print(i)
