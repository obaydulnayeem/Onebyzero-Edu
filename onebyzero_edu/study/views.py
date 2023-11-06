from django.shortcuts import render, redirect
from .models import University, Department, Course, Question, NoteModel
from django.shortcuts import get_object_or_404
from .forms import QuestionForm, MyDepartmentForm, MyResourcesSelectionForm, NoteForm
from django.contrib.auth.models import User
from collections import Counter
from django.db.models import Count
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseRedirect


def is_departmental_ambassador(user):
    return user.is_authenticated and user.profile.user_type == 'departmental_ambassador'


def university_detail(request, university_id):
    university = University.objects.get(pk=university_id)
    departments = Department.objects.filter(university=university)
    return render(request, 'university_detail.html', {'university': university, 'departments': departments})


@user_passes_test(is_departmental_ambassador, login_url='/study/error/department/access-denied/')
def my_department(request, university_id, department_id):
    university = get_object_or_404(University, pk=university_id)
    department = get_object_or_404(Department, pk=department_id, university=university)
    
    # courses = department.course_set.filter(year=1, semester=2)
    courses = department.course_set.all()

    return render(request, 'my_department.html', {'department': department, 'university': university, 'courses': courses})

def error_department_access(request):
    return render(request, 'department_access_denied.html', status=403)


def my_resources(request, department_id, year, semester):
    department = get_object_or_404(Department, pk=department_id)
    courses = Course.objects.filter(department=department, year=year, semester=semester)
    
    course_data = []
    for course in courses:
        question_count = Question.objects.filter(course=course).count()
        note_count = NoteModel.objects.filter(course=course).count()
        course_data.append({'course': course, 'question_count': question_count, 'note_count': note_count})
        
    context = {
        'department': department,
        'year': year,
        'semester': semester,
        'courses': courses,
        # 'question_count': question_count,
        'course_data': course_data,
        'note_count': note_count
    }

    return render(request, 'my_resources.html', context)




def my_resources_selection(request):
    if request.method == 'POST':
        form = MyResourcesSelectionForm(request.POST)
        if form.is_valid():
            university = form.cleaned_data['university']
            department = form.cleaned_data['department']
            semester = form.cleaned_data['semester']
            year = form.cleaned_data['year']
            
            # Redirect to my_resources view with the selected parameters
            return HttpResponseRedirect(reverse('my_resources', args=[department.id, year, semester]))
    else:
        form = MyResourcesSelectionForm()

    return render(request, 'my_resources_selection.html', {'form': form})


# QUESTION ================================================
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False) # Create the question object but don't save it yet
            question.uploaded_by = request.user  # Set the uploaded_by field to the currently logged-in user
            question.save()  # Save the question with the uploaded_by information
            return redirect('view_questions', course_id=question.course.id)
    else:
        form = QuestionForm()
    return render(request, 'add_question.html', {'form': form})



def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    course_id = question.course.id
    return redirect('view_questions', course_id=course_id)

def view_questions(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    questions = Question.objects.filter(course=course).order_by('-upload_time')
    
    session_filter = request.GET.get('session')
    exam_name_filter = request.GET.get('exam_name')

    if session_filter:
        questions = questions.filter(session=session_filter)

    if exam_name_filter:
        questions = questions.filter(exam_name__icontains=exam_name_filter)
        
    all_uploaders = Question.objects.filter(course=course_id).values_list('uploaded_by__username', flat=True).distinct()
    
    users_with_question_count = (
        Question.objects
        .filter(course=course)
        .values('uploaded_by__username')
        .annotate(question_count=Count('uploaded_by__username'))
    )

    context = {
        'questions': questions,
        'course': course,
        'all_uploaders': all_uploaders,
        # 'question_count': question_count
        'users_with_question_count': users_with_question_count
    }

    return render(request, 'view_questions.html', context)

def share_question(request, question_id):
    # Retrieve the question with the specified ID or handle appropriately
    question = get_object_or_404(Question, pk=question_id)
    # You can pass the question to a template and render it for viewing
    return render(request, 'share_question.html', {'question': question})

# NOTES=================================================
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False) # Create the question object but don't save it yet
            note.uploaded_by = request.user  # Set the uploaded_by field to the currently logged-in user
            note.save()  # Save the question with the uploaded_by information
            return redirect('view_notes', course_id=note.course.id)
    else:
        form = NoteForm()
    return render(request, 'resources/notes/add_note.html', {'form': form})

