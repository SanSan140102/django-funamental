from  django.urls import path
from login import views



urlpatterns = [
    
    path('login/',views.index,name='login.index'),
    path('logut/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    
]