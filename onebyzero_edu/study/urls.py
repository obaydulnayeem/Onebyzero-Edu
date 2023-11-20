from django.urls import path
from . import views
from .views import error_department_access

urlpatterns = [
    path('university/<int:university_id>/', views.university_detail, name='university_detail'),
    
    # path('my_department/<int:university_id>/<int:department_id>/<int:course_id>/', views.my_department, name='my_department'),
    
    path('get_access/', views.get_access, name='get_access'),
    
    path('my_department/<int:university_id>/<int:department_id>/', views.my_department, name='my_department'),

    # path('view_course/<int:course_id>/', views.view_course, name='view_course'),

    # REST API =================================================
    # path('view_course/<int:course_id>/', views.view_course, name='view_course'), # for REST API: serializer

    # path('create_course/', views.create_course, name='create_course'), # for REST API: deserializer, update, delete
    #---------------------------------------
    
    # path('my_course/', views.my_course, name='my_course'), # for REST API: get all by api_view
    
    # path('my_course/<int:course_id>/', views.my_course, name='my_course'), # for REST API: get by pk by api_view
    #---------------------------------------
    
    # path('my_course/', views.MyCourseView.as_view(), name='my_course'), # for REST API: class based view
    
    # path('my_course/<int:course_id>/', views.MyCourseView.as_view(), name='my_course'), # for REST API: class based view
    
    #--using mixins (individuals)------------------------------------- 

    # path('my_course/', views.MyCourseListView.as_view(), name='my_course'),
    
    # path('my_course_create/', views.MyCourseCreateView.as_view(), name='my_course_create'),
    
    # path('my_course_retrieve/<int:pk>/', views.MyCourseRetrieveView.as_view(), name='my_course_retrieve'),
    
    # path('my_course_update/<int:pk>/', views.MyCourseUpdateView.as_view(), name='my_course_update'),
    
    # path('my_course_destroy/<int:pk>/', views.MyCourseDestroyView.as_view(), name='my_course_destroy'),

    #--using mixins (together)-------------------------------------
    path('my_course_list_create/', views.MyCourseListCreateView.as_view(), name='my_course_list_create'),
    
    path('my_course_retrive_update_destroy/<int:pk>/', views.MyCourseRetrieveUpdateDestroyView.as_view(), name='my_course_retrive_update_destroy'),

    # ==================================================================
    path('my_resources/<int:department_id>/<int:year>/<int:semester>/', views.my_resources, name='my_resources'),

    path('my_resources_selection/', views.my_resources_selection, name='my_resources_selection'),

    # QUESTIONS---------------------------------
    path('add_question/', views.add_question, name='add_question'),

    path('view_questions/<int:course_id>/', views.view_questions, name='view_questions'),

    path('view_questions/<int:question_id>/delete/', views.delete_question, name='delete_question'),

    # NOTES-------------------------------------
    path('add_note/', views.add_note, name='add_note'),

    path('view_notes/<int:course_id>/', views.view_notes, name='view_notes'),

    # BOOKS-------------------------------------
    path('add_book/', views.add_book, name='add_book'),
    
    path('view_books/<int:course_id>/', views.view_books, name='view_books'),
    
    # LECTURE SLIDES -------------------------------------
    path('add_lecture/', views.add_lecture, name='add_lecture'),
    
    path('view_lectures/<int:course_id>/', views.view_lectures, name='view_lectures'),
    
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
        
    # TEST PURPOSE ===============================================
    path('nothing/', views.nothing, name='nothing'),
    
    path('test_page1/', views.test_page1, name='test_page1'),
    
    path('test_page2/', views.test_page2, name='test_page2'),
    
    path('make_user_ambassador/<int:department_id>/', views.make_user_ambassador, name='make_user_ambassador'),

]
