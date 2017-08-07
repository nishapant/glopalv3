
#from django.shortcuts import render


from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Activity
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm


def index(request):
    all_activites = Activity.objects.all()
    return render(request, 'core/index.html', {'all_activites': all_activites})

def detail(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request, 'core/detail.html', {'activity': activity})

class UserFormView(View):
    form_class = UserForm
    template_name = 'core/registration_form.html'
