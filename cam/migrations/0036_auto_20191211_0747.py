# Generated by Django 2.2.6 on 2019-12-11 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cam', '0035_camera_fournisseur'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fournisseur',
            old_name='societé',
            new_name='société',
        ),
    ]
