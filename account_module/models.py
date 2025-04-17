from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    avatar=models.ImageField(upload_to='image/profile',verbose_name='تصویر آواتار',null=True,blank=True)
    email_activation_code=models.CharField(max_length=300,verbose_name='کد اعتبار سنجی')
    about=models.TextField(null=True,blank=True,verbose_name='درباره شخص')
    address=models.TextField(null=True,blank=True,verbose_name=' آدرس ')
    class Meta:
        verbose_name='کاربر'
        verbose_name_plural='کاربران'
    def __str__(self):
        return self.email