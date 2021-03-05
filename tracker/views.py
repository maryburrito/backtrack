from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# list resources, create resources, read resources, update resources, and delete resources (CRUDL - Create, Read, Updadta, Delete)
# Django Admin - CRUD application , roles associated with each CRUD action 
# DetailView - view details about an object, ListView - lists items, FormView, CreateView, UpdateView, DeleteView 
# since Django knows about data models (models.py) 
#URLs: Paths, query parameters, ect. 
#Scheme - HTTPS , host - domain using, path - the resource , query string - affect data displays, hash location - refer to somethin on the page

from django.views.generic import ListView, DetailView
from django.urls import reverse, reverse_lazy


from tracker.models import Student, Standard, Assessment
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def signout(request):
    logout(request)
    # TODO : use signout.html to confirm user signout 
    return redirect('home')



def home(request):
    return render(request, "home.html")


class StudentList(ListView):
    model = Student


class StudentCreate(CreateView):
    model = Student
    fields = ['active', 'first_name', 'last_name']


class StudentUpdate(UpdateView):
    model = Student
    fields = ['active', 'first_name', 'last_name']


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student-list')

class StudentDetail(DetailView):
    model = Student
    fields = ['active', 'first_name', 'last_name', 'statement_name', 'score']


class StandardList (ListView):
    model = Standard


class StandardCreate(CreateView):
    model = Standard
    fields = ['active', 'statement_name']


class StandardUpdate(UpdateView):
    model = Standard
    fields = ['active', 'statement_name']


class StandardDelete(DeleteView):
    model = Standard
    success_url = reverse_lazy('standard-list')

class StandardDetail(DetailView):
    model = Standard


class AssessmentList (ListView):
    model = Assessment


class AssessmentCreate(CreateView):
    model = Assessment
    fields = ['student', 'standard', 'score']


class AssessmentUpdate(UpdateView):
    model = Assessment
    fields = ['student', 'standard', 'score']


class AssessmentDelete(DeleteView):
    model = Assessment
    success_url = reverse_lazy('assessment-list')

class AssessmentDetail(DetailView):
    model = Assessment


    #  def get_query(self):
    #     queryset = Student.objects.all()
    #     tag_qp = self.request.GET.getlist('tag')
    #     if tag_qp:
    #         return queryset.filter(tags__slug__in=tag_qp)
    #     return queryset
