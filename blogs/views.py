from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponseRedirect
from .models import Post,Category
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import RegisterForm,LoginForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'latest_blog_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	# This file should exist somewhere to render your page
	template_name = 'blogs/detail.html'
	# Should match the value after ':' from url <slug:the_slug>
	slug_url_kwarg = 'the_slug'
	# Should match the name of the slug field on the model 
	slug_field = 'slug' # DetailView's default value: optional
	def get_queryset(self):
		""" Excludes any Posts that aren't published yet."""
		return Post.objects.filter(pub_date__lte=timezone.now())

post_detail_view = DetailView.as_view()

def navbar(request):
	return render(request,'blogs/navbar.html',{'category':Category.objects.filter()})

def home(request):
	return render(request,'blogs/home.html')

def Userregister(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect("blogs:home")
	else:
		form = RegisterForm()
	return render(request, "blogs/register.html", {"form":form})



def Userlogin(request):
	if request.method == "POST":
		form = LoginForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect('blogs:home')
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")
	else:
		form = LoginForm()
		return render(request,'blogs/login.html',{'form':form})



def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("/")