def view_notes(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    notes = NoteModel.objects.filter(course=course).order_by('-upload_time')
    
    session_filter = request.GET.get('session')
    exam_name_filter = request.GET.get('exam_name')

    if session_filter:
        notes = notes.filter(session=session_filter)
        
    all_uploaders = NoteModel.objects.filter(course=course_id).values_list('uploaded_by__username', flat=True).distinct()
    
    users_with_note_count = (
        NoteModel.objects
        .filter(course=course)
        .values('uploaded_by__username')
        .annotate(note_count=Count('uploaded_by__username'))
    )

    context = {
        'notes': notes,
        'course': course,
        'all_uploaders': all_uploaders,
        # 'question_count': question_count
        'users_with_note_count': users_with_note_count
    }

    return render(request, 'resources/notes/view_notes.html', context)

def view_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    university = course.university
    department = course.department
    question_count = Question.objects.filter(course=course).count()
    note_count = NoteModel.objects.filter(course=course).count()
    syllabus = course.syllabus
    
    return render(request, 'view_course.html', {'course': course, 'university': university, 'department': department, 'question_count': question_count, 'note_count': note_count, 'syllabus': syllabus})


def handle_love_click(request, question_id):
    if request.method == 'POST':
        question = Question.objects.get(pk=question_id)
        question.love_count += 1
        question.save()
        return JsonResponse({'love_count': question.love_count})



# AJAX
def load_departments(request):
    university_id = request.GET.get('university_id')
    departments = Department.objects.filter(university_id=university_id).all()
    return render(request, 'department_dropdown_list_options.html', {'departments': departments})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
    
def load_courses(request):
    university_id = request.GET.get('university_id')
    department_id = request.GET.get('department_id')
    semester = request.GET.get('semester')
    year = request.GET.get('year')
    courses = Course.objects.filter(university_id=university_id, department_id = department_id, year = year, semester = semester).all()
    return render(request, 'course_dropdown_list_options.html', {'courses': courses})


def submit_feedback(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    exam_name = question.exam_name
    session = question.session
    course_name = question.course.title
    department_name = question.course.department.name
    university_name = question.course.department.university.name

    
    if request.method == 'POST':
        
        if question_id:  # Check if question_id is not an empty string
            feedback_text = request.POST.get('feedback')
            question = get_object_or_404(Question, pk=question_id)
            question.feedback = feedback_text
            question.save()
        return HttpResponseRedirect(reverse('view_questions', args=[question.course.id]))

    
    # return HttpResponseRedirect(reverse('success_feedback'))
    
    return render(request, 'feedbacks/submit_feedback.html', {
        'question_id': question_id,
        'exam_name': exam_name,
        'session': session,
        'course_name': course_name,
        'department_name': department_name,
        'university_name': university_name
    })


def success_feedback(request):
    # Your logic for the success feedback view
    return render(request, 'feedbacks/success_feedback.html')

def view_feedback(request):
    feedbacks = Question.objects.all() # Fetch all feedbacks (adjust as needed)
    return render(request, 'feedbacks/view_feedbacks.html', {'feedbacks': feedbacks})




def contributors(request):
    
    return render(request, 'contributors.html')


def nothing(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False) # Create the question object but don't save it yet
            question.uploaded_by = request.user  # Set the uploaded_by field to the currently logged-in user
            question.save()  # Save the question with the uploaded_by information
            return redirect('view_questions', course_id=question.course.id)
    else:
        form = QuestionForm()
    return render(request, 'add_question.html', {'form': form}) 