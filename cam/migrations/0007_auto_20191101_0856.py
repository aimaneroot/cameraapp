# Generated by Django 2.2.6 on 2019-11-01 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cam', '0006_reparation_camera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='nom',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='nom',
            field=models.CharField(max_length=250, null=True),
        ),
    ]