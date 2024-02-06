from django.urls import path
from member import views

urlpatterns = [
  path('',views.index,name='member.index'),
  path('delete/<int:id>',views.delete,name='member.delete'),
  path('create/',views.create,name='member.create'),
  path('edit/<int:id>',views.edit,name='member.edit'),
  

]