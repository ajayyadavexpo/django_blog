from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Post
from slugify import slugify



class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
    	model = User
    	fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    class Meta:
    	model = User
    	fields = ["email", "password"]


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ["title","image","post_text","category","status"]