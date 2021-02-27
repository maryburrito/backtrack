from django.urls import path

from tracker.views import hello_world
from tracker.views import StudentList, StudentCreate, StudentDelete, StudentUpdate, StudentDetail
from tracker.views import AssessmentList, AssessmentCreate, AssessmentDelete, AssessmentUpdate
from tracker.views import StandardCreate, StandardList, StandardDelete, StandardUpdate
from tracker.views import reverse, reverse_lazy


urlpatterns = [
    path('', hello_world),
    path('students/', StudentList.as_view(), name='student-list'),
    path('student/add/', StudentCreate.as_view(), name ='student-add'),
    path('student/<int:pk>/', StudentUpdate.as_view(), name ='student-update'),
    path('student/<int:pk>/delete/', StudentDelete.as_view(), name ='student-delete'),
    path('students/<int:pk>/', StudentDetail.as_view(), name="student-detail"),
    path('standards/', StandardList.as_view(), name='standard-list'),
    path('assessments/', AssessmentList.as_view(), name='assessment-list'),
]