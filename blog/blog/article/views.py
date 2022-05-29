from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("<h3>Ana Sayfa</h3>")
    return render(request,"article/index.html")