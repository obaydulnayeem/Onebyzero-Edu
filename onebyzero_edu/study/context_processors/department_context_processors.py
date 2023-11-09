from django.shortcuts import render
from study.models import Department
from study.models import Course

def department_context_view(request):
    user = request.user.id
    total_courses = Course.objects.all().count()
    
    sem1_total_courses = Course.objects.filter(year=1, semester=1).count()
    
    
    
    context = {
        'total_courses': total_courses,
        'sem1_total_courses': sem1_total_courses,
    }
    
    return {'context': context}
