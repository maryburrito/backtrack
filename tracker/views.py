from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# list resources, create resources, read resources, update resources, and delete resources (CRUDL - Create, Read, Updadta, Delete)
# Django Admin - CRUD application , roles associated with each CRUD action 
# DetailView - biew details about an object, ListView - lists items, FormView, CreateView, UpdateView, DeleteView 
# since Django knows about data models (models.py) 
#URLs: Paths, query parameters, ect. 
#Scheme - HTTPS , host - domain using, path - the resource , query string - affect data displays, hash location - refer to somethin on the page

from django.views.generic import ListView, DetailView
from django.urls import reverse, reverse_lazy


from tracker.models import Student, Standard, Assessment


def hello_world(request):
    return HttpResponse("Hello, world!")


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


class StandardList (ListView):
    model = Standard


class StandardCreate(CreateView):
    model = Standard
    fields = ['name']


class StandardUpdate(UpdateView):
    model = Standard
    fields = ['name']


class StandardDelete(DeleteView):
    model = Standard
    success_url = reverse_lazy('student-list')


class AssessmentList (ListView):
    model = Assessment


class AssessmentCreate(CreateView):
    model = Assessment
    fields = ['name']


class AssessmentUpdate(UpdateView):
    model = Assessment
    fields = ['name']


class AssessmentDelete(DeleteView):
    model = Assessment
    success_url = reverse_lazy('student-list')


    #  def get_query(self):
    #     queryset = Student.objects.all()
    #     tag_qp = self.request.GET.getlist('tag')
    #     if tag_qp:
    #         return queryset.filter(tags__slug__in=tag_qp)
    #     return queryset
