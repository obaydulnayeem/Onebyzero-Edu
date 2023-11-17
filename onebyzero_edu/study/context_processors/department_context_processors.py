from study.models import Department
from study.models import Course
from django.db.models import Sum

def department_context_view(request):
    # user = request.user.id
    department_id = None

    # Assuming department_id is passed in the URL, for example: /department/1/
    if 'department_id' in request.resolver_match.kwargs:
        department_id = request.resolver_match.kwargs['department_id']
    
    total_courses = Course.objects.all().count()

    # TOTAL COURSES - SEMESTER WISE================================
    courses_sem1 = Course.objects.filter(year=1, semester=1).count()
    courses_sem2 = Course.objects.filter(year=1, semester=2).count()
    courses_sem3 = Course.objects.filter(year=2, semester=1).count()
    courses_sem4 = Course.objects.filter(year=2, semester=2).count()
    courses_sem5 = Course.objects.filter(year=3, semester=1).count()
    courses_sem6 = Course.objects.filter(year=3, semester=2).count()
    courses_sem7 = Course.objects.filter(year=4, semester=1).count()
    courses_sem8 = Course.objects.filter(year=4, semester=2).count()
    
    
    # TOTAL CREDITS SEMESTER WISE===============================
    credits_sem1 = Course.objects.filter(department = department_id, year=1, semester=1).aggregate(total_credits=Sum('credit'))['total_credits'] or 0
    
    credits_sem2 = Course.objects.filter(department = department_id, year=1, semester=2).aggregate(total_credits=Sum('credit'))['total_credits'] or 0
    
    credits_sem3 = Course.objects.filter(department = department_id, year=2, semester=1).aggregate(total_credits=Sum('credit'))['total_credits'] or 0
    
    credits_sem4 = Course.objects.filter(department = department_id, year=2, semester=2).aggregate(total_credits=Sum('credit'))['total_credits'] or 0
    
    credits_sem5 = Course.objects.filter(department = department_id, year=3, semester=1).aggregate(total_credits=Sum('credit'))['total_credits'] or 0
    
    credits_sem6 = Course.objects.filter(department = department_id, year=3, semester=2).aggregate(total_credits=Sum('credit'))['total_credits'] or 0
    
    credits_sem7 = Course.objects.filter(department = department_id, year=4, semester=1).aggregate(total_credits=Sum('credit'))['total_credits'] or 0
    
    credits_sem8 = Course.objects.filter(department = department_id, year=4, semester=2).aggregate(total_credits=Sum('credit'))['total_credits'] or 0

    context = {
        'total_courses': total_courses,

        'courses_sem1': courses_sem1,
        'courses_sem2': courses_sem2,
        'courses_sem3': courses_sem3,
        'courses_sem4': courses_sem4,
        'courses_sem5': courses_sem5,
        'courses_sem6': courses_sem6,
        'courses_sem7': courses_sem7,
        'courses_sem8': courses_sem8,
        
        
        'credits_sem1': credits_sem1,
        'credits_sem2': credits_sem2,
        'credits_sem3': credits_sem3,
        'credits_sem4': credits_sem4,
        'credits_sem5': credits_sem5,
        'credits_sem6': credits_sem6,
        'credits_sem7': credits_sem7,
        'credits_sem8': credits_sem8,
    }

    return context
