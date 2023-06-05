from . import views
from django.urls import path




#add urls foro app here

urlpatterns = [
    
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    
]