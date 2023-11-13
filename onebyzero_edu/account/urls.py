from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

from .views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    
    path('login/', views.user_login, name='login'),
    
    path('logout/', views.user_logout, name='logout'),
    
    path('view_profile/', views.view_profile, name='view_profile'),
    
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    
    path('users/', views.user_list, name='user_list'),
    
    path('update_user_type/<int:user_id>/', views.update_user_type, name='update_user_type'),
    
    path('ajax/load-departments/', views.load_departments, name='ajax_load_departments'), # AJAX for dependant dropdown
    
    path('social-auth/', include('social_django.urls', namespace='social')), # for google auth
    
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
