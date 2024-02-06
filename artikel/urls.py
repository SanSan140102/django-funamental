from django.urls import path
from artikel import views

urlpatterns = [
    path('',views.index, name="artikel_index"),
    path('delete/<int:id>',views.delete,name='artikel.delete'),
    path('create/',views.create,name='artikel.create'),
    path('edit/<int:id>',views.edit,name='artikel.edit'),
]
