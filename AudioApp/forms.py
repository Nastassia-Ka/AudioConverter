import os

from django import forms
from django.core.exceptions import ValidationError


class UserSongForm(forms.ModelForm):
    # Add some custom validation to our file field
    def clean_audio_file(self, some_lib=None):
        file = self.cleaned_data.get('audio_file', False)
        if file:
            if file._size > 4 * 1024 * 1024:
                raise ValidationError("Audio file too large ( > 4mb )")
            if not file.content - type in ["audio/mpeg", "audio/..."]:
                raise ValidationError("Content-Type is not mpeg")
            if not os.path.splitext(file.name)[1] in [".mp3", ".wav", '.ac3', '.asf', '.flak', '.mp4', '.mov', '.ogg']:
                raise ValidationError("Doesn't have proper extension")
            # Here we need to now to read the file and see if it actually
            # a valid audio file. I don't know what the best library is to
            # to do this
            if not some_lib.is_audio(file.content):
                raise ValidationError("Not a valid audio file")
            return file
        else:
            raise ValidationError("Couldn't read uploaded file")

