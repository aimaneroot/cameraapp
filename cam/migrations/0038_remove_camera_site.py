# Generated by Django 2.2.6 on 2019-12-12 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cam', '0037_camera_site'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camera',
            name='site',
        ),
    ]
