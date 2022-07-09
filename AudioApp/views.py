from django.contrib.auth.models import User
from django.shortcuts import redirect, render, reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect

from .forms import *
from .models import *
from .utils.app_utils import handle_uploaded_file

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Кабинет пользователя', 'url_name': 'user_account'},
        {'title': 'Войти', 'url_name': 'login'},
        ]

def home_page(request):
    """Домашняя страница"""
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = AudioForm()
    return render(request, 'AudioApp/home.html', {'menu': menu, 'forms': form})


def user_account(request):
    return render(request, 'AudioApp/user.html')

def about(request):
    return render(request, 'AudioApp/about.html')

def deletion_page(request):
    return render(request, 'AudioApp/deletion.html')

def login(request):
    return render(request, 'AudioApp/login.html')


# def upload_file(request):
#     if request.method == 'POST':
#         form = UserSongForm(request.POST, request.FILES)
#         if form.is_valid():
#             # If we are here, the above file validation has completed
#             # so we can now write the file to disk
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render_to_response('upload.html', {'form': form})

