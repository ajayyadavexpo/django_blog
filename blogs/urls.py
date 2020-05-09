from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns=[
	path('',views.IndexView.as_view(), name='index'),
	# ex: /blogs/5/
    path('blog/<slug:the_slug>/', views.post_detail_view, name='show_post'),
]