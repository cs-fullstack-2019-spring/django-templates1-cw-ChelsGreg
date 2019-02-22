from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'tempApp/index.html')


def toBase(request):
    return render(request, 'tempApp/base.html')


def toAbout(request):
    return render(request, 'tempApp/about.html')