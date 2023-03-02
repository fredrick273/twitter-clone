from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="Home"),
    path('user/',views.profileRedirect,name="user"),
    path('register/',views.register,name="register"),
    path('login/',views.userLogin,name="login"),
    path('tweets/',views.tweets,name="tweets"),
    path('logout/',views.userLogout,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('create/',views.createTweet,name= "create"),
    path('user/<str:username>',views.userpage),
    path('tweet/<int:tweetid>',views.tweet),
    path('tweet/',views.home,name='tweet'),
    path('liketweet/',views.liketweet,name='like'),
    path('follow/',views.follow,name="follow")
]