from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("<h3>Ana Sayfa</h3>")
    return render(request,"index.html")

def abou(request):
    return render(request="about.html")