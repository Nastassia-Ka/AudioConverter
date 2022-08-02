import os

from django import forms
from django.core.exceptions import ValidationError

from AudioApp.models import UserSong
from .audiohandler.audio import AudioConverter


class UploadFileForm(forms.ModelForm):
    """Форма загрузки файла"""

    def clean_audio_file(self):
        """Проверка файла"""

        file = self.cleaned_data.get('audio_file', False)
        if file:
            if file.size > 10 * 1024 * 1024:
                raise ValidationError("Audio file too large ( > 10mb )")

            if not os.path.splitext(file.name)[1] in [".mp3", ".wav", '.ac3','.asf', '.Flac', '.mp4', '.mov', ".ogg"]:
                raise ValidationError("Doesn't have proper extension")

            return file
        else:
            raise ValidationError("Couldn't read uploaded file")

    class Meta:
        model = UserSong
        fields = ['audio_file']


class SelectFormatForm(forms.Form):
    """Форма выбора формата конвертирования."""

    converter_formats :list = AudioConverter.available_formats()
    formats_tuple :tuple = tuple(zip(tuple(converter_formats),tuple(converter_formats)))

    format :forms.Form = forms.ChoiceField(choices=formats_tuple)

