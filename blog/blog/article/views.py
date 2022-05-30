from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        "numbers":[1,2,3,4,5,6],
    }
    #return HttpResponse("<h3>Ana Sayfa</h3>")
    return render(request,"index.html",context)

def abou(request):
    return render(request="about.html")