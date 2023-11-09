from django.shortcuts import render
from study.models import Question

def profile_question_contributions(request):
    user = request.user.id

    qs_sem1 = Question.objects.filter(uploaded_by=user, course__year=1, course__semester=1).count()
    
    qs_sem2 = Question.objects.filter(uploaded_by=user, course__year=1, course__semester=2).count()
    
    qs_sem3 = Question.objects.filter(uploaded_by=user, course__year=2, course__semester=1).count()
    
    qs_sem4 = Question.objects.filter(uploaded_by=user, course__year=2, course__semester=2).count()
    
    qs_sem5 = Question.objects.filter(uploaded_by=user, course__year=3, course__semester=1).count()
    
    qs_sem6 = Question.objects.filter(uploaded_by=user, course__year=3, course__semester=2).count()
    
    qs_sem7 = Question.objects.filter(uploaded_by=user, course__year=4, course__semester=1).count()
    
    qs_sem8 = Question.objects.filter(uploaded_by=user, course__year=4, course__semester=2).count()
    
    qs_total = qs_sem1 + qs_sem2 + qs_sem3 + qs_sem4 + qs_sem5 + qs_sem6 + qs_sem7 + qs_sem8
    
    context = {
        'qs_sem1': qs_sem1,
        'qs_sem2': qs_sem2,
        'qs_sem3': qs_sem3,
        'qs_sem4': qs_sem4,
        'qs_sem5': qs_sem5,
        'qs_sem6': qs_sem6,
        'qs_sem7': qs_sem7,
        'qs_sem8': qs_sem8,
        'qs_total': qs_total
    }
    
    return {'context': context}
