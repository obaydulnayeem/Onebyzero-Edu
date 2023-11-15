from django.urls import path
from . import views
from .views import error_department_access

urlpatterns = [
    path('university/<int:university_id>/', views.university_detail, name='university_detail'),
    
    # path('my_department/<int:university_id>/<int:department_id>/<int:course_id>/', views.my_department, name='my_department'),
    
    path('get_access/', views.get_access, name='get_access'),
    
    path('my_department/<int:university_id>/<int:department_id>/', views.my_department, name='my_department'),

    path('view_course/<int:course_id>/', views.view_course, name='view_course'),

    path('my_resources/<int:department_id>/<int:year>/<int:semester>/', views.my_resources, name='my_resources'),
    
    path('my_resources_selection/', views.my_resources_selection, name='my_resources_selection'),
    
    # QUESTIONS---------------------------------
    path('add_question/', views.add_question, name='add_question'),
    
    path('view_questions/<int:course_id>/', views.view_questions, name='view_questions'),
    
    path('view_questions/<int:question_id>/delete/', views.delete_question, name='delete_question'),
    
    # NOTES-------------------------------------
    path('add_note/', views.add_note, name='add_note'),
    
     path('view_notes/<int:course_id>/', views.view_notes, name='view_notes'),
    
    
    # FEEDBACKS ============================================
    path('submit-feedback/<int:question_id>/', views.submit_feedback, name='submit_feedback'),
   
    path('success-feedback/', views.success_feedback, name='success_feedback'),
    
    path('view_feedback/', views.view_feedback, name='view_feedback'),
    
    
    
    
    path('handle_love_click/<int:question_id>/', views.handle_love_click, name='handle_love_click'),
    
    path('share/<int:question_id>/', views.share_question, name='share_question'),

    path('ajax/load-departments/', views.load_departments, name='ajax_load_departments'), # AJAX
    
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'), # AJAX
    
    # path('department_list/', views.nothing, name='nothing'),
    
    path('error/department/access-denied/', error_department_access, name='department_access_denied'),

    path('contributors/', views.contributors, name='contributors'),
        
    path('nothing/', views.nothing, name='nothing'),
    
    path('test_page1/', views.test_page1, name='test_page1'),
    
    path('test_page2/', views.test_page2, name='test_page2'),

]
