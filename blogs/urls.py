from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns=[
	path('',views.IndexView.as_view(), name='index'),
	# ex: /blogs/5/
    path('blog/<slug:the_slug>/', views.post_detail_view, name='show_post'),
    path('navbar/', views.navbar, name='navbar'),
    path('register/', views.Userregister, name='userregister'),
    path('login/', views.Userlogin, name='userlogin'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_request, name='logout'),
]