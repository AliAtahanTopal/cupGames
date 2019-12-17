from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/<str:pk>/', views.gamepage, name='gamepage'),
    path('category/<str:pk>', views.categorypage, name='categorypage'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logoutpage', views.logoutpage, name='logoutpage'),
    path('profile', views.profile, name='profile'),
    path('becomepremium', views.becomepremium, name='becomepremium'),
    path('leaderboards', views.leaderboards, name='leaderboards')

]
