from django.shortcuts import render
from study.models import *
from django.contrib.auth.models import User

def home(request):
    # TOTALS
    total_questions = Question.objects.count()
    total_notes = NoteModel.objects.count()
    total_resources = total_questions + total_notes
    total_departments = Department.objects.count()
    total_courses = Course.objects.count()
    total_students = User.objects.count()

    # CONTEXT:
    context = {
        'total_resources': total_resources,
        'total_courses': total_courses,
        'total_departments': total_departments,
        'total_students': total_students,
    }
    
    return render(request, 'home.html', {'context': context})

