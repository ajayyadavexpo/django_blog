from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime
# Create your models here.

User = settings.AUTH_USER_MODEL

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
	user = models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
	ORDER_STATUS = ((0, 'draft'), (1, 'publish'))
	status = models.SmallIntegerField(choices=ORDER_STATUS)

	def __str__(self):
		return self.title
	def was_published_recently(self):
		return self.pub_date>=timezone.now() - datetime.timedelta(days=1)
	def save(self, *args, **kwargs):
		self.slug = self.slug or slugify(self.title)
		super().save(*args, **kwargs)

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'



