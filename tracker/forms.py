from django import forms
from tracker.models import Student
from tracker.models import Assessment
from tracker.models import Standard

class GroupForm(forms.Form):
    numbergroups = forms.IntegerField(label='Number of Groups', min_value=1)
    
    selected_standards = forms.ModelMultipleChoiceField(label='Select Standards (Hold Command to Select Multiple)', queryset=Standard.objects.all())