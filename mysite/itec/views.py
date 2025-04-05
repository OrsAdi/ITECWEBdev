from django.shortcuts import render

# Create your views here.
def home(request):
    context={}
    return render(request, "itec/home.html", context)

def manele(request):
    context={}
    return render(request, "itec/manele.html", context)

def rock(request):
    context={}
    return render(request, "itec/rock.html", context)
def rap(request):
    context={}
    return render(request, "itec/rap.html", context)
def trap(request):
    context={}
    return render(request, "itec/trap.html", context)

def jaz(request):
    context={}
    return render(request, "itec/jaz.html", context)
def pop(request):
    context={}
    return render(request, "itec/pop.html", context)
