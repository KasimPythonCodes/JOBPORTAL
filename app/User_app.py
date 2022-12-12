from django.shortcuts import render ,HttpResponse ,redirect
from django.http import HttpResponse , HttpResponseNotFound,HttpResponseRedirect

from app.models import *
from django.contrib import messages


"""
   
    Strat User/Employee/Student/Other Panel Function

"""



def Submit_Resume_Form(request):
    if request.method == 'POST':
        myfile = request.FILES.get('myfile')
        r = Resume.objects.create(doc=myfile)
        r.save()
        # return HttpResponse(r.pk , r.doc)
        return render(request , "Resume/resume.html")
    return render(request , "Resume/resume.html")


