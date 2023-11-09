from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('batch_ambassador', 'Batch Ambassador'),
        ('departmental_ambassador', 'Departmental Ambassador'),
        ('university_ambassador', 'University Ambassador'),
        ('admin', 'Admin'),
        # Add more user types if needed
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICES, default='student')
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True)
    university = models.ForeignKey('study.University', on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey('study.Department', on_delete=models.CASCADE, blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    semester = models.PositiveIntegerField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
