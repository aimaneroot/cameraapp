# Generated by Django 2.2.6 on 2019-12-05 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cam', '0029_remove_camera_site'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camera',
            name='emplacements',
        ),
        migrations.AddField(
            model_name='camera',
            name='emplacements',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cam.Emplacement'),
        ),
    ]