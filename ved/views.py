from django.shortcuts import render
from models import Event, YearlyEvent, Darshan, Photos
from datetime import datetime,date,timedelta
from dateutil.relativedelta import relativedelta
from django.db.models import Q
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

def datedisp(request,pmonth,pday):
    context = {}
    temp = "ved/dates/" + str(pmonth).zfill(2) + str(pday).zfill(2) + ".html"
    return render(request, temp, context)

def events(request, pmonth = None, pyear = None):
    today_date = datetime.now()
    from_date = date(today_date.year,today_date.month,1)
    to_date = from_date + relativedelta(months=1)
    
    events = Event.objects.filter(Q(event_start__gte = from_date),Q(event_end__lt = to_date)).order_by('event_start')

    print events

    return render(request, 'ved/events.html', {'events':events})

def yearlyevents(request, pmonth = None):
    curr_year = datetime.now().year
    if pmonth:
        events = YearlyEvent.objects.filter(event_date__year = curr_year,event_date__month = pmonth).order_by('event_date')
    else:
        events = YearlyEvent.objects.filter(event_date__year = curr_year).order_by('event_date')
        
    return render(request, 'ved/yearly_events.html', {'yearlyevents':events})


def darshan(request):
    darshans = Darshan.objects.all().order_by('display_order')
    return render(request, 'ved/darshan.html', {'darshans':darshans})

def photos(request):
    return render(request, 'ved/photos.html', {})

def demo_light_skin(request):
    photos = Photos.objects.all().order_by('display_order')
    return render(request, 'ved/demo_light_skin.html', {'photos':photos})
