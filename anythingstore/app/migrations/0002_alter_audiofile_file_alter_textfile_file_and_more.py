# Generated by Django 4.2.2 on 2023-06-20 18:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='file',
            field=models.FileField(upload_to='audio_files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['m4a', 'flac', 'mp3', 'wav'])]),
        ),
        migrations.AlterField(
            model_name='textfile',
            name='file',
            field=models.FileField(upload_to='text_files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['txt', 'pdf', 'doc', 'docx'])]),
        ),
        migrations.AlterField(
            model_name='videofile',
            name='file',
            field=models.FileField(upload_to='video_files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mp3'])]),
        ),
    ]