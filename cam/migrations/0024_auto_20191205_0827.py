# Generated by Django 2.2.6 on 2019-12-05 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cam', '0023_emplacementcamera_reparation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emplacementcamera',
            name='reparation',
            field=models.ForeignKey(blank=True, default='DEFAULT VALUE', null=True, on_delete=django.db.models.deletion.CASCADE, to='cam.Reparation'),
        ),
    ]
