
from django.db import models


class AudioStore(models.Model):
    #  Данные из формы будут доступны во views как request.FILES['file']
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio_files')

    class Meta:
        db_table = 'AudioStore'

    def __str__(self):
        return str(self.audio_file) + str(self.title)
