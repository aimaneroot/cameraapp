# Generated by Django 2.2.6 on 2019-11-16 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cam', '0017_auto_20191116_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camera',
            name='site',
        ),
        migrations.DeleteModel(
            name='Reparation',
        ),
        migrations.DeleteModel(
            name='Site',
        ),
    ]