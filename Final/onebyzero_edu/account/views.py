from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm, ProfileForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from . models import Profile
from django.contrib.auth.models import User
from study.models import Department, Course
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # Log the user in after registration
            # UserProfile.objects.create(user=user)
            return redirect('home')  # Redirect to the user's profile page
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('my_department', university_id=1, department_id=1)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


# PROFILE VIEWS =============================
@login_required
def my_profile(request):
    # Assuming the user is logged in
    user = request.user
    
    try:
        profile = Profile.objects.get(user=user)  # Retrieve the user's profile
    except Profile.DoesNotExist:
         # If the profile doesn't exist, create a new one
        profile = Profile(user=user)
        profile.save()
        # You can also redirect the user to an edit profile page to fill in details
        return redirect('my_profile')
    
    context = {
        'profile': profile
    }

    return render(request, 'profile/my_profile.html', context)

from study.models import *
@login_required
def view_profile(request, user_id):
    # Retrieve the user based on user_id, or return a 404 if not found
    user = get_object_or_404(User, id=user_id)
    
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        # If the profile doesn't exist, you can handle it as needed
        # For example, you might want to create a new profile or redirect to a page
        # return render(request, 'profile/profile_not_found.html')
        pass
    
    # QUESTIONS ========================================
    qs_sem1 = Question.objects.filter(uploaded_by=user, course__year=1, course__semester=1).count()
    
    qs_sem2 = Question.objects.filter(uploaded_by=user, course__year=1, course__semester=2).count()
    
    qs_sem3 = Question.objects.filter(uploaded_by=user, course__year=2, course__semester=1).count()
    
    qs_sem4 = Question.objects.filter(uploaded_by=user, course__year=2, course__semester=2).count()
    
    qs_sem5 = Question.objects.filter(uploaded_by=user, course__year=3, course__semester=1).count()
    
    qs_sem6 = Question.objects.filter(uploaded_by=user, course__year=3, course__semester=2).count()
    
    qs_sem7 = Question.objects.filter(uploaded_by=user, course__year=4, course__semester=1).count()
    
    qs_sem8 = Question.objects.filter(uploaded_by=user, course__year=4, course__semester=2).count()
    
    qs_total = qs_sem1 + qs_sem2 + qs_sem3 + qs_sem4 + qs_sem5 + qs_sem6 + qs_sem7 + qs_sem8
    

# BOOKS ==============================================
    books_sem1 = BookModel.objects.filter(uploaded_by=user, course__year=1, course__semester=1).count()
    
    books_sem2 = BookModel.objects.filter(uploaded_by=user, course__year=1, course__semester=2).count()
    
    books_sem3 = BookModel.objects.filter(uploaded_by=user, course__year=2, course__semester=1).count()
    
    books_sem4 = BookModel.objects.filter(uploaded_by=user, course__year=2, course__semester=2).count()
    
    books_sem5 = BookModel.objects.filter(uploaded_by=user, course__year=3, course__semester=1).count()
    
    books_sem6 = BookModel.objects.filter(uploaded_by=user, course__year=3, course__semester=2).count()
    
    books_sem7 = BookModel.objects.filter(uploaded_by=user, course__year=4, course__semester=1).count()
    
    books_sem8 = BookModel.objects.filter(uploaded_by=user, course__year=4, course__semester=2).count()
    
    books_total = books_sem1 + books_sem2 + books_sem3 + books_sem4 + books_sem5 + books_sem6 + books_sem7 + books_sem8
    

# LECTURE SLIDES ============================================
    lectures_sem1 = LectureModel.objects.filter(uploaded_by=user, course__year=1, course__semester=1).count()
    
    lectures_sem2 = LectureModel.objects.filter(uploaded_by=user, course__year=1, course__semester=2).count()
    
    lectures_sem3 = LectureModel.objects.filter(uploaded_by=user, course__year=2, course__semester=1).count()
    
    lectures_sem4 = LectureModel.objects.filter(uploaded_by=user, course__year=2, course__semester=2).count()
    
    lectures_sem5 = LectureModel.objects.filter(uploaded_by=user, course__year=3, course__semester=1).count()
    
    lectures_sem6 = LectureModel.objects.filter(uploaded_by=user, course__year=3, course__semester=2).count()
    
    lectures_sem7 = LectureModel.objects.filter(uploaded_by=user, course__year=4, course__semester=1).count()
    
    lectures_sem8 = LectureModel.objects.filter(uploaded_by=user, course__year=4, course__semester=2).count()
    
    lectures_total = lectures_sem1 + lectures_sem2 + lectures_sem3 + lectures_sem4 + lectures_sem5 + lectures_sem6 + lectures_sem7 + lectures_sem8
    
    
