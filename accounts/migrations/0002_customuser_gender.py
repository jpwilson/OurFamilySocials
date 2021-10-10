# Generated by Django 3.1.13 on 2021-10-10 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('refuse', 'Choose not to say')], default='refuse', max_length=32),
        ),
    ]