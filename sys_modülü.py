import sys

print(dir(sys))
a = int(input("a: "))
b = int(input("b: "))
sys.exit()
c = int(input("c: "))

sys.stderr.write("bu bir hata mesajı\n")
sys.stderr.flush()
sys.stdout.write("bu bir normal mesaj\n")

for i in sys.argv:
    print(i)


def kok_bulma(a,b,c):
    delta = b**2-4*a*c
    if(delta<0):
        print("reel kök yok")
    else:
        x1 = (-b-delta**0.5)/(2*a)
        x2 = -b+delta**0.5/(2*a)
        return (x1,x2)

if len(sys.argv) == 4:
    print("kök bulma: ",kok_bulma(int(sys.argv[1],sys.argv[2],sys.argv[3])))
else:
    sys.stderr.write("Doğru değerler girin")
    sys.stderr.flush()
