from django.db import models
from django.contrib.auth.models import PermissionsMixin , AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from PIL import Image

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, name, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('name'), max_length=150, default='Anonymous', unique=False)
    age = models.PositiveIntegerField(_('age'), blank=True, null=True, validators=[MinValueValidator(18), MaxValueValidator(100)])
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        CLIENT = "CLIENT", "Client"
        ANALYST = "ANALYST", "Analyst"

    role = models.CharField(_('role'), max_length=50, choices=Role.choices, default=Role.CLIENT)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'age', 'role']

    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.email:
                raise ValidationError("Email address is required.")
            elif User.objects.filter(email=self.email).exists():
                raise ValidationError("Email address must be unique.")
            elif not self.role:
                self.role = self.Role.CLIENT
        super().save(*args, **kwargs)
class ClientManager(CustomUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Role.CLIENT)

class Client(User):
    base_role = User.Role.CLIENT
    objects = ClientManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Client"

class AnalystManager(CustomUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Role.ANALYST)

class Analyst(User):
    base_role = User.Role.ANALYST
    objects = AnalystManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Analysts"



class Post(models.Model):
    CATEGORY_CHOICES = [
        ('math', 'Math'),
        ('philosophy', 'Philosophy'),
        ('science', 'Science'),
        ('political', 'Political'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=250, blank=False)  # Required field
    text = models.TextField(blank=False)  # Required field
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES, blank=False)  # Required field
    author = models.CharField(max_length=100)  # You can adjust the max length as needed
    image = models.ImageField(upload_to='djangoposts/files/images', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set to the current date and time when created
    
    def __str__(self):
        return self.title
    
    def clean(self):
        if self.image:
            try:
                img = Image.open(self.image)
                if img.format not in ['JPEG', 'PNG', 'GIF']:
                    raise ValidationError("Only JPEG, PNG, and GIF formats are supported.")
            except:
                raise ValidationError("Invalid image file.")
            



#class PostImage(models.Model):
 #   post = models.ForeignKey(Post, default=None ,on_delete=models.CASCADE, related_name = "images")
  #  image = models.ImageField(upload_to='djangoposts/files/images', default="", null=True, blank=True)
   # 
    #def __str__(self):
     #   return self.post.title
