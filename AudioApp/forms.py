import os

from django import forms
from django.core.exceptions import ValidationError
from AudioApp.models import *


class AudioForm(forms.ModelForm):
    def clean_audio_file(self, some_lib=None):
        file = self.cleaned_data.get('audio_file', False)
        if file:
            if file.size > 10 * 1024 * 1024:
                raise ValidationError("Файл слишком большой ( > 10mb )")  #Нужно ли?
            # if not file.content - type in ["audio/mpeg","audio/..."]:
            #     raise ValidationError("Content-Type is not mpeg")  ## - не понимаю что это
            if not os.path.splitext(file.name)[1] in [".mp3", ".wav", '.ac3', '.asf', '.flak', '.mp4', '.mov', '.ogg']:
                raise ValidationError("Выберите другой формат файла")
            # if not some_lib.is_audio(file.content):
            #     raise ValidationError("Недействительный аудиофайл")  ## Тоже хз что и зачем
            return file
        else:
            raise ValidationError("Couldn't read uploaded file")
    class Meta:
        model = AudioStore
        fields = ['audio_file']



