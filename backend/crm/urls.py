from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 
from . import views
from rest_framework.routers import DefaultRouter
from .views import PostCreateAPIView

urlpatterns = [ 
    path('', views.homepage, name=""),

    # path("products", views.ApiProducts.as_view()),
    

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),
    
    path('dashboard', views.dashboard, name="dashboard"),
    
    path('user-logout', views.user_logout, name="user-logout"),
    
    path('create_post', PostCreateAPIView.as_view(), name='create_post'),

    #path('posts/', views.create_post, name='create_post'),

    path('posts/<int:pk>/', views.get_post, name='get_post'),  
    
    path('posts/<int:pk>/update/', views.update_post, name='update_post'),
    
    path('posts/<int:pk>/delete/', views.delete_post, name='delete_post'),

    
    #-*=-09876 1path('create-post/', views.create_post_view, name='create-post'),
    
    #path('<int:id>/', views.detail_view, name='detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)