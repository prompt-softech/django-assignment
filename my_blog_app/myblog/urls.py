from django.urls import path
from .views.user import views_user
from .views.post import views_post

urlpatterns = [
    path('', views_user.index, name='index'),
    path('login/', views_user.login_user),
    path('logout/', views_user.logout_user),
    path('usersignup/', views_user.user_signup),
    path('addmessage/', views_post.add_post),
]
