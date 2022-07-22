import os

from django import forms
from django.core.exceptions import ValidationError
from AudioApp.models import *


class UploadFileForm(forms.ModelForm):
#     # Add some custom validation to our file field
#     def __init__(
#             self,
#             data=None,
#             files=None,
#             auto_id="id_%s",
#             prefix=None,
#             initial=None,
#             error_class=ErrorList,
#             label_suffix=None,
#             empty_permitted=False,
#             instance=None,
#             use_required_attribute=None,
#             renderer=None,
#     ):
#         super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance,
#                          use_required_attribute, renderer)
#         self.file = None


    def clean_audio_file(self):
        file = self.cleaned_data.get('audio_file', False)
        if file:
            if file.size > 10 * 1024 * 1024:
                raise ValidationError("Audio file too large ( > 10mb )")
            # if not file.content - type in ["audio/mpeg", "audio/..."]:
            #     raise ValidationError("Content-Type is not mpeg")
            if not os.path.splitext(file.name)[1] in [".mp3", ".wav", '.ac3','.asf', '.Flac', '.mp4', '.mov', ".ogg"]:
                raise ValidationError("Doesn't have proper extension")
            # Here we need to now to read the file and see if it actually
            # a valid audio file. I don't know what the best library is to
            # to do this
            return file
        else:
            raise ValidationError("Couldn't read uploaded file")

    class Meta:
        model = UserSong
        fields = ['audio_file']


