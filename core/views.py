
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Activity
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import logout
from django.http import JsonResponse
from django.db.models import Q

def homepage(request):
    return render(request, 'core/homepage.html')

def index(request):
    all_activities = Activity.objects.all()
    return render(request, 'core/index.html', {'all_activities': all_activities})

def aboutus(request):
    return render(request, 'core/aboutus.html')

def detail(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request, 'core/detail.html', {'activity': activity})

def add_total(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    try:
        if activity.is_complete:
            activity.is_complete = False
        else:
            activity.is_complete = True
        activity.save()
    except (KeyError, Activity.DoesNotExist):
        return JsonResponse({'success':False})
    else:
        return JsonResponse({'success':True})

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

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                all_activities = Activity.objects.all()
                #all_activities = Activity.objects.filter(user=request.user)
                return render(request, 'core/index.html', {'all_activities': all_activities})
            else:
                return render(request, 'core/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'core/login.html', {'error_message': 'Invalid login'})
    return render(request, 'core/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'core/homepage.html', context)
