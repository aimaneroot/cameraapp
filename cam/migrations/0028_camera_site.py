# Generated by Django 2.2.6 on 2019-12-05 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cam', '0027_remove_camera_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cam.Site'),
        ),
    ]
