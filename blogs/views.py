from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect
from .models import Post,Category
from django.urls import reverse
from django.views import generic
from django.utils import timezone

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

def register(request):
	return render(request,'blogs/register.html',{'category':Category.objects.filter()})

def login(request):
	return render(request,'blogs/login.html',{'category':Category.objects.filter()})

