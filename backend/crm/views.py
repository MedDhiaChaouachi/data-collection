from django.shortcuts import render ,redirect ,get_object_or_404          
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .forms import CreateUserForm, LoginForm
from rest_framework.response import Response
from rest_framework import status
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
#, UploadForm
from rest_framework.decorators import api_view, permission_classes, action

from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Post

# - Authentication models and functions 
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate, login, logout

def homepage(request):

    return render(request, 'crm/index.html')

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("my-login")

    context = {'registerform':form}

    return render(request, 'crm/register.html', context=context)



def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username,password=password)

            if user is not None :

                auth.login(request, user)

                return redirect("dashboard")

    
    context = {'loginform':form}

    return render(request, 'crm/my-login.html', context=context)

def user_logout(request):
    auth.logout(request)
    
    return redirect("")

#def upload(request):
#   if request.POST:
#      form = UploadForm(request.POST, request.FILES)
#     print(request.FILES)
    #    if form.is_valid():
#       form.save_()
#  return redirect(homepage)
    #return render(request, 'crm/upload.html', {'form' : UploadForm })


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



@login_required(login_url="my-login")
def dashboard(request):

    return render(request, 'crm/dashboard.html') 




