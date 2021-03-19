from django.urls import path
from django.contrib.auth.views import LoginView
from tracker.views import home, signup, signout, groupform
from tracker.views import StudentList, StudentCreate, StudentDelete, StudentUpdate, StudentDetail
from tracker.views import AssessmentList, AssessmentCreate, AssessmentDelete, AssessmentUpdate, StandardDetail
from tracker.views import StandardCreate, StandardList, StandardDelete, StandardUpdate, AssessmentDetail
from tracker.views import reverse, reverse_lazy



urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(template_name = 'login.html'), name="login"),
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),
    path('students/', StudentList.as_view(), name='student-list'),
    path('student/add/', StudentCreate.as_view(), name ='student-add'),
    path('student/<int:pk>/', StudentUpdate.as_view(), name ='student-update'),
    path('student/<int:pk>/delete/', StudentDelete.as_view(), name ='student-delete'),
    path('students/<int:pk>/', StudentDetail.as_view(), name="student-detail"),
    path('standards/', StandardList.as_view(), name='standard-list'),
    path('standard/add/', StandardCreate.as_view(), name ='standard-add'),
    path('standard/<int:pk>/', StandardUpdate.as_view(), name ='standard-update'),
    path('standard/<int:pk>/delete/', StandardDelete.as_view(), name ='standard-delete'),
    path('standards/<int:pk>/', StandardDetail.as_view(), name="standard-detail"),
    path('assessments/', AssessmentList.as_view(), name='assessment-list'),
    path('assessment/add/', AssessmentCreate.as_view(), name ='assessment-add'),
    path('assessment/<int:pk>/', AssessmentUpdate.as_view(), name ='assessment-update'),
    path('assessment/<int:pk>/delete/', AssessmentDelete.as_view(), name ='assessment-delete'),
    path('assessments/<int:pk>/', AssessmentDetail.as_view(), name="assessment-detail"),
    path('groups/', groupform, name='group-form'),
]