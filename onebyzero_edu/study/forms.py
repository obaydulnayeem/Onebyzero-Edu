from django import forms
from .models import *
from account.models import Profile
from django.contrib.auth.models import User

class UniversityForm(forms.Form):
    university = forms.ModelChoiceField(queryset=University.objects.all(), empty_label="Select a university")

class DepartmentForm(forms.Form):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label="Select a department")

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
 
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['university', 'department', 'year', 'semester', 'course', 'exam_name', 'session', 'question_file']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].queryset = Department.objects.none()
        self.fields['course'].queryset = Course.objects.none()

        if all(field in self.data for field in ['university', 'department', 'year', 'semester']):
            try:
                university_id = int(self.data.get('university'))
                department_id = int(self.data.get('department'))
                year = int(self.data.get('year'))
                semester = int(self.data.get('semester'))
                
                # Filter the 'department' queryset based on the selected 'university'.
                self.fields['department'].queryset = Department.objects.filter(university_id=university_id).order_by('name')
                
                # Filter the 'course' queryset based on 'university', 'department', 'year', and 'semester'.
                self.fields['course'].queryset = Course.objects.filter(
                    department_id=department_id, year=year, semester=semester
                ).order_by('title')

            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            # If the form is for an instance (editing an existing instance), set the queryset based on the instance's data.
            # You'll need to replace these with the appropriate logic based on your model structure.
            self.fields['department'].queryset = self.instance.university.department_set.order_by('name')
            self.fields['course'].queryset = self.instance.department.course_set.filter(year=self.instance.year, semester=self.instance.semester).order_by('name')

class NoteForm(forms.ModelForm):
    class Meta:
        model = NoteModel
        fields = ['university', 'department', 'year', 'semester', 'course', 'session', 'note_title', 'note_author', 'note_file']
        
class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['university', 'department', 'year', 'semester', 'course', 'book_title', 'book_author', 'book_file']
        
class LectureForm(forms.ModelForm):
    class Meta:
        model = LectureModel
        fields = ['university', 'department', 'year', 'semester', 'session', 'course', 'lecture_title', 'lecture_author', 'lecture_file']
    


class MyDepartmentForm(forms.Form):
    university = forms.ModelChoiceField(
        queryset=University.objects.all(),
        empty_label="Select a university",
        widget=forms.Select(attrs={'id': 'id_university'})
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        empty_label="Select a department",
        widget=forms.Select(attrs={'id': 'id_department'})
    )
    
class MyResourcesSelectionForm(forms.Form):
    university = forms.ModelChoiceField(queryset=University.objects.all())
    department = forms.ModelChoiceField(queryset=Department.objects.none())
    semester = forms.IntegerField()
    year = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].queryset = Department.objects.none()

        if 'university' in self.data:
            try:
                university_id = int(self.data.get('university'))
                self.fields['department'].queryset = Department.objects.filter(university_id=university_id).order_by('name')
            except (ValueError, TypeError):
                pass  # Invalid input from the client; ignore and fallback to an empty queryset
            
            
            
# class MakeAmbassadorForm(forms.Form):
#     selected_users = forms.ModelMultipleChoiceField(
#         queryset=User.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#     )

class MakeAmbassadorForm(forms.Form):
    selected_users = forms.ModelMultipleChoiceField(
        queryset=Profile.objects.all(),  # Replace with your user profile queryset
        widget=forms.CheckboxSelectMultiple,
    )
    
    def __init__(self, *args, **kwargs):
        department_id = kwargs.pop('department_id', None)
        super(MakeAmbassadorForm, self).__init__(*args, **kwargs)

        # Define 'department_id' as a hidden field
        self.fields['department_id'] = forms.IntegerField(widget=forms.HiddenInput(), initial=department_id)