from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    #return HttpResponse("Hello")
    return render(request, 'ved/index.html', context)

