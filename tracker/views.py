from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.urls import reverse, reverse_lazy
from tracker.models import Student, Standard, Assessment
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView    
from django.http import HttpResponseRedirect
from django.shortcuts import render
from tracker.groups import ResolveGroups
from tracker.forms import GroupForm

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
    return redirect('home')

def home(request):
    return render(request, "home.html")

def groupform(request):
    form = GroupForm(request.GET)
    context = {
        'form': form
    }
    if form.is_valid(): 
        print(form.cleaned_data['selected_standards'], form.cleaned_data['numbergroups'])
        context["sorted_students"] = ResolveGroups(form.cleaned_data['numbergroups'], form.cleaned_data['selected_standards'])

    return render(request, 'groups.html', context)

class StudentList(LoginRequiredMixin, ListView):
    model = Student


class StudentCreate(LoginRequiredMixin, CreateView):
    model = Student
    fields = ['active', 'first_name', 'last_name']


class StudentUpdate(LoginRequiredMixin, UpdateView):
    model = Student
    fields = ['active', 'first_name', 'last_name']


class StudentDelete(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('student-list')

class StudentDetail(LoginRequiredMixin, DetailView):
    model = Student
    fields = ['active', 'first_name', 'last_name', 'statement_name', 'score', 'semester']


class StandardList (LoginRequiredMixin, ListView):
    model = Standard


class StandardCreate(LoginRequiredMixin, CreateView):
    model = Standard
    fields = ['active', 'statement_name']


class StandardUpdate(LoginRequiredMixin, UpdateView):
    model = Standard
    fields = ['active', 'statement_name']


class StandardDelete(LoginRequiredMixin, DeleteView):
    model = Standard
    success_url = reverse_lazy('standard-list')

class StandardDetail(LoginRequiredMixin, DetailView):
    model = Standard


class AssessmentList (LoginRequiredMixin, ListView):
    model = Assessment


class AssessmentCreate(LoginRequiredMixin, CreateView):
    model = Assessment
    fields = ['student', 'standard', 'score', "semester"]


class AssessmentUpdate(LoginRequiredMixin, UpdateView):
    model = Assessment
    fields = ['student', 'standard', 'score', "semester"]


class AssessmentDelete(LoginRequiredMixin, DeleteView):
    model = Assessment
    success_url = reverse_lazy('assessment-list')

class AssessmentDetail(LoginRequiredMixin, DetailView):
    model = Assessment


def load_standards(request):
    standard = Standards.objects.all().order_by('standard__statement')
    return render(request, 'hr/grou_form.html', {'standard': standard})

