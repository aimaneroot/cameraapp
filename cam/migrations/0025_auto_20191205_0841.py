# Generated by Django 2.2.6 on 2019-12-05 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cam', '0024_auto_20191205_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emplacementcamera',
            name='camera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cam.Camera'),
        ),
        migrations.AlterField(
            model_name='emplacementcamera',
            name='emplacement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cam.Emplacement'),
        ),
    ]
