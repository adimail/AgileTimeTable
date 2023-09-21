# yourappname/views.py

from django.shortcuts import render, redirect
from .models import Subject
from django.db import connection

def manage_subjects(request):
    if request.method == 'POST':
        name = request.POST['name']
        abbreviation = request.POST['abbreviation']
        theory_hours = request.POST['theory_hours']
        semester = request.POST['semester']
        practical_hours = request.POST['practical_hours']
        
        subject = Subject(name=name, abbreviation=abbreviation, theory_hours=theory_hours, semester=semester, practical_hours=practical_hours)
        subject.save()
        
        return redirect('manage_subjects')

    subjects = Subject.objects.all()
    return render(request, 'manage_subjects.html', {'subjects': subjects})

def edit_subject(request, id):
    subject = Subject.objects.get(pk=id)
    
    if request.method == 'POST':
        subject.name = request.POST['name']
        subject.abbreviation = request.POST['abbreviation']
        subject.theory_hours = request.POST['theory_hours']
        subject.save()
        
        return redirect('manage_subjects')

    return render(request, 'edit_subject.html', {'subject': subject})

def delete_subject(request, id):
    Subject.objects.filter(pk=id).delete()
    return redirect('manage_subjects')
