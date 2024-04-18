from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)  # Ensure username is unique
    email = models.EmailField(unique=True)  # Ensure email is unique
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='users/images', null=True, blank=True)
    facebook_profile = models.URLField(max_length=200, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    is_activated = models.BooleanField(default=False)
    activation_key = models.CharField(max_length=64, blank=True)
    reset_token = models.CharField(max_length=100, blank=True, null=True)

    # Add related_name attributes to resolve clashes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='user_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='user_permissions_set'
    )

    def save(self, *args, **kwargs):
        # Ensure that the username and email are not empty
        if not self.username:
            raise ValidationError("Username cannot be empty.")
        if not self.email:
            raise ValidationError("Email cannot be empty.")
        # Perform additional actions before saving the user
        super().save(*args, **kwargs)

    @property
    def profile_picture_url(self):
        if self.profile_picture:
            return self.profile_picture.url
        return '/path/to/default/profile/picture.jpg'
