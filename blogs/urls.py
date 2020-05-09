from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns=[
	path('',views.IndexView.as_view(), name='index'),
	# ex: /blogs/5/
    path('blogs/<int:pk>/', views.DetailView.as_view(), name='detail'),
]