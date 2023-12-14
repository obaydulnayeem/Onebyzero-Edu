from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    
    path('login/', views.user_login, name='login'),
    
    path('logout/', views.user_logout, name='logout'),
    
    path('view_profile/', views.view_profile, name='view_profile'),
    
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    
    path('users/', views.user_list, name='user_list'),
    
    path('update_user_type/<int:user_id>/', views.update_user_type, name='update_user_type'),
    
    path('change_verification_status/<int:profile_id>/', views.change_verification_status, name='change_verification_status'),
    
    path('ajax/load-departments/', views.load_departments, name='ajax_load_departments'), # AJAX for dependant dropdown
    
    path('social-auth/', include('social_django.urls', namespace='social')), # for google auth
]
