# Generated by Django 3.1.13 on 2021-09-22 20:47

import albums.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("albums", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="album",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="album",
            name="blog",
            field=models.TextField(blank="", null=True),
        ),
        migrations.AlterField(
            model_name="album",
            name="description",
            field=models.CharField(blank="", max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name="album",
            name="pub_date",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="date published"
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="description",
            field=models.CharField(blank="", max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="tag",
            name="description",
            field=models.CharField(blank="", max_length=200, null=True),
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="pictures/")),
                ("caption", models.CharField(blank="", max_length=400, null=True)),
                (
                    "album",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="albums.album",
                    ),
                ),
                ("locations", models.ManyToManyField(to="albums.Location")),
            ],
        ),
    ]
