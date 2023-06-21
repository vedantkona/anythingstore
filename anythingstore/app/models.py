from django.db import models
from django.contrib.auth.models import User
from  django.core.validators import FileExtensionValidator

class VideoFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='video_files/', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mp3'])])

    def __str__(self):
        return self.file.name

class AudioFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='audio_files/',validators=[FileExtensionValidator(allowed_extensions=['m4a', 'flac', 'mp3','wav'])])

    def __str__(self):
        return self.file.name

class TextFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='text_files/', validators=[FileExtensionValidator(allowed_extensions=['txt', 'pdf', 'doc','docx'])])

    def __str__(self):
        return self.file.name