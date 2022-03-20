import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()
mesaj["From"] = "someone.gmail.com"
mesaj["To"] = "someone.gmail.com"
mesaj["Subject"] = "Smtp mail gönderme"

yazi = """

Stmp ile mail gönderdin.

someone

"""

mesaj_gövdesi = MIMEText(yazi,"plain")
mesaj.attach(mesaj_gövdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("","")
    """mail ve şifre girilecek sırayla"""
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    print("mail gönderildi")
    mail.close()
except:
    sys.stderr.write("hata var ")
    sys.stderr.flush()
