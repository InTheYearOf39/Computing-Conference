from django.shortcuts import render, redirect
from conferenceapp.forms import RegistrationForm
from .models import Program

# Create your views here.
def  home(request):
    program1 = Program.objects.filter(day="Day 1")
    program2 = Program.objects.filter(day="Day 2")
    program3 = Program.objects.filter(day="Day 3")
    program4 = Program.objects.filter(day="Day 4")
    
    

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    else:
        form = RegistrationForm()
    context= {
        'program1':program1,
        'program2':program2,
        'program3':program3,
        'program4':program4,
        'form':form
            }
    return render(request,"conferenceapp/index.html",context)
