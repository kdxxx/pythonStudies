import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open("mail.txt","r",encoding="utf-8") as file:
    for i in file:
        i = i[:-1]
        liste = i.split(",")
        ad = liste[0]
        email = liste[1]
        mesaj = MIMEMultipart()
        mesaj["From"] = "gönderceğin email adresi"
        mesaj["To"] = email
        mesaj["Subject"] = "email"
        yazı = "this is a trial message"
        mesaj_govdesi = MIMEText(ad+yazı,"plain")
        mesaj.attach(mesaj_govdesi)

        try:
            mail = smtplib.SMTP("smtp.live.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login("login","password")
            mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
            print("Email gönderildi")
            mail.close()
        except:
            print("hata var")
