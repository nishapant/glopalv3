
#from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Activity

def index(request):
    all_activites = Activity.objects.all()
    template = loader.get_template('core/index.html')

    context = {
        'all_activites': all_activites,
    }
    return HttpResponse(template.render(context, request))

def detail(request, activity_id):
    return HttpResponse('<h2>Details for activity id: ' + str(activity_id) + '</h2>')
