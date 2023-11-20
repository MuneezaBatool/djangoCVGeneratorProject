from django.shortcuts import render,redirect
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import os
from .forms import ResumeForm
from django.contrib.auth.decorators import login_required

@login_required
def accept(request):
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('list')  
    else:
        form = ResumeForm()

    return render(request, 'pdf/accept.html', {'form': form})



def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    config = pdfkit.configuration(wkhtmltopdf='C:/wkhtmltox/bin/wkhtmltopdf.exe')
    html = template.render({'user_profile': user_profile})
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',

    }
    
    pdf = pdfkit.from_string(html, False, options, configuration=config)
    
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    
    return response 





def list(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            profile_instance = form.save()
            profile_id = profile_instance.id
            return redirect('resume', id=profile_id)

    else:
        form = ResumeForm()

    return render(request, 'pdf/list.html', {'form': form})


def firstPage(request):

    return render(request,'pdf/firstPage.html')
