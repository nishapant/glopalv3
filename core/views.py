
#from django.shortcuts import render


from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Activity


def index(request):
    all_activites = Activity.objects.all()
    return render(request, 'core/index.html', {'all_activites': all_activites})

def detail(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request, 'core/detail.html', {'activity': activity})
