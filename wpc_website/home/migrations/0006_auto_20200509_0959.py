# Generated by Django 3.0.5 on 2020-05-09 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200507_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='home_video_url',
            field=models.URLField(blank=True, help_text='Paste the video url from youtube.', null=True, verbose_name='Video URL'),
        ),
    ]
