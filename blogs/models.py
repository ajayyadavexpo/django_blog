from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Category(models.Model):
	category_text = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	def __str__(self):
		return self.category_text
	def was_published_recently(self):
		return self.pub_date>=timezone.now() - datetime.timedelta(days=1)
	def save(self, *args, **kwargs):
		self.slug = self.slug or slugify(self.category_text)
		super().save(*args, **kwargs)




class Post(models.Model):
	"""this is post model"""
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	image = models.ImageField(blank=True)
	post_text = models.TextField()
	pub_date = models.DateTimeField('Date published')
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	def __str__(self):
		return self.post_text
	def was_published_recently(self):
		return self.pub_date>=timezone.now() - datetime.timedelta(days=1)
	def save(self, *args, **kwargs):
		self.slug = self.slug or slugify(self.title)
		super().save(*args, **kwargs)



