
print("problem 1")
liste =  ["345","sadas","324a","14","kemal"]
for element in liste:
    try:
        element = int(element)
        print(element)
    except:
        pass

print("problem 2")

def çift_mi(sayı):
    if(sayı%2==0):
        return sayı
    else:
        raise ValueError
liste2 = [55,6,5,9,77,88,6,9,11,2,0]
for i in liste2:
    try:
        print(çift_mi(i))
    except ValueError:
        pass
