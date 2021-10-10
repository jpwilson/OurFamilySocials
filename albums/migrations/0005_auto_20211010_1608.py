# Generated by Django 3.1.13 on 2021-10-10 21:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('albums', '0004_auto_20210924_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='locations',
            field=models.ManyToManyField(blank=True, to='albums.Location'),
        ),
        migrations.AlterField(
            model_name='album',
            name='people',
            field=models.ManyToManyField(blank=True, related_name='people', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='album',
            name='tags',
            field=models.ManyToManyField(blank=True, to='albums.Tag'),
        ),
        migrations.AlterField(
            model_name='image',
            name='locations',
            field=models.ManyToManyField(blank=True, to='albums.Location'),
        ),
    ]
