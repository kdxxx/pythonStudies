print("problem 1 --------------")

class Kareler():
    def __init__(self,max):
        self.max= max
        self.sayı = 1

    def __iter__(self):
        return self
    def __next__(self):
        if(self.sayı<=self.max):
            sonuc = self.sayı**2
            self.sayı+=1
            return sonuc
        else:
            self.sayı=1
            raise StopIteration

kareler = Kareler(5)
for i in kareler:
    print(i)


print("problem 2 ---------------")

def asal_mı(sayı):
    i=2
    while (i<sayı):
        if(sayı%i==0):
            return False
        i+=1
    return True

def asal_generator():
    i = 2
    while True:
        if(asal_mı(i)):
            yield i
        i+=1
for sayı in asal_generator():
    if(sayı>1000):
        break
    print(sayı)
