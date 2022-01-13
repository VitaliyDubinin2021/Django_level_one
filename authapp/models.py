from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')

    activation_key = models.CharField(max_length=256, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=72)))

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True