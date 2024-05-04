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
from .serializers import  PostCreateSerializer, PostRetrieveSerializer, PostDeleteSerializer,PostUpdateSerializer

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


@api_view(['POST'])
@permission_classes([AllowAny])
def create_post(request):
    serializer = PostCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = PostRetrieveSerializer(post)
    return Response(serializer.data)

@api_view(['PUT'])
def update_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = PostUpdateSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_post(request, pk):
    serializer = PostDeleteSerializer(data={'id': pk})
    if serializer.is_valid():
        post_id = serializer.validated_data['id']
        Post.objects.filter(pk=post_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@login_required(login_url="my-login")
def dashboard(request):

    return render(request, 'crm/dashboard.html') 




