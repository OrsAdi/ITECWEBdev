from django.shortcuts import render

# Create your views here.
def home(request):
    context={}
    return render(request, "itec/home.html", context)

def manele(request):
    context={}
    return render(request, "itec/manele.html", context)