# Generated by Django 4.1.6 on 2023-02-14 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_album_options_alter_artist_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='songalbumm2m',
            options={'ordering': ('position',)},
        ),
        migrations.RemoveConstraint(
            model_name='songalbumm2m',
            name='unique_song_album',
        ),
        migrations.AddConstraint(
            model_name='songalbumm2m',
            constraint=models.UniqueConstraint(fields=('song', 'album', 'position'), name='unique_song_album'),
        ),
    ]
