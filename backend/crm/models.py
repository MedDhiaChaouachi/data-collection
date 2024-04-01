from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

# Custom manager for User model
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

# Define the custom user model
class User(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('name'), max_length=150, default='Anonymous',unique=False)
    age = models.PositiveIntegerField(_('age'), blank=True, null=True, validators=[MinValueValidator(18), MaxValueValidator(100)])
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)

    # Define choices for the role field
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        CLIENT = "CLIENT", "Client"
        ANALYST = "ANALYST", "Analyst"

    # Define the role field
    role = models.CharField(_('role'), max_length=50, choices=Role.choices, default=Role.CLIENT)

    # Define the custom user manager
    objects = CustomUserManager()

    # Define the field used as the unique identifier for logging in
    USERNAME_FIELD = 'email'

    # Define additional fields required for creating a user
    REQUIRED_FIELDS = ['name']

    # Override the save method to ensure email uniqueness and presence
    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.email:
                raise ValidationError("Email address is required.")
            elif User.objects.filter(email=self.email).exists():
                raise ValidationError("Email address must be unique.")
            else:
                self.role = self.base_role
        super().save(*args, **kwargs)

# Custom manager for Client model to filter clients
class ClientManager(CustomUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CLIENT)

# Proxy model for clients
class Client(User):
    # Override base_role for clients
    base_role = User.Role.CLIENT

    
    # Associate manager with the client model
    client = ClientManager()

    class Meta:
        proxy = True

    # Example method specific to clients
    def welcome(self):
        return "Only for Client"

# Signal receiver to create client profile after client creation
@receiver(post_save, sender=Client)
def create_client_profile(sender, instance, created, **kwargs):
    if created:
        ClientProfile.objects.create(user=instance)

# Model for client profile
class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    client_id = models.IntegerField(null=True, blank=True)

# Custom manager for Analyst model to filter analysts
class AnalystManager(CustomUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.ANALYST)

# Proxy model for analysts
class Analyst(User):
    # Override base_role for analysts
    base_role = User.Role.ANALYST

    # Associate manager with the analyst model
    analyst = AnalystManager()

    class Meta:
        proxy = True

    # Example method specific to analysts
    def welcome(self):
        return "Only for Analysts"

# Signal receiver to create analyst profile after analyst creation
@receiver(post_save, sender=Analyst)
def create_analyst_profile(sender, instance, created, **kwargs):
    if created:
        AnalystProfile.objects.create(user=instance) 

# Model for analyst profile
class AnalystProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    analyst_id = models.IntegerField(null=True, blank=True)