from django.contrib import admin
from .models import University, Department, Course, Question, Note

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_format_name')

    def custom_format_name(self, obj):
        return f'{obj.name}'
    custom_format_name.short_description = 'University Name'
    
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_format_name', 'university_name')

    def custom_format_name(self, obj):
        return f'{obj.name}'
    custom_format_name.short_description = 'Department Name'

    def university_name(self, obj):
        return obj.university.name if obj.university else None
    university_name.short_description = 'University Name'

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_name', 'department_name', 'university_name')
    def course_name(self, obj):
        return obj.title
    course_name.short_description = 'Course Name'
    
    def department_name(self, obj):
        return obj.department.name
    department_name.short_description = 'Department Name'
    
    def university_name(self, obj):
        return obj.department.university.name
    university_name.short_description = 'University Name'
    
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam_name', 'department_name', 'university_name')
    
    def exam_name(self, obj):
        return obj.exam_name
    exam_name.short_description = 'Exam Name'
        
    def department_name(self, obj):
        return obj.department.name
    department_name.short_description = 'Department Name'
    
    def university_name(self, obj):
        return obj.department.university.name
    university_name.short_description = 'University Name'
    
admin.site.register(Note)

admin.site.register(Department, DepartmentAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Question, QuestionAdmin)