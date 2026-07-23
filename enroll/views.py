from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import user


# This function will add new Item and show all items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()

    stud = user.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})


# This function will Update/Edit
def update_data(request, id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        pi = user.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)

    return render(request, 'enroll/updatestudent.html', {'form': fm})


# This function will Delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


# Home Page
def home(request):
    return HttpResponse("Home Page")