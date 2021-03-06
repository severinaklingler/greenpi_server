import datetime

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from api.models import Measurement

# Create your views here.

@api_view(['GET'])
def chart(request):
    sensor_type = request.GET.get('sensor','')
    time_range = request.GET.get('time_range','')
    color_string = request.GET.get('color','7,121,228')

    if time_range == 'today':
        date_to_show = datetime.date.today()
    else:
        date_to_show = datetime.date.today() - datetime.timedelta(days=1)

    labels = list(range(24))
    data = []
    for m in Measurement.objects.filter(when__date=date_to_show).filter(sensor=sensor_type).order_by("when"):
        data.append({'x' : m.when.hour + m.when.minute / 60 , 'y' : m.value})

    chart_config = {
        'type': 'line',
        'data': {
            'labels': labels,
            'datasets': [{
                'label': 'My First dataset',
                'backgroundColor': 'rgba(' + color_string +',0.5)',
                'borderColor': 'rgb(' + color_string + ')',
                'data': data
            }]
        },
         "options":{
            'legend' : {
                'display' : False
            },
            'scales': {
                'xAxes': [{
                'type': 'linear',
                'gridLines' : {
                    'display' : False
                },
                'ticks': {
                    'min': 1,
                    'max': 24
                }
                }]
            }
        }
    }
    return JsonResponse(data=chart_config)
