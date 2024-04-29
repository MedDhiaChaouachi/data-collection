from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


from django import forms 

from django.forms.widgets import PasswordInput, TextInput


#
from django.forms import ModelForm
from .models import Post
# - Create/Register a user from django.forms import MultipleFileInput #from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField
# - from django.forms import ClearableFileInput

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


# - Authenticate a user (Model Form)

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

#class UploadForm(ModelForm):
#   title = forms.TextInput()
#    text = forms.CharField(widget=forms.Textarea)
#    category = forms.ChoiceField(choices=Post.CATEGORY_CHOICES)
#    author = forms.TextInput()
#    images = forms.FileField(widget=MultipleFileInput(attrs={'multiple': True}))  # Use MultipleFileInput for multiple file uploads
#    class Meta:
    #    model = Post
    #s   fields = ['title', 'text','category','author','images']
