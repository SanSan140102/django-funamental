from django.urls import path
from news import views

urlpatterns = [
  
  
   path('category/',views.index_category,name='category.index'),
   path('category/<int:id>',views.detail_category),
   path('category/delete/<int:id>',views.delete_category,name='category.delete'),
   path('category/create/',views.create_category,name='category.create'),
   path('category/edit/<int:id>',views.edit_category,name='category.edit'),
  
  
  path('',views.index_news,name='news.index'),
  path('<int:id>',views.detail_news,name='news.detail'),
  path('delete/<int:id>',views.delete_news,name='news.delete'),
  path('create/',views.create_news,name='news.create'),
  path('edit/<int:id>',views.edit_news,name='news.edit'),
 
  
]