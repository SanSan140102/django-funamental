from django.urls import path
from sansan import views

urlpatterns = [
  path('',views.index,name='barang.index'),
  path('create/',views.create,name='barang.create'),

]