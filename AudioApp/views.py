from django.contrib.auth.models import User
from django.shortcuts import redirect, render, reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.template.loader import render_to_string

from .forms import *
from .models import *
from .utils.app_utils import handle_uploaded_file
from .audiohandler.audio import AudioConverter
from .utils.database import write_database
from AudioConverter.settings import STATIC_URL # файлы статики

#Converter setiings
settings = {
        'move': True, # Перемещать (не копировать) файлы в папку конвертированных
        'write_db': False, # Использовать стандартную базу данных конвертора
        'db_path': '', # Путь к стандартной базе данных конвертора
        'storage_path': f'AudioApp{STATIC_URL}', # Путь, где будут храниться конвертированные файлы
        }
#object converter
converter = AudioConverter(setting_dict=settings)



def upload_file(request):
    """Загрузка аудио и его конвретирвоание."""
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            text :str= str(form.files['audio_file']).replace(' ', '_')
            # Конвертирование аудиофайла и сохранение информации о нем в базу данных
            trek_dict : dict = converter.convert(f'AudioApp/media/audio_files/{text}', frmt='wav', name='Admin')
            flag: bool = write_database(trek_dict)

            # Инфа о файле в шаблон
            trek_name :str= trek_dict['trek_name']
            trek_format :str = trek_dict['format']
            audio :str= trek_dict['path_convert'].replace('AudioApp/static/', '')
            context = {'form': form,
                       'trek_name': trek_name,
                       'format': trek_format,
                        'audio':audio,
                       }

            print(audio)
            return render(request,  'AudioApp/home.html', context=context)
            # return redirect('home')
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

