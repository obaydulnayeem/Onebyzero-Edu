from django.db import models
from .choices import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from account.models import Profile

class University(models.Model):
    name = models.CharField(max_length=100)
    # location = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'

class Department(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    ambassadors = models.ManyToManyField(User, blank=True)
    def __str__(self):
        return f'{self.name}'

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    credit = models.DecimalField(max_digits=4, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE, default=1)
    year = models.PositiveIntegerField()
    semester = models.PositiveIntegerField()
    syllabus = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

class Question(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.PositiveIntegerField(choices=YEAR_CHOICES)
    semester = models.PositiveIntegerField(choices=SEMESTER_CHOICES)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=50, choices=EXAM_CHOICES)
    session = models.CharField(max_length=9, choices=SESSION_CHOICES)
    question_file = models.FileField(upload_to='study/questions/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'png', 'jpeg'])])
    upload_time = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    love_count = models.IntegerField(default=0)
    feedback = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.exam_name
    
class NoteModel(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.PositiveIntegerField(choices=YEAR_CHOICES)
    semester = models.PositiveIntegerField(choices=SEMESTER_CHOICES)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # exam_name = models.CharField(max_length=50, choices=EXAM_CHOICES)
    session = models.CharField(choices=SESSION_CHOICES, max_length=50)
    note_title = models.CharField(max_length=200)
    note_author = models.CharField(max_length=100)
    note_file = models.FileField(upload_to='study/notes/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'png', 'jpeg'])])
    upload_time = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # love_count = models.IntegerField(default=0)
    feedback = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.note_title
    
class BookModel(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.PositiveIntegerField(choices=YEAR_CHOICES)
    semester = models.PositiveIntegerField(choices=SEMESTER_CHOICES)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # session = models.CharField(choices=SESSION_CHOICES, max_length=50)
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=100)
    book_file = models.FileField(upload_to='study/books/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    upload_time = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # love_count = models.IntegerField(default=0)
    feedback = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.book_title    


class LectureModel(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.PositiveIntegerField(choices=YEAR_CHOICES)
    semester = models.PositiveIntegerField(choices=SEMESTER_CHOICES)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session = models.CharField(choices=SESSION_CHOICES, max_length=50)
    lecture_title = models.CharField(max_length=200)
    lecture_author = models.CharField(max_length=100)
    lecture_file = models.FileField(upload_to='study/lectures/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    upload_time = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # love_count = models.IntegerField(default=0)
    feedback = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.lecture_title
