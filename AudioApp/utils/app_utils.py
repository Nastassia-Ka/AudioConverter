# from django docs
import os

def handle_uploaded_file(f):
    """Обработка загруженного файла"""
    ext = os.path.splitext(f.name)[1]
    destination = open('media/audio_files/name%s'%(ext), 'wb+')
    for chunk in f.chunks():  # Чтобы файлы не перегружали память системы
        destination.write(chunk)
    destination.close()
