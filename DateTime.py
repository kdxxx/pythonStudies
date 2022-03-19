from datetime import datetime


"""
import locale
locale.setlocale(locale.LC_ALL,"")
to make local for language etc
"""

su_an = datetime.now()
print(su_an)
print(su_an.year)
print(su_an.month)
print(su_an.hour)

print(datetime.strftime(su_an,"%Y"))
print(datetime.strftime(su_an,"%B"))
print(datetime.strftime(su_an,"%D"))
print(datetime.strftime(su_an,"%Y %B"))
print(datetime.strftime(su_an,"%Y %B %A"))
print(datetime.strftime(su_an,"%Y %B %a"))


saniye = datetime.timestamp(su_an)
print(saniye)
su_an2 = datetime.fromtimestamp(saniye)
print(su_an2)

su_an = datetime.fromtimestamp(0)
print(su_an)

tarih = datetime(2019,12,1)
su_an3 = datetime.now()
print(tarih- su_an3)

