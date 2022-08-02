# from django.contrib.auth.models import User
from django.shortcuts import redirect, render, reverse
# from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect

from .forms import UploadFileForm, SelectFormatForm
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

    select = SelectFormatForm()

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            text :str= str(form.files['audio_file']).replace(' ', '_')
            print(text)
            frmt = request.POST.get('format')

            # Конвертирование аудиофайла и сохранение информации о нем в базу данных
            trek_dict : dict = converter.convert(f'AudioApp/media/audio_files/{text}', frmt=frmt, name='Admin')
            flag: bool = write_database(trek_dict)

            # Инфа о файле в шаблон
            trek_name :str= trek_dict['trek_name']
            trek_format :str = trek_dict['format']
            audio :str= trek_dict['path_convert'].replace('AudioApp/static/', '')

            context :dict = {'form': form,
                       'trek_name': trek_name,
                       'format': trek_format,
                        'audio':audio,
                       'select': select,
                       }

            return render(request,  'AudioApp/home.html', context=context)
            # return redirect('home')
    else:
        form = UploadFileForm()
        context :dict = {'form': form,
                        'select': select,
                         }

        return render(request, 'AudioApp/home.html',context=context)


def user_account(request):
    return render(request, 'AudioApp/user.html')

def about(request):
    return render(request, 'AudioApp/about.html')

def deletion_page(request):
    return render(request, 'AudioApp/deletion.html')

def login(request):
    return render(request, 'AudioApp/login.html')



