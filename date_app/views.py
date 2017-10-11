from django.http import HttpResponse
import datetime

# Create your views here.

def date(request):
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    return HttpResponse("<h2>%s</h2>" % date)
