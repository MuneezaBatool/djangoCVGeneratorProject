# forms.py
from django import forms
from .models import Profile

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'job' ,'location', 'email', 'phone', 'linkedin', 'summary','skill1','skill2','skill3','skill4', 'degreeU', 'university', 'yearU','degreeC', 'college', 'yearC','degreeS', 'school', 'yearS', 
                 'job_title1', 'company1', 'job_description1' ,'start_date1', 'end_date1','job_title2','job_description2' , 'company2', 'start_date2', 'end_date2']

