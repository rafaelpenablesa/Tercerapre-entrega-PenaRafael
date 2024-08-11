from django.urls import path
from . import views
from .views import custom_logout

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
   path('logout/', custom_logout, name='logout'),
]
