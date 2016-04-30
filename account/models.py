from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class MyUser(AbstractUser):
	profile_pic=models.ImageField(upload_to='profile_pics/',default='profile_pics/default.jpg')
	sex=models.CharField(max_length=10,null=True,blank=True)
	age=models.IntegerField(null=True,blank=True)
	phone=models.IntegerField(null=True,blank=True)
	address=models.CharField(max_length=200,null=True,blank=True)
	stars=models.IntegerField(null=True,blank=True)
	about=models.TextField(max_length=10000,null=True,blank=True)
	following = models.ManyToManyField("self", symmetrical = False, related_name = "followers",null=True,blank=True)

