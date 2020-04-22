import datetime

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

# Create your views here.

@api_view(['GET'])
def chart(request):
    sensor = request.GET.get('sensor','')
    time_range = request.GET.get('time_range','')

    if time_range == 'today':
        date_to_show = datetime.date.today()
    else:
        date_to_show = datetime.date.today() - datetime.timedelta(days=1)

    labels = list()
    data = [{'x' : 1 , 'y' : 3},{'x' : 2 , 'y' : 2},{'x' : 3 , 'y' : 10}]

    chart_config = {
        'type': 'line',
        'data': {
            'labels': labels,
            'datasets': [{
                'label': 'My First dataset',
                'backgroundColor': 'rgba(7, 121, 228,0.5)',
                'borderColor': 'rgb(7, 121, 228)',
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
                }
                }]
            }
        }
    }
    return JsonResponse(data=chart_config)
