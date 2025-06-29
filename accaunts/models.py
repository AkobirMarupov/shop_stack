from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import timedelta

from common.models import BaseModel
from accaunts.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    saved_products = models.ManyToManyField('products.Product', related_name='saved_by_users')
    is_confirmed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
    

class Cart(BaseModel):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.RESTRICT, null=False, blank=False, related_name="cart_items")
    product = models.ForeignKey('products.ProductVariant', on_delete=models.RESTRICT, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"CartItem({self.id})"
    

class Story(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='stories/images/', null=True, blank=True)
    video = models.FileField(upload_to='stories/videos/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    expires_at = models.DateTimeField(default=timezone.now() + timedelta(hours=24))


    def __str__(self):
        return self.title

    def is_expired(self):
        return timezone.now() > self.expires_at

    def view_count(self):
        return self.views.count()