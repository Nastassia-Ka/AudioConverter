
from django.db import models

class UserSong(models.Model):
    title = models.CharField(max_length=100)
    audio_file = models.FileField()

    def __str__(self):
        return str(self.title) + str(self.audio_file)


class AudioStore(models.Model):
    record = models.FileField(upload_to='audio_files/')
    class Meta:
        db_table = 'AudioStore'

    def __str__(self):
        return str(self.record)
