from django.shortcuts import render

# Create your views here.

# FUNCTIONS FOR ROUTES

# INDEX
def index(request):
    return render(request, 'tempApp/index.html')

# BASE
def toBase(request):
    return render(request, 'tempApp/base.html')

# ABOUT
def toAbout(request):
    return render(request, 'tempApp/about.html')