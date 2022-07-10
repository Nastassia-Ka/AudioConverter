import os
import subprocess


def chek_systempath(pathffmpeg :str) ->bool:
    """Проверяет наличие кодека ffmpeg  в системной переменной path Windows."""
    systempath :str = os.path.expandvars("$PATH") # Значение системной переменной

    ffmpeg :str = os.path.abspath(pathffmpeg) # Абсолютный путь кодека
    suf :str  = pathffmpeg[pathffmpeg.rfind("/"):].replace("/", "\\") # Получаем ,в качестве суфикса, приложение exe кодека и меняем слеши

    ffmpeg :str = ffmpeg.replace(suf, '') # Обрезаем суфикс,остовляем лишь путь
    if systempath.find(ffmpeg)> 0:
        return True
    else:
        return False


def create_backup_dir() ->str:
    """Создает папку для хранения резервной копии системной переменной Windows - path."""
    name:str = "system_path_backup"
    try:
        os.mkdir(name)
    except FileExistsError:
        pass
    return name


def create_backup_systempath(directory :str) ->str:
    """Создает резеврную копию системной переменной path."""
    pathstr :str = os.path.expandvars("$PATH")
    pathlist_draft :list[str] = pathstr.split(";")
    pathlist = []
    for i in pathlist_draft:
        if i.startswith("C:\Windows"):
            i = i.replace("C:\Windows", "%SystemRoot%")
        pathlist.append(i)
    pathlist.pop(-1)
    recovery_file = f"{directory}/Path.txt"
    with open(recovery_file, "w", encoding="utf-8") as f1:
        for i in pathlist:
            f1.write(i+"\n")
    return os.path.abspath(recovery_file)


def check_ffmpeg(ffmpeg :str) ->str:
    """Проверяет наличие кодека ffmpeg и директории bin."""
    if os.path.exists(ffmpeg):
        val = ffmpeg.find("bin/")
        if val > -1:
            suf: str = ffmpeg[ffmpeg.rfind("/"):].replace("/", "\\")

            return os.path.abspath(ffmpeg).replace(suf, "")
    return None


def addpath(path_ffmpeg :str) ->str:
    """Добалвяет путь в системную переменную path Windows."""
    # cmd = f'SETX MY_PATH "{path_ffmpeg}";"%PATH%" /M'
    # os.system(cmd)
    systempath :str = os.path.expandvars("$PATH")
    systempath = systempath.replace("C:\Windows", '%SystemRoot%')
    result :str = subprocess.check_output(['SETX', 'Path', f'{path_ffmpeg};{systempath}', '/M'], shell=True) #bytes, ecoding='cp866'
    reslultstr = result.decode("cp866")
    return reslultstr + "Перезапустите систему."




# Позволяет использвать кодек с бибилотекой pudub.Audiosigment и из командной строки
def connect_ffmpeg(ffmpeg :str, backup :bool = False, forcibly :bool = False ):
    """Подключает кодек ffmpeg."""
    # Записан ли кодек в системную переменную path ?
    flag: bool = chek_systempath(pathffmpeg=ffmpeg)

    # Перезаписать в любом случае.
    if forcibly == True:
        flag = False

    if flag == False:
        # Создать резервную копию системной  переменной path, если указано в агрументе
        if backup == True:
            # Создать папку для резевреной копиии
            dir :str = create_backup_dir()
            # Записать в текстовый файл все значения сист. перем. path
            create_backup_systempath(directory=dir)

        # Проверка налачия кодека и нужной папки bin
        path_ffmpeg :str = check_ffmpeg(ffmpeg=ffmpeg)
        if path_ffmpeg == None:
            raise Exception("ffmpegsitting.connect_ffmpeg.check_ffmpeg 'Codec not found'")
        try: # Обязятельно  с админ правами.
            result :str = addpath(path_ffmpeg=path_ffmpeg)
        except:
            print("connect_ffmpeg->addpath. Ошибка записи кодека в системную переменную path.")
        print(result)
        return result

    else:  # Если кодек уже записан в сист переменную path
        print("chek_systempath.ffmpeg кодек подключен.")
        return True










# Через bat
# def addpath(path_ffmpeg):
#     file_name = "add_ffmpeg_system_path.bat"
#     command = f'SETX MY_PATH "%PATH%";"{path_ffmpeg}" /M'
#     with open(file_name, "w", encoding="utf-8") as f:
#         f.write('@echo\n')
#         f.write(command)
#   # os.system(file_name)
#     return file_name