print("problem 1------------")
import os
for lokasyon,klasor_ad,dosya_ad in os.walk("C:\\"):
    for i in dosya_ad:
        if i.endswith(".txt"):
            with open("txt dosyaları.txt","a",encoding="utf-8") as file:
                file.write(i+"-------------"+"dosyanın yeri %s" %(lokasyon) +"\n")
        elif i.endswith(".pdf"):
            with open("pdf dosyaları.txt","a",encoding="utf-8") as file2:
                file2.write(i+"----------- dosyanın yeri %s"%(lokasyon)+"\n")

        elif i.endswith(".jpg"):
            with open("jpg dosyaları.txt","a",encoding="utf-8") as file3:
                file3.write(i+"---------------- dosyanın yeri %s"%(lokasyon)+"\n")
