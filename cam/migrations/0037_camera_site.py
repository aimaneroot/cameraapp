# Generated by Django 2.2.6 on 2019-12-12 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cam', '0036_auto_20191211_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cam.Site'),
        ),
    ]