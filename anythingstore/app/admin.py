from django.contrib import admin
from .models import AudioFile,TextFile,VideoFile



admin.site.register(AudioFile)
admin.site.register(TextFile)
admin.site.register(VideoFile)