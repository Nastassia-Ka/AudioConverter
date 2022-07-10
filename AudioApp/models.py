
from django.db import models


class UserSong(models.Model):
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio_files/')


    def __str__(self):
        return str(self.audio_file) + str(self.title)


class TrackData(models.Model):
    login = models.CharField(max_length=100)
    original_tracks = models.CharField(max_length=100)
    convertable_tracks = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

    def __str__(self):
        return str(self.date)



