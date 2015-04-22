from django.shortcuts import render
from models import Event, YearlyEvent, Darshan, Photos
from datetime import datetime,date,timedelta
from dateutil.relativedelta import relativedelta
from django.db.models import Q
from django.shortcuts import render
from forms import ContactForm, HallForm, PriestServiceForm
from django.core.mail import send_mail
from django.conf import settings

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
    to_date = from_date + relativedelta(months=2)
    
    events = Event.objects.filter(Q(event_date__gte = from_date),Q(event_date__lt = to_date)).order_by('event_date')

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

def volunteer(request):
    return render(request, 'ved/vol.html', {})

def priest(request):
    if request.method == 'POST':
        form = PriestServiceForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'ved/priest.html', {} )
        else:
            return render(request, 'ved/priest.html', {'form':form} )
            
    else:
        form = PriestServiceForm()
        return render(request, 'ved/priest.html', {'form':form} )

def hall(request):
    if request.method == 'POST':
        form = HallForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'ved/hall.html', {} )
        else:
            return render(request, 'ved/hall.html', {'form':form} )
            
    else:
        form = HallForm()
        return render(request, 'ved/hall.html', {'form':form} )

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            contact = form.instance

            mandir_staff = getattr(settings, "MANDIR_STAFF", None)

            ## Send Thank you email
            message = "Dear " + contact.name + "\n"
            message += "Thank you for your message. We will get back to you soon!"
            send_mail("Thank you from Ved Mandir!", message, 'no-reply@vedmandir.org', [contact.email])

            ## Notify Ved mandir staff
            message = "New Contact message received from " + contact.name + "\n"
            message += "-----------------------------------------------------\n"
            message += "Subject: " + contact.subject + "\n"
            message += "Message: \n"
            message += contact.message  + "\n"
            message += "-----------------------------------------------------\n"
            send_mail("New Contact Message", message, 'no-reply@vedmandir.org', mandir_staff)

            return render(request, 'ved/contact.html', {} )
        else:
            return render(request, 'ved/contact.html', {'form':form} )
            
    else:
        form = ContactForm()
        return render(request, 'ved/contact.html', {'form':form} )

def about(request):
    return render(request, 'ved/about.html', {})

