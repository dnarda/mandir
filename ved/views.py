from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    return render(request, 'ved/index.html', context)

def test(request):
    context = {}
    return render(request, 'ved/test.html', context)

def t2(request):
    context = {}
    return render(request, 'ved/t2.html', context)

