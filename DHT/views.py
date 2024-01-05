from django.http import HttpResponse
from .models import Dht11
from django.shortcuts import render
import datetime
from django.utils import timezone
def test(repuest):
    return HttpResponse('Iot Project')

"""def dht_tab(request):
    tab = Dht11.objects.all()
    s = {'tab': tab}
    return render(request,'table.html',s)"""

def table(request):
    derniere_ligne = Dht11.objects.last()
    derniere_date = Dht11.objects.last().dt
    delta_temps = timezone.now() - derniere_date
    difference_minutes = delta_temps.seconds // 60
    temps_ecoule = ' il y a ' + str(difference_minutes) + ' min'
    if difference_minutes> 60:
        temps_ecoule = ('il y a ' + str(difference_minutes // 60) + 'h' + str(difference_minutes % 60) + 'min')
        valeurs = {'date': temps_ecoule, 'id': derniere_ligne.id, 'temp':
            derniere_ligne.temp, 'hum': derniere_ligne.hum}
        return render(request, 'table.html', {'valeurs': valeurs})

