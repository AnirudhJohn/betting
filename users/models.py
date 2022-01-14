from django.db.models import manager
from autoslug import AutoSlugField
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from datetime import date


class CustomUser(AbstractUser):
    pass


class Profile(models.Model):

    CustomUser = get_user_model()

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    INTERESTS = (
        ('Poetry', 'Poetry'),
        ('Short-Stories', 'Short Stories',),
        ('Novels', 'Novels',),
    )



    name = models.CharField(max_length=30, blank=True, null=True)
    
    interset = models.CharField(max_length=15, choices=INTERESTS, null=True)
    
    birth_date = models.DateField(null=True, blank=True)
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    
    user = models.OneToOneField(CustomUser, primary_key=True,verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    
    profile_pic = models.ImageField(
        default='default.png', upload_to='profile_pics', null=True)
    
    slug = AutoSlugField(populate_from='user')
    
    bio = models.CharField(max_length=500, blank=True)
    
    location = models.CharField(max_length=100, blank=True, null=True)

    followers = models.ManyToManyField(CustomUser, blank=True, related_name='followers')

    def __str__(self):
        return str(self.user.username)

    def get_absolute_url(self):

        return "/users/{}".format(self.slug)


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass


post_save.connect(post_save_user_model_receiver,
                  sender=settings.AUTH_USER_MODEL)


class FriendRequest(models.Model):
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "From {}, to {}".format(self.from_user.username, self.to_user.username)
