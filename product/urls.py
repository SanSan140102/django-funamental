from django.urls import path
from product import views

urlpatterns = [
  path('',views.index,name='product.index'),
  path('<int:id>',views.detail),
  path('calculator/<int:bil1>/<int:bil2>',views.calculator),
  path('delete/<int:id>',views.delete,name='product.delete'),
  path('create/',views.create,name='product.create'),
  path('edit/<int:id>',views.edit,name='product.edit'),
  

]