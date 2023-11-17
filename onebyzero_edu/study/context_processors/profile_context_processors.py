from study.models import *

def profile_question_contributions(request):
    user = request.user.id

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
    total_uploads = qs_total + books_total, lectures_total, notes_total
    
    context = {
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
    }
    
    return context
