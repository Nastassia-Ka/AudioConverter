from django.contrib.auth.models import User
from django.shortcuts import redirect, render, reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.template.loader import render_to_string

from .forms import *
from .models import *
from .utils.app_utils import handle_uploaded_file
from .audioconvert import AudioConverter


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            text = str(form.files['audio_file']).replace(' ', '_')
            trek_dict = AudioConverter.convert(f'AudioApp/media/audio_files/{text}', format='wav', login='Nastya')
            AudioConverter.write_db(trek_dict)
            conv_song = trek_dict['trek_convert']
            name = trek_dict['name']
            format = trek_dict['format']
            print(conv_song)
            return render(request, 'AudioApp/home.html', {'conv_song': conv_song, 'name': name, 'format': format})
    else:
        form = UploadFileForm()
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

