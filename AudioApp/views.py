from django.contrib.auth.models import User
from django.shortcuts import redirect, render, reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect

from .forms import *
from .models import *
from .utils.app_utils import handle_uploaded_file


def home_page(request):
    """Домашняя страница"""
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES or None)  # Привязка загруженных файлов к форме
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])  ## Нужна, если делаешь через модели
            form.save()  # Загрузка в директорию ./media/audio_files
            return HttpResponseRedirect('/success/url/')
    else:
        form = AudioForm()
    return render(request, 'AudioApp/home.html', {'form': form})


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

