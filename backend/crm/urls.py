from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [ 
    path('', views.homepage, name=""),

    # path("products", views.ApiProducts.as_view()),
    path('create_post', views.PostsViewSet, name='create-post'),

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),
    
    path('dashboard', views.dashboard, name="dashboard"),
    
    path('user-logout', views.user_logout, name="user-logout"),

    
    #-*=-09876 1path('create-post/', views.create_post_view, name='create-post'),
    
    #path('<int:id>/', views.detail_view, name='detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)