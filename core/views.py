
from django.shortcuts import render
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

# display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form })

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

             user = form.save(commit=False)

             # cleaned (normlaized) data
             username = form.cleaned_data['username']
             password = form.cleaned_data['password']
             user.set_password(password)
             user.save()

             # returns User objects if credentials are correct
             user = authenticate(username=username, password=password)

             if user is not None:

                 if user.is_active:
                     login(request, user)
                     return redirect('core:index')

        return render(request, self.template_name, {'form': form })