# NOTES =============================================
    notes_sem1 = BookModel.objects.filter(uploaded_by=user, course__year=1, course__semester=1).count()
    
    notes_sem2 = BookModel.objects.filter(uploaded_by=user, course__year=1, course__semester=2).count()
    
    notes_sem3 = BookModel.objects.filter(uploaded_by=user, course__year=2, course__semester=1).count()
    
    notes_sem4 = BookModel.objects.filter(uploaded_by=user, course__year=2, course__semester=2).count()
    
    notes_sem5 = BookModel.objects.filter(uploaded_by=user, course__year=3, course__semester=1).count()
    
    notes_sem6 = BookModel.objects.filter(uploaded_by=user, course__year=3, course__semester=2).count()
    
    notes_sem7 = BookModel.objects.filter(uploaded_by=user, course__year=4, course__semester=1).count()
    
    notes_sem8 = BookModel.objects.filter(uploaded_by=user, course__year=4, course__semester=2).count()
    
    notes_total = notes_sem1 + notes_sem2 + notes_sem3 + notes_sem4 + notes_sem5 + notes_sem6 + notes_sem7 + notes_sem8
    
    # TOTAL UPLOADS ==================
    total_uploads = sum([qs_total, books_total, lectures_total, notes_total], 0)
    
    # TOTALS UPLOADS SEMESTER WISE
    all_sem1 = sum([qs_sem1, books_sem1, lectures_sem1, notes_sem1], 0)
    all_sem2 = sum([qs_sem2, books_sem2, lectures_sem2, notes_sem2], 0)
    all_sem3 = sum([qs_sem3, books_sem3, lectures_sem3, notes_sem3], 0)
    all_sem4 = sum([qs_sem4, books_sem4, lectures_sem4, notes_sem4], 0)
    all_sem5 = sum([qs_sem5, books_sem5, lectures_sem5, notes_sem5], 0)
    all_sem6 = sum([qs_sem6, books_sem6, lectures_sem6, notes_sem6], 0)
    all_sem7 = sum([qs_sem7, books_sem7, lectures_sem7, notes_sem7], 0)
    all_sem8 = sum([qs_sem8, books_sem8, lectures_sem8, notes_sem8], 0)
    

    context = {
        'profile': profile,
        'viewed_user': user,
        
        'qs_sem1': qs_sem1,
        'qs_sem2': qs_sem2,
        'qs_sem3': qs_sem3,
        'qs_sem4': qs_sem4,
        'qs_sem5': qs_sem5,
        'qs_sem6': qs_sem6,
        'qs_sem7': qs_sem7,
        'qs_sem8': qs_sem8,
        'qs_total': qs_total,
        
        'books_sem1': books_sem1,
        'books_sem2': books_sem2,
        'books_sem3': books_sem3,
        'books_sem4': books_sem4,
        'books_sem5': books_sem5,
        'books_sem6': books_sem6,
        'books_sem7': books_sem7,
        'books_sem8': books_sem8,
        'books_total': books_total,
        
        'lectures_sem1': lectures_sem1,
        'lectures_sem2': lectures_sem2,
        'lectures_sem3': lectures_sem3,
        'lectures_sem4': lectures_sem4,
        'lectures_sem5': lectures_sem5,
        'lectures_sem6': lectures_sem6,
        'lectures_sem7': lectures_sem7,
        'lectures_sem8': lectures_sem8,
        'lectures_total': lectures_total,
        
        'notes_sem1': notes_sem1,
        'notes_sem2': notes_sem2,
        'notes_sem3': notes_sem3,
        'notes_sem4': notes_sem4,
        'notes_sem5': notes_sem5,
        'notes_sem6': notes_sem6,
        'notes_sem7': notes_sem7,
        'notes_sem8': notes_sem8,
        'notes_total': notes_total,
        
        'total_uploads': total_uploads,
        
        'all_sem1': all_sem1,
        'all_sem2': all_sem2,
        'all_sem3': all_sem3,
        'all_sem4': all_sem4,
        'all_sem5': all_sem5,
        'all_sem6': all_sem6,
        'all_sem7': all_sem7,
        'all_sem8': all_sem8,
    }

    return render(request, 'profile/view_profile.html', context)


@login_required
def edit_profile(request):
    user = request.user

    try:
        profile = Profile.objects.get(user=user)  # Retrieve the user's profile
    except Profile.DoesNotExist:
        # If the profile doesn't exist, create a new one
        profile = Profile(user=user)
        profile.save()
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form
    }

    return render(request, 'profile/edit_profile.html', context)


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def update_user_type(request, user_id):
    user = get_object_or_404(User, id=user_id)

    try:
        profile = user.profile  # Attempt to retrieve the profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=user)  # If the profile doesn't exist, create a new one

    if request.method == 'POST':
        new_user_type = request.POST.get('new_user_type')
        profile.user_type = new_user_type
        profile.save()
        return redirect('user_list')  # Redirect to the user list page after updating

    return render(request, 'update_user_type.html', {'profile': profile})



@login_required
def change_verification_status(request, profile_id):
    # Ensure the logged-in user has the necessary permissions to change verification status
    # if not request.user.profile.is_admin:
    #     return render(request, 'error.html', {'error_message': 'You do not have permission to change verification status.'})

    profile = get_object_or_404(Profile, id=profile_id)
    
    # Toggle the is_verified status
    profile.is_verified = not profile.is_verified
    profile.save()

    return render(request, 'verification_status_changed.html', {'profile': profile})


# AJAX
def load_departments(request):
    university_id = request.GET.get('university_id')
    departments = Department.objects.filter(university_id=university_id).all()
    return render(request, 'department_dropdown_list_options.html', {'departments': departments})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
    
def some_view(request, user_id):
    context = {
        **view_profile_contributions(request, user_id),  # Include the data from the context processor
        'other_variable': 'Some other data',  # You can include other variables as well
    }

    return render(request, 'profile/view_profile.html', context)