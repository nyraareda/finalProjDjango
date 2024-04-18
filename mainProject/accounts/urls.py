from django.urls import path
from .views import user_create_form, verify, profile, add_additional_info, delete_account,edit_profile,login_view,custom_logout,request_password_reset,password_reset_confirm

urlpatterns = [
    path('verify/<str:key>/', verify, name='verify'),
    path('register/', user_create_form, name='user_create_form'),
    path('profile/<int:user_id>/', profile, name='profile'),
    path('add_additional_info/', add_additional_info, name='add_additional_info'),
    path('delete/<int:user_id>/', delete_account, name='delete_account'),
    path('edit/<int:user_id>/', edit_profile, name='edit_profile'),
    path('login/', login_view, name='login'),
    path('logout/<int:user_id>/', custom_logout, name='custom_logout'),
    path('password_reset/', request_password_reset, name='password_reset'),  # Password reset request view
    path('password_reset_confirm/<str:token>/', password_reset_confirm, name='password_reset_confirm'),  # Password reset confirmation view
]
