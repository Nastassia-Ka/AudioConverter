from .ffmpegsetting import connect_ffmpeg
# Только относительный путь к кодку ffmpeg
ffmpeg = "AudioApp/ffmpeg/bin/ffmpeg.exe"
connect_ffmpeg(ffmpeg = ffmpeg, backup=True, forcibly= False)

from pydub import AudioSegment
import os
import shutil
from datetime import datetime

from .models import TrackData


class AudioConverter():
    """Аудио конвертер."""

    formats :list[str] = ['ac3','asf', 'Flac', 'mp3', 'mp4','mov', "ogg", 'wav',] # '-AAC' '-DTS' '-wma'
    dir_original_traks :str = 'AudioApp/media/original_traks'
    dir_convertible_traks :str = 'AudioApp/media/convertible_tracks'
    try:
        os.mkdir(dir_original_traks)
        os.mkdir(dir_convertible_traks)
    except FileExistsError:
        pass

    @classmethod
    def create_user_dir(cls,login :str)->dict:
        """Создает директории хранения оригинальных и  конвертируемых треков."""
        dir_name = login.replace(" ", "_")
        user_dir_orig = AudioConverter.dir_original_traks + "/" + dir_name
        user_dir_convert = AudioConverter.dir_convertible_traks + "/" + dir_name

        # Если  директории существуют- нечего не делать
        try:
            os.mkdir(user_dir_orig)
            os.mkdir(user_dir_convert)
        except FileExistsError:
            pass

        user_dirs = {'user_orig': user_dir_orig,
                     'user_convert':user_dir_convert
                     }

        return user_dirs


    @classmethod
    def convert(cls, pathsound :str, format :str, login :str = ''):
        """Конвертирует в треки в указанный формат."""
        # Проверка указанного формата
        if format.lower()  not in AudioConverter.formats:
            raise Exception("AudioConverter.convert 'Unknown format'")

        # Директории  пользователя. Оригинальные и конвертируемые треки
        user_dirs :dict = AudioConverter.create_user_dir(login)

        trek_name: str = pathsound[pathsound.rfind("/") + 1:pathsound.rfind(".")]
        trek_frmt: str = format.lower()

        trek :object = AudioSegment.from_file(pathsound)
        trek.export(f"{user_dirs['user_convert']}/{trek_name}.{trek_frmt}", format=trek_frmt)

        # Перемещение оргинального трека в директорию пользователя
        try:
            trek_orig =  shutil.move(pathsound, user_dirs['user_orig']).replace('\\', "/")
        except shutil.Error:
            os.remove(user_dirs['user_orig']+ pathsound[pathsound.rfind("/"):])
            trek_orig = shutil.move(pathsound, user_dirs['user_orig']).replace('\\', "/")

        date :datetime = str(datetime.now())

        result :dict = {
            "login": login,
            "trek_orig": trek_orig,
            "trek_convert": f"{user_dirs['user_convert']}/{trek_name}.{trek_frmt}",
            "date": date,
            "name": trek_name,
            "format": trek_frmt,
                 }
        return result

    @classmethod
    def show_formats(cls):
        return AudioConverter.formats

    @classmethod
    def write_db(cls,data_dict):
        login = data_dict['login']
        orig = data_dict['trek_orig']
        convert = data_dict['trek_convert']
        date = data_dict['date']
        # print(login,orig,convert,date)
        ex = TrackData(login=login, original_tracks=orig, convertable_tracks=convert, date=date)
        ex.save()
        # for item in TrackData.objects.all():
        #     print(item.login)







if __name__ == '__main__':
    sound = "original_traks/testsong.mp3"
    t = AudioConverter.convert(sound, "wav", "Alex" )


