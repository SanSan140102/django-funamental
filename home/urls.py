from django.urls import path
from home import views



urlpatterns = [
    path('',views.index_home,name='home_index'),
    path('berita/<str:slug>/',views.news_Detail,name='home.news_detail'),
    path('list/<str:category>/',views.news_Category,name='home.news_category'),
    path('komentar/<str:slug>',views.tambah_komentar,name='tambah_komentar'),
    path('replay/<str:slug>/<int:id>',views.replay_komentar,name='replay'),
    path('ajax/',views.load_ajax,name='home.load_ajax'),
    path('ajax/data/',views.ajax_data,name='home.ajax_data'),
    path('news/like/<int:newsId>',views.news_like,name='home.news_like')
    
]